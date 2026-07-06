---
title: "EarHover: Mid-Air Gesture Recognition for Hearables Using Sound Leakage Signals"
venue: "ACM UIST 2024"
tags: [Projects, XR Interaction]
date: 2025-08-01T00:00:00+09:00
paper_authors: "Shunta Suzuki, Takashi Amesaka, Hiroki Watanabe, Buntarou Shizuki, and Yuta Sugiura"
links:
  - label: "Paper"
    url: "https://dl.acm.org/doi/10.1145/3654777.3676367"
bibtex: |
  @inproceedings{suzuki2024earhover,
    author    = {Shunta Suzuki and Takashi Amesaka and Hiroki Watanabe and Buntarou Shizuki and Yuta Sugiura},
    title     = {EarHover: Mid-Air Gesture Recognition for Hearables Using Sound Leakage Signals},
    booktitle = {Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology (UIST '24)},
    articleno = {129},
    pages     = {1--13},
    year      = {2024},
    publisher = {Association for Computing Machinery}
  }
---

### Abstract
We introduce EarHover, an innovative system that enables mid-air gesture input for hearables. Mid-air gesture input, which eliminates the need to touch the device and thus helps to keep hands and the device clean. However, existing mid-air gesture input methods for hearables have been limited to adding cameras or infrared sensors. By focusing on the sound leakage phenomenon unique to hearables, we have realized mid-air gesture recognition using a speaker and an external microphone that are highly compatible with hearables. The signal leaked to the outside of the device due to sound leakage can be measured by an external microphone, which detects the differences in reflection characteristics caused by the hand’s speed and shape during mid-air gestures. Among 27 types of gestures, we determined the seven suitable gestures for EarHover in terms of signal discrimination and user acceptability. We then evaluated the gesture detection and classification performance of two prototype devices (in-ear type/open-ear type) for real-world application scenarios.

***

{{< youtube FvmiPpnCMA0 >}}

***

{{< figure src="認識アルゴリズム.jpg" caption="Recognition system." numbered="false" >}}

