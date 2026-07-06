---
title: "Shadowless projector using large-aperture Fresnel lens"
venue: "Optics Express 2026"
tags: [Projects, XR Displays, Computational Imaging]
date: 2026-02-25T00:00:00+09:00
paper_authors: "Hiroki Kusuyama, Tomoya Nakamura, and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1364/OE.587813"
  - label: "Project"
    url: "https://hirokikusuyama.studio.site/3#coded_la"
bibtex: |
  @article{kusuyama2026shadowless,
    author  = {Hiroki Kusuyama and Tomoya Nakamura and Daisuke Iwai},
    title   = {Shadowless projector using large-aperture Fresnel lens},
    journal = {Optics Express},
    volume  = {34},
    number  = {5},
    pages   = {7791--7808},
    year    = {2026}
  }
---

### Abstract
In interactive projection mapping (PM) application, when the users' bodies occlude projection lights, the projected imagery becomes  invisible due to cast shadows. One approach to shadowless PM is to use a large-aperture (LA) projector that focuses projection light from a wide viewing angle with a large-format Fresnel lens. However, LA projectors often suffer from significant blur in projected images due to lens aberrations and stray light etc. In this study, we address the blur by sequentially optimizing the coded aperture and the pre-sharpening process of the projection images. First, we mathematically model the surface profile of the Fresnel lens and introduce an optical simulator for the point spread function (PSF) of the LA projector using differentiable ray tracing. Next, we propose the optimization framework for the coded aperture pattern based on the simulated PSF. The coded aperture is optimized under a linear combination of three loss functions: the broadband Fourier spectrum of the PSF, light transmission efficiency, and shadow suppression performance. Additionally, we optimize the projection image using a conventional deconvolution process under the optimized mask. Finally, we validate the effectiveness of the proposed deblurring method through simulation and actual experiments.
<br>

***

{{< figure src="nofeatured.jpg" caption="Aperture optimization using our differentiable PSF simulator and shadowless PM with our actual setup" numbered="false" >}}

***

{{< figure src="setup.jpg" caption="Experimental setup" numbered="false" >}}

*** 

{{< figure src="PSFs_and_MTFs.jpg" caption="Simulated PSFs (Point Spread Function) and MTFs (Modulation Transfer Function) in different mask aperture condition" numbered="false" >}}

*** 

<figure style="width: 100%; margin: 0;">
  {{< video src="Visualization_1.mp4" >}}
  <figcaption style="text-align: center; margin-top: 8px;">
    Comparison of projected results between with and without our coded aperture
  </figcaption>
</figure>

