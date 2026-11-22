# // Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# //
# // Licensed under the Apache License, Version 2.0 (the "License");
# // you may not use this file except in compliance with the License.
# // You may obtain a copy of the License at
# //
# //     http://www.apache.org/licenses/LICENSE-2.0
# //
# // Unless required by applicable law or agreed to in writing, software
# // distributed under the License is distributed on an "AS IS" BASIS,
# // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# // See the License for the specific language governing permissions and
# // limitations under the License.
import spaces
import subprocess

import os
import torch
import mediapy
from einops import rearrange
from omegaconf import OmegaConf
print(os.getcwd())
import datetime
from tqdm import tqdm
import gc

from data.image.transforms.divisible_crop import DivisibleCrop
from data.image.transforms.na_resize import NaResize
from data.video.transforms.rearrange import Rearrange
if os.path.exists("./projects/video_diffusion_sr/color_fix.py"):
    from projects.video_diffusion_sr.color_fix import wavelet_reconstruction
    use_colorfix=True
else:
    use_colorfix = False
    print('Note!!!!!! Color fix is not avaliable!')
from torchvision.transforms import Compose, Lambda, Normalize
from torchvision.io.video import read_video
import argparse
from PIL import Image

from common.distributed import (
    get_device,
    init_torch,
)

from common.distributed.advanced import (
    get_data_parallel_rank,
    get_data_parallel_world_size,
    get_sequence_parallel_rank,
    get_sequence_parallel_world_size,
    init_sequence_parallel,
)

from projects.video_diffusion_sr.infer import VideoDiffusionInfer
from common.config import load_config
from common.distributed.ops import sync_data
from common.seed import set_seed
from common.partition import partition_by_groups, partition_by_size

import gradio as gr
from pathlib import Path
from urllib.parse import urlparse
from torch.hub import download_url_to_file, get_dir
import shlex
import uuid
import mimetypes
import torchvision.transforms as T

os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = "12355"
os.environ["RANK"] = str(0)
os.environ["WORLD_SIZE"] = str(1)

subprocess.run(
    "pip install flash-attn --no-build-isolation",
    env={"FLASH_ATTENTION_SKIP_CUDA_BUILD": "TRUE"},
    shell=True,
)

def load_file_from_url(url, model_dir=None, progress=True, file_name=None):
    """Load file from http url, will download models if necessary.

    Reference: https://github.com/1adrianb/face-alignment/blob/master/face_alignment/utils.py

    Args:
        url (str): URL to be downloaded.
        model_dir (str): The path to save the downloaded model. Should be a full path. If None, use pytorch hub_dir.
            Default: None.
        progress (bool): Whether to show the download progress. Default: True.
        file_name (str): The downloaded file name. If None, use the file name in the url. Default: None.

    Returns:
        str: The path to the downloaded file.
    """
    if model_dir is None:  # use the pytorch hub_dir
        hub_dir = get_dir()
        model_dir = os.path.join(hub_dir, 'checkpoints')

    os.makedirs(model_dir, exist_ok=True)

    parts = urlparse(url)
    filename = os.path.basename(parts.path)
    if file_name is not None:
        filename = file_name
    cached_file = os.path.abspath(os.path.join(model_dir, filename))
    if not os.path.exists(cached_file):
        print(f'Downloading: "{url}" to {cached_file}\n')
        download_url_to_file(url, cached_file, hash_prefix=None, progress=progress)
    return cached_file


# os.system("pip freeze")
ckpt_dir = Path('./ckpts')
if not ckpt_dir.exists():
	ckpt_dir.mkdir()

pretrain_model_url = {
	'vae': 'https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/ema_vae.pth',
	'dit': 'https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/seedvr2_ema_3b.pth',
    'pos_emb': 'https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/pos_emb.pt',
    'neg_emb': 'https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/neg_emb.pt',
    'apex': 'https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/apex-0.1-cp310-cp310-linux_x86_64.whl'
}
# download weights
if not os.path.exists('./ckpts/seedvr2_ema_3b.pth'):
	load_file_from_url(url=pretrain_model_url['dit'], model_dir='./ckpts/', progress=True, file_name=None)
