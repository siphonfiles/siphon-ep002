# Space propriu: SeedVR2-3B pe video

- `upstream/` = copia Space-ului `Upsampler/seedvr2-3b` (Apache-2.0), adusă cu `space-fetch.yml`. Nu se modifică.
- `reference/` = app.py-ul Space-ului oficial `ByteDance-Seed/SeedVR2-3B`, doar ca referință pentru calea video.
- `overlay/` = ce înlocuim peste `upstream/`: `app.py` (video, un singur `@spaces.GPU`, durată dinamică ≤ 240 s), `README.md`, `requirements.txt`.
- Deploy: workflow-ul `space-deploy.yml` asamblează `upstream/` + `overlay/` și urcă în Space-ul privat `<cont>/siphon-seedvr2-video` (ZeroGPU). Nu apelează inferența.
- Apel: `seedvr2.yml` cu inputul `space` (implicit Space-ul propriu).
