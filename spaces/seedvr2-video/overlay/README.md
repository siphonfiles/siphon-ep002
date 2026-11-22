---
title: Siphon SeedVR2 Video
emoji: 🎞️
colorFrom: gray
colorTo: yellow
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
license: apache-2.0
short_description: SeedVR2-3B one-step video restoration (private)
models:
  - ByteDance-Seed/SeedVR2-3B
---

Private Space for Siphon Files. SeedVR2-3B (ByteDance, Apache-2.0) video restoration,
built on the fixed image port Upsampler/seedvr2-3b (Apache-2.0) plus the video path of
the official ByteDance-Seed/SeedVR2-3B Space. Max 121 frames per request; one GPU
allocation per request with a duration estimated from frame count and working area.