if not os.path.exists('./ckpts/ema_vae.pth'):
	load_file_from_url(url=pretrain_model_url['vae'], model_dir='./ckpts/', progress=True, file_name=None)
if not os.path.exists('./pos_emb.pt'):
	load_file_from_url(url=pretrain_model_url['pos_emb'], model_dir='./', progress=True, file_name=None)
if not os.path.exists('./neg_emb.pt'):
	load_file_from_url(url=pretrain_model_url['neg_emb'], model_dir='./', progress=True, file_name=None)
if not os.path.exists('./apex-0.1-cp310-cp310-linux_x86_64.whl'):
	load_file_from_url(url=pretrain_model_url['apex'], model_dir='./', progress=True, file_name=None)

subprocess.run(shlex.split("pip install apex-0.1-cp310-cp310-linux_x86_64.whl"))
print(f"✅ setup completed Apex")

# download images
torch.hub.download_url_to_file(
	'https://huggingface.co/datasets/Iceclear/SeedVR_VideoDemos/resolve/main/seedvr_videos_crf23/aigc1k/23_1_lq.mp4',
	'01.mp4')
torch.hub.download_url_to_file(
	'https://huggingface.co/datasets/Iceclear/SeedVR_VideoDemos/resolve/main/seedvr_videos_crf23/aigc1k/28_1_lq.mp4',
	'02.mp4')
torch.hub.download_url_to_file(
	'https://huggingface.co/datasets/Iceclear/SeedVR_VideoDemos/resolve/main/seedvr_videos_crf23/aigc1k/2_1_lq.mp4',
	'03.mp4')

def configure_sequence_parallel(sp_size):
    if sp_size > 1:
        init_sequence_parallel(sp_size)

@spaces.GPU(duration=100)
def configure_runner(sp_size):
    config_path = os.path.join('./configs_3b', 'main.yaml')
    config = load_config(config_path)
    runner = VideoDiffusionInfer(config)
    OmegaConf.set_readonly(runner.config, False)
    
    init_torch(cudnn_benchmark=False, timeout=datetime.timedelta(seconds=3600))
    configure_sequence_parallel(sp_size)
    runner.configure_dit_model(device="cuda", checkpoint='./ckpts/seedvr2_ema_3b.pth')
    runner.configure_vae_model()
    # Set memory limit.
    if hasattr(runner.vae, "set_memory_limit"):
        runner.vae.set_memory_limit(**runner.config.vae.memory_limit)
    return runner

@spaces.GPU(duration=100)
def generation_step(runner, text_embeds_dict, cond_latents):
    def _move_to_cuda(x):
        return [i.to(torch.device("cuda")) for i in x]

    noises = [torch.randn_like(latent) for latent in cond_latents]
    aug_noises = [torch.randn_like(latent) for latent in cond_latents]
    print(f"Generating with noise shape: {noises[0].size()}.")
    noises, aug_noises, cond_latents = sync_data((noises, aug_noises, cond_latents), 0)
    noises, aug_noises, cond_latents = list(
        map(lambda x: _move_to_cuda(x), (noises, aug_noises, cond_latents))
    )
    cond_noise_scale = 0.1

    def _add_noise(x, aug_noise):
        t = (
            torch.tensor([1000.0], device=torch.device("cuda"))
            * cond_noise_scale
        )
        shape = torch.tensor(x.shape[1:], device=torch.device("cuda"))[None]
        t = runner.timestep_transform(t, shape)
        print(
            f"Timestep shifting from"
            f" {1000.0 * cond_noise_scale} to {t}."
        )
        x = runner.schedule.forward(x, aug_noise, t)
        return x

    conditions = [
        runner.get_condition(
            noise,
            task="sr",
            latent_blur=_add_noise(latent_blur, aug_noise),
        )
        for noise, aug_noise, latent_blur in zip(noises, aug_noises, cond_latents)
    ]

    with torch.no_grad(), torch.autocast("cuda", torch.bfloat16, enabled=True):
        video_tensors = runner.inference(
            noises=noises,
            conditions=conditions,
            dit_offload=False,
            **text_embeds_dict,
        )

    samples = [
        (
            rearrange(video[:, None], "c t h w -> t c h w")
            if video.ndim == 3
            else rearrange(video, "c t h w -> t c h w")
        )
        for video in video_tensors
    ]
    del video_tensors

    return samples

