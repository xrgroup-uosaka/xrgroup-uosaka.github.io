---
title: "Fast, Physically Faithful, and High-Quality Lensless Imaging via Knowledge Distillation of Denoising Diffusion Null-Space Model"
venue: "IEEE ICCP 2026"
tags: [Projects, Computational Imaging]
date: 2026-06-19T00:00:00+09:00
paper_authors: "J. R. C. S. A. V. S. Neto, H. Kawachi, Y. Yagi, and T. Nakamura"
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2511.12024"
  - label: "Code"
    url: "https://github.com/JRCSAVSN/NullSpaceDiffusionDistillation"
bibtex: |
  @inproceedings{silvaneto2026nullspace,
    author    = {Jos\'e Reinaldo Cunha Santos A. V. Silva Neto and Hodaka Kawachi and Yasushi Yagi and Tomoya Nakamura},
    title     = {Null-Space Diffusion Distillation Unlocks Speed, Fidelity and Realism in Lensless Imaging},
    booktitle = {IEEE International Conference on Computational Photography (ICCP)},
    year      = {2026}
  }
---

### Abstract
   Lensless imaging is a computational optics technology that achieves compact imaging systems by combining coded optics with image reconstruction. Since the reconstruction involves solving an ill-conditioned inverse problem of disentangling superimposed optical information, algorithm design is critical. Classical methods are limited in reconstruction quality, while deep-learning approaches lack fidelity to the physical model. Recently, diffusion null-space models—which restrict generative completion to image components unrecoverable by inverse analysis—have achieved both physical fidelity and high quality, but remain slow due to iterative sampling.<br>
   We propose Null-Space Diffusion Distillation (NSDD), which distills the null-space generator into a single forward pass, enabling non-iterative, physically faithful, high-quality reconstruction. Numerical experiments quantitatively showed that NSDD uniquely achieves speed, physical fidelity, and perceptual quality simultaneously. Optical experiments confirmed its effectiveness in real-world settings, including strong generalization to out-of-distribution objects. We also verify that restricting distillation to the null-space generator yields substantially better performance than naïve full-image distillation. These results position NSDD as a key enabling technology toward practical lensless cameras.
<!-- *** 

{{< figure src="figure1.jpg" caption="研究成果の概要。符号化開口を用いて撮影した1枚のぼけ画像から、撮影の物理法則に基づいて被写体の距離と全焦点画像を同時に復元する。拡散モデルを事前知識として活用することで高い精度を達成。" numbered="false" >}}

***

{{< figure src="figure2.jpg" caption="技術の概要。再構成アルゴリズムは、観測画像と矛盾しない被写体距離・画像情報を最適化により探索する。この最適化問題は不良設定問題と呼ばれ、観測データと矛盾しない解が多数存在するため、答えを一つに絞ることが困難である。この問題を解決するために、本研究では、符号化開口が実現する距離情報の強力な特徴づけと、拡散モデルが持つ自然画像に関する強力な事前知識を援用する。" numbered="false" >}}

***  -->
