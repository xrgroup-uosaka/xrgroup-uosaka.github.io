---
title: "Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling"
venue: "IEEE Trans. Computational Imaging 2026"
tags: [Projects, Computational Imaging]
date: 2026-05-28T00:00:00+09:00
paper_authors: "H. Kawachi, J. R. C. S. A. V. S. Neto, Y. Yagi, H. Nagahara and T. Nakamura"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TCI.2026.3697618"
  - label: "Press release"
    url: "https://resou.osaka-u.ac.jp/ja/research/2026/20260609_2"
bibtex: |
  @article{kawachi2026single,
    author  = {Hodaka Kawachi and Jos\'e Reinaldo Cunha Santos A. V. Silva Neto and Yasushi Yagi and Hajime Nagahara and Tomoya Nakamura},
    title   = {Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling},
    journal = {IEEE Transactions on Computational Imaging},
    volume  = {12},
    pages   = {1034--1045},
    year    = {2026},
    doi     = {10.1109/TCI.2026.3697618}
  }
---

### Abstract
In this study, we developed a method that recovers both the distance to the subject and an in-focus image from a single photograph, using the depth-dependent blur patterns produced by a special mask (a coded aperture) placed inside the lens. Blur in out-of-focus regions contains distance information, but blur alone is insufficient to uniquely determine both the distance and the image. Conventional approaches, based on hand-crafted rules or deep learning from large datasets, have struggled to achieve high accuracy and degrade when imaging conditions change. We instead built a framework that searches for solutions consistent with the observed image under the physical laws of image formation, using the knowledge of natural image appearance learned by a diffusion model as auxiliary information. Because this AI prior is independent of the imaging conditions, reconstruction remains stable even when the camera or noise conditions change. We validated the method in both simulations and experiments with a prototype camera. These results are expected to lead to devices smaller and cheaper than dedicated sensors such as LiDAR, with further gains in accuracy and applicability.

*** 

{{< figure src="figure1.jpg" caption="Summary of research results: A method that simultaneously recovers the scene depth and an all-in-focus image from a single blurred image captured with a coded aperture, based on the physical laws of image formation. High accuracy is achieved by leveraging a diffusion model as prior knowledge" numbered="false" >}}

***

{{< figure src="figure2.jpg" caption="Overview of the technology: The reconstruction algorithm uses optimization to find the subject distance and image consistent with the observed data. This problem is ill-posed, with many consistent solutions, making it hard to identify a unique answer. Our method resolves this by combining the strong depth encoding of the coded aperture with the strong natural-image prior of the diffusion model." numbered="false" >}}