@spaces.GPU(duration=100)
def generation_loop(video_path='./test_videos', seed=666, fps_out=12, batch_size=1, cfg_scale=1.0, cfg_rescale=0.0, sample_steps=1, res_h=1280, res_w=720, sp_size=1):
    runner = configure_runner(1)

    def _extract_text_embeds():
        # Text encoder forward.
        positive_prompts_embeds = []
        for texts_pos in tqdm(original_videos_local):
            text_pos_embeds = torch.load('pos_emb.pt')
            text_neg_embeds = torch.load('neg_emb.pt')

            positive_prompts_embeds.append(
                {"texts_pos": [text_pos_embeds], "texts_neg": [text_neg_embeds]}
            )
        gc.collect()
        torch.cuda.empty_cache()
        return positive_prompts_embeds

    def cut_videos(videos, sp_size):
        if videos.size(1) > 121:
            videos = videos[:, :121]
        t = videos.size(1)
        if t <= 4 * sp_size:
            print(f"Cut input video size: {videos.size()}")
            padding = [videos[:, -1].unsqueeze(1)] * (4 * sp_size - t + 1)
            padding = torch.cat(padding, dim=1)
            videos = torch.cat([videos, padding], dim=1)
            return videos
        if (t - 1) % (4 * sp_size) == 0:
            return videos
        else:
            padding = [videos[:, -1].unsqueeze(1)] * (
                4 * sp_size - ((t - 1) % (4 * sp_size))
            )
            padding = torch.cat(padding, dim=1)
            videos = torch.cat([videos, padding], dim=1)
            assert (videos.size(1) - 1) % (4 * sp_size) == 0
            return videos

    # classifier-free guidance
    runner.config.diffusion.cfg.scale = cfg_scale
    runner.config.diffusion.cfg.rescale = cfg_rescale
    # sampling steps
    runner.config.diffusion.timesteps.sampling.steps = sample_steps
    runner.configure_diffusion()

    # set random seed
    seed = seed % (2**32) # avoid over range
    set_seed(seed, same_across_ranks=True)
    os.makedirs('output/', exist_ok=True)

    # get test prompts
    original_videos = [video_path.split('/')[-1]]

    # divide the prompts into different groups
    original_videos_group = original_videos
    # store prompt mapping
    original_videos_local = original_videos_group
    original_videos_local = partition_by_size(original_videos_local, batch_size)

    # pre-extract the text embeddings
    positive_prompts_embeds = _extract_text_embeds()

    video_transform = Compose(
        [
            NaResize(
                resolution=(
                    res_h * res_w
                )
                ** 0.5,
                mode="area",
                # Upsample image, model only trained for high res.
                downsample_only=False,
            ),
            Lambda(lambda x: torch.clamp(x, 0.0, 1.0)),
            DivisibleCrop((16, 16)),
            Normalize(0.5, 0.5),
            Rearrange("t c h w -> c t h w"),
        ]
    )

    # generation loop
    for videos, text_embeds in tqdm(zip(original_videos_local, positive_prompts_embeds)):
        # read condition latents
        cond_latents = []
        for video in videos:
            media_type, _ = mimetypes.guess_type(video_path)
            is_image = media_type and media_type.startswith("image")
            is_video = media_type and media_type.startswith("video")
            if is_video:
                video = (
                    read_video(
                       os.path.join(video_path), output_format="TCHW"
                    )[0]
                    / 255.0
                )
                if video.size(0) > 121:
                    video = video[:121]
                print(f"Read video size: {video.size()}")
                output_dir = 'output/' + str(uuid.uuid4()) + '.mp4'
            else:
                video_transform = Compose(
                    [
                        NaResize(
                            resolution=(
                                2560 * 1440
                            )
                            ** 0.5,
                            mode="area",
                            # Upsample image, model only trained for high res.
                            downsample_only=False,
                        ),
                        Lambda(lambda x: torch.clamp(x, 0.0, 1.0)),
                        DivisibleCrop((16, 16)),
                        Normalize(0.5, 0.5),
                        Rearrange("t c h w -> c t h w"),
                    ]
                )
                
                img = Image.open(video_path).convert("RGB")
                img_tensor = T.ToTensor()(img).unsqueeze(0)  # (1, C, H, W)
                video = img_tensor.permute(0, 1, 2, 3)  # (T=1, C, H, W)
                print(f"Read Image size: {video.size()}")
                output_dir = 'output/' + str(uuid.uuid4()) + '.png'
            cond_latents.append(video_transform(video.to(torch.device("cuda"))))

        ori_lengths = [video.size(1) for video in cond_latents]
        input_videos = cond_latents
        if is_video:
            cond_latents = [cut_videos(video, sp_size) for video in cond_latents]

        # runner.dit.to("cpu")
        print(f"Encoding videos: {list(map(lambda x: x.size(), cond_latents))}")
        # runner.vae.to(torch.device("cuda"))
        cond_latents = runner.vae_encode(cond_latents)
        # runner.vae.to("cpu")
        # runner.dit.to(torch.device("cuda"))

        for i, emb in enumerate(text_embeds["texts_pos"]):
            text_embeds["texts_pos"][i] = emb.to(torch.device("cuda"))
        for i, emb in enumerate(text_embeds["texts_neg"]):
            text_embeds["texts_neg"][i] = emb.to(torch.device("cuda"))

        samples = generation_step(runner, text_embeds, cond_latents=cond_latents)
        # runner.dit.to("cpu")
        del cond_latents

        # dump samples to the output directory
        for path, input, sample, ori_length in zip(
            videos, input_videos, samples, ori_lengths
        ):
            if ori_length < sample.shape[0]:
                sample = sample[:ori_length]
            # color fix
            input = (
                rearrange(input[:, None], "c t h w -> t c h w")
                if input.ndim == 3
                else rearrange(input, "c t h w -> t c h w")
            )
            if use_colorfix:
                sample = wavelet_reconstruction(
                    sample.to("cpu"), input[: sample.size(0)].to("cpu")
                )
            else:
                sample = sample.to("cpu")
            sample = (
                rearrange(sample[:, None], "t c h w -> t h w c")
                if sample.ndim == 3
                else rearrange(sample, "t c h w -> t h w c")
            )
            sample = sample.clip(-1, 1).mul_(0.5).add_(0.5).mul_(255).round()
            sample = sample.to(torch.uint8).numpy()

            if is_image:
                mediapy.write_image(output_dir, sample[0])
            else:
                mediapy.write_video(
                    output_dir, sample, fps=fps_out
                )

        # print(f"Generated video size: {sample.shape}")
        gc.collect()
        torch.cuda.empty_cache()
        if is_image:
            return output_dir, None, output_dir
        else:
            return None, output_dir, output_dir


