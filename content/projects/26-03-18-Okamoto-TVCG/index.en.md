---
title: "Shadowless Projection Mapping for Tabletop Workspaces with Synthetic Aperture Projector"
venue: "IEEE TVCG 2026"
tags: [Projects, XR Displays, XR Interaction]
date: 2026-03-18T00:00:00+09:00
paper_authors: "Takahiro Okamoto, Masaki Takeuchi, Masataka Sawayama, Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TVCG.2026.3679111"
  - label: "arXiv"
    url: "https://doi.org/10.48550/arXiv.2603.11551"
  - label: "Press release"
    url: "https://resou.osaka-u.ac.jp/en/research/20260318_2"
  - label: "Talk video"
    url: "https://youtu.be/ue1W2vhWk38"
bibtex: |
  @article{okamoto2026shadowless,
    author  = {Takahiro Okamoto and Masaki Takeuchi and Masataka Sawayama and Daisuke Iwai},
    title   = {Shadowless Projection Mapping for Tabletop Workspaces with Synthetic Aperture Projector},
    journal = {IEEE Transactions on Visualization and Computer Graphics},
    note    = {Proceedings of 2026 IEEE Conference on Virtual Reality and 3D User Interfaces (VR)},
    year    = {2026}
  }
---

### Abstract
Projection mapping (PM) enables augmented reality (AR) experiences without requiring users to wear head-mounted displays and supports multi-user interaction. It is regarded as a promising technology for a variety of applications in which users interact with content superimposed onto augmented objects in tabletop workspaces, including remote collaboration, healthcare, industrial design, urban planning, artwork creation, and office work. However, conventional PM systems often suffer from projection shadows when users occlude the light path. Prior approaches employing multiple distributed projectors can compensate for occlusion, but suffer from latency due to computational processing, degrading the user experience. In this research, we introduce a synthetic-aperture PM system that uses a significantly larger number of projectors, arranged densely in the environment, to achieve delay-free, shadowless projection for tabletop workspaces without requiring computational compensation. To address spatial resolution degradation caused by subpixel misalignment among overlaid projections, we develop and validate an offline blur compensation method whose computation time remains independent of the number of projectors. Furthermore, we demonstrate that our shadowless PM plays a critical role in achieving a fundamental goal of PM: altering material properties without evoking projection-like impression. Specifically, we define this perceptual impression as “sense of projection (SoP)” and establish a PM design framework to minimize the SoP based on user studies.

***

{{< youtube DEDGYcM5H84 >}}

***

{{< figure src="setup.jpg" caption="Experimental setup." numbered="false" >}}

***

{{< figure src="shadowless-demo.jpg" caption="(left) Standard projection mapping and (right) the proposed shadowless projection mapping." numbered="false" >}}

*** 

{{< figure src="results.jpg" caption="Stimuli used in the user study. Ten sheets of paper were placed on the tabletop surface: seven had printed text in various languages, and the remaining three were blank with projected text patterns instead." numbered="false" >}}

