---
title: "High-Contrast Projection Mapping under Light Field Illumination with LED Display and Aperiodic Lens Array"
venue: "IEEE TVCG 2026"
tags: [Projects, XR Displays]
date: 2026-03-19T00:00:00+09:00
paper_authors: "Kotaro Fujimura, Hiroki Kusuyama, Masaki Takeuchi, and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TVCG.2026.3679878"
  - label: "arXiv"
    url: "https://arxiv.org/abs/2603.11573"
  - label: "Press release"
    url: "https://resou.osaka-u.ac.jp/en/research/20260319_2"
  - label: "Talk video"
    url: "https://youtu.be/CyRxHD-HI1A"
bibtex: |
  @article{fujimura2026high,
    author  = {Kotaro Fujimura and Hiroki Kusuyama and Masaki Takeuchi and Daisuke Iwai},
    title   = {High-Contrast Projection Mapping under Light Field Illumination with LED Display and Aperiodic Lens Array},
    journal = {IEEE Transactions on Visualization and Computer Graphics},
    note    = {Proceedings of 2026 IEEE Conference on Virtual Reality and 3D User Interfaces (VR)},
    year    = {2026}
  }
---

### Abstract
Projection Mapping (PM) is a technology that projects images onto the surfaces of physical objects, allowing multiple users to share an augmented reality experience without special devices. However, its practical use has been constrained by the need for dark environments to ensure high-quality projection. To overcome this "dark-room constraint," we propose a novel target-excluding lighting method that selectively illuminates the surrounding environment while avoiding the PM target. Our system achieves light-field illumination by combining an LED display panel with an optimized aperiodic lens array. The key contributions include a compact form factor that provides a large effective light source area, reproducing natural soft shadows comparable to typical lighting, while maintaining the spatial controllability needed to precisely avoid the target. We also introduce a computational technique for optimizing aperiodic lens placement to suppress undesired dark spots caused by crosstalk under target-excluding lighting, and three efficient methods for computing LED luminance patterns, including one that enables dynamic PM. Experiments with a prototype system demonstrate that our approach achieves high-contrast PM even in bright environments.

***

{{< youtube lILZRiP7yps >}}

***

{{< figure src="prototype.jpg" caption="Prototype" numbered="false" >}}

*** 

{{< figure src="target-excluding-lighting-en.jpg" caption="Target-excluding lighting" numbered="false" >}}

*** 

{{< figure src="optimized-lens-array.jpg" caption="Comparison under target-excluding lighting. Unintended dark spots caused by a conventional periodic lens arrangement (left), and their significant mitigation through the proposed optimized lens placement (right)." numbered="false" >}}

*** 

{{< video src="comparison.mp4" >}}