with gr.Blocks(title="SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training") as demo:
    # Top logo and title
    gr.HTML("""
        <div style='text-align:center; margin-bottom: 10px;'>
            <img src='https://huggingface.co/ByteDance-Seed/SeedVR2-3B/resolve/main/assets/seedvr_logo.png' style='height:40px;' alt='SeedVR logo'/>
        </div>
        <p><b>Official Gradio demo</b> for 
        <a href='https://github.com/ByteDance-Seed/SeedVR' target='_blank'>
        <b>SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training</b></a>.<br>
        🔥 <b>SeedVR2</b> is a one-step image and video restoration algorithm for real-world and AIGC content.
        </p>
    """)

    # Interface
    with gr.Row():
        input_video = gr.File(label="Upload image or video", type="filepath")
        seed = gr.Number(label="Seeds", value=666)
        fps = gr.Number(label="fps", value=24)

    with gr.Row():
        output_video = gr.Video(label="Output_Video")
        output_image = gr.Image(label="Output_Image")
        download_link = gr.File(label="Download the output")

    run_button = gr.Button("Run")
    run_button.click(fn=generation_loop, inputs=[input_video, seed, fps], outputs=[output_image, output_video, download_link])

    # Examples
    gr.Examples(
        examples=[
            ["./01.mp4", 4, 24],
            ["./02.mp4", 4, 24],
            ["./03.mp4", 4, 24],
        ],
        inputs=[input_video, seed, fps]
    )

    # Article/Footer
    gr.HTML("""
        <hr>
        <p>If you find SeedVR helpful, please ⭐ the 
        <a href='https://github.com/ByteDance-Seed/SeedVR' target='_blank'>GitHub repository</a>:</p>

        <a href="https://github.com/ByteDance-Seed/SeedVR" target="_blank">
            <img src="https://img.shields.io/github/stars/ByteDance-Seed/SeedVR?style=social" alt="GitHub Stars">
        </a>

        <h4>Notice</h4>
        <p>This demo supports up to <b>720p and 121 frames for videos or 2k images</b>.  
        For other use cases (image restoration beyond 2K, video resolutions beyond 720p, etc), check the <a href='https://github.com/ByteDance-Seed/SeedVR' target='_blank'>GitHub repo</a>.</p>

        <h4>Limitations</h4>
        <p>May fail on heavy degradations or small-motion AIGC clips, causing oversharpening or poor restoration.</p>

        <h4>Citation</h4>
        <pre style="font-size: 12px;">
        @article{wang2025seedvr2,
            title={SeedVR2: One-Step Video Restoration via Diffusion Adversarial Post-Training},
            author={Wang, Jianyi and Lin, Shanchuan and Lin, Zhijie and Ren, Yuxi and Wei, Meng and Yue, Zongsheng and Zhou, Shangchen and Chen, Hao and Zhao, Yang and Yang, Ceyuan and Xiao, Xuefeng and Loy, Chen Change and Jiang, Lu},
            booktitle={arXiv preprint arXiv:2506.05301},
            year={2025}
        }

        @inproceedings{wang2025seedvr,
            title={SeedVR: Seeding Infinity in Diffusion Transformer Towards Generic Video Restoration},
            author={Wang, Jianyi and Lin, Zhijie and Wei, Meng and Zhao, Yang and Yang, Ceyuan and Loy, Chen Change and Jiang, Lu},
            booktitle={CVPR},
            year={2025}
        }
        </pre>

        <h4>License</h4>
        <p>Licensed under the 
        <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache 2.0 License</a>.</p>

        <h4>Contact</h4>
        <p>Email: <b>iceclearwjy@gmail.com</b></p>

        <p>
        <a href="https://twitter.com/Iceclearwjy">
        <img src="https://img.shields.io/twitter/follow/Iceclearwjy?label=%40Iceclearwjy&style=social" alt="Twitter Follow">
        </a>
        <a href="https://github.com/IceClear">
        <img src="https://img.shields.io/github/followers/IceClear?style=social" alt="GitHub Follow">
        </a>
        </p>

        <p style="text-align:center;">
        <img src="https://visitor-badge.laobi.icu/badge?page_id=ByteDance-Seed/SeedVR" alt="visitors">
        </p>
    """)

demo.queue()
demo.launch()
