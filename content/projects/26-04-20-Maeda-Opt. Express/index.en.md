---
title: "Projector radiometric compensation using a 2D spectroradiometer"
venue: "Optics Express 2026"
tags: [Projects, XR Displays]
date: 2026-04-20T00:00:00+09:00
paper_authors: "Yoshiaki Maeda and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1364/OE.596052"
  - label: "Project"
    url: "https://maedayoshiaki.github.io/projects/projector-radiometric-compensation/"
bibtex: |
  @article{maeda2026projector,
    author  = {Yoshiaki Maeda and Daisuke Iwai},
    title   = {Projector radiometric compensation using a 2D spectroradiometer},
    journal = {Optics Express},
    volume  = {34},
    number  = {9},
    pages   = {15979--15993},
    year    = {2026}
  }
---

### Abstract
Projection mapping (PM) optically overlays computer-generated imagery onto realworld
objects, enabling users to experience augmented reality without wearing any display devices.
However, surface textures often cause color distortion, leading the displayed colors to deviate
from the desired colors. To address this issue, we propose a projector radiometric compensation
method that minimizes the color difference between a target image and the projected result using
a 2D spectroradiometer (2DSR). In the proposed method, we model the color transformation
between the projector and the 2DSR in a differentiable manner. Based on this formulation, we
propose two optimization strategies for projector radiometric compensation: (i) minimizing
the spectral error between the target appearance and the projected result, and (ii) minimizing
the color difference measured in a differentiable color space designed to reflect human visual
perception. Experiments with a physical prototype demonstrate that our method achieves more
accurate projector radiometric compensation and better alignment with human color perception
than conventional methods using an RGB camera.

*** 

{{< figure src="system_setup_revised.jpg" caption="Experimental setup, consisting of a projector (EPSON EB-FH52), a 2D spectroradiometer (TOPCON SR-5100), and the projection surface (paper with inkjet-printed patterns). The projector-to-surface distance was 0.8 m." numbered="false" >}}

***

{{< figure src="ablation2_revised2.jpg" caption="Comparison of projection results across objective functions (ablation study). (a) sRGB-converted visualization images of 2DSR-captured projections, with ∆E76 and spectral-MAE heatmaps relative to the target spectral image. (b) Mean-spectra comparison within the marked rectangular region. Evaluates Ospe, Orgb, Olab and all their combinations." numbered="false" >}}

*** 

{{< figure src="convergence_plot.jpg" caption="Convergence behavior of the proposed iterative optimization, with evaluation metrics (spectral MAE, PSNR, ∆E76) plotted as a function of the iteration number." numbered="false" >}}

*** 

{{< figure src="comparison2.jpg" caption="Comparison of projection results across methods, contrasting the baselines (Yoshida et al., CompenNeSt w/SL) with the proposed method (Orgb+Olab, Ospe+Orgb+Olab). (a) visualization images and error heatmaps, (b) mean-spectra comparison. The proposed method most closely reproduces the target spectral shape." numbered="false" >}}

