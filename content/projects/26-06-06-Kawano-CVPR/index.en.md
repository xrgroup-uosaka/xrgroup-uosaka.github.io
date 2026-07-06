---
title: "Breaking the Scalability Limit of Multi-Projector Calibration with Embedded Cameras"
venue: "IEEE CVPR 2026 (Oral)"
tags: [Projects, XR Displays]
date: 2026-06-06T00:00:00+09:00
paper_authors: "Takumi Kawano, Kohei Miura, Daisuke Iwai"
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2604.24024"
  - label: "Poster"
    url: "https://drive.google.com/file/d/1wrR82TFADZGZL3KIoy4IDUnL8eO6mBwL/view?usp=sharing"
  - label: "Supplementary video"
    url: "https://drive.google.com/file/d/1YZWZopKY_IIcBldOb_gzcNhCahP7WAFF/view?usp=drive_link"
  - label: "Code"
    url: "https://github.com/tk-flourish/embedded-camera-calibration"
bibtex: |
  @inproceedings{kawano2026breaking,
    author    = {Takumi Kawano and Kohei Miura and Daisuke Iwai},
    title     = {Breaking the Scalability Limit of Multi-Projector Calibration with Embedded Cameras},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    pages     = {21573--21582},
    year      = {2026}
  }
---

### Abstract
Conventional multi-projector calibration requires projecting and capturing structured light patterns for each projector sequentially, causing calibration time and effort to increase linearly with the number of projectors. This scalability bottleneck has long limited the deployment of large-scale projection mapping systems. We present a new calibration framework that breaks this limitation by embedding cameras into the surface of the calibration target. The embedded cameras directly capture the incoming projection light, enabling the separation of simultaneously projected structured light patterns from multiple projectors according to their incident directions. Our method establishes correspondences between the optical centers of the embedded cameras and the projector pixels, allowing the intrinsic and extrinsic parameters of all projectors to be simultaneously estimated. We further introduce a correction technique for small misalignments between the calibration board and camera optical centers. As a result, our system achieves calibration accuracy comparable to conventional methods while reducing the required number of projection-capture cycles from linear to nearly constant with respect to the number of projectors, dramatically improving scalability for dense multi-projector systems with overlapping projection regions, such as high-brightness stacking, super-resolution, light-field, and shadow-suppression displays.

*** 

{{< youtube raUvRT-TBTU >}}

***

{{< figure src="kawano-cvpr26-poster.jpg" caption="Poster ([full-res](https://drive.google.com/file/d/1wrR82TFADZGZL3KIoy4IDUnL8eO6mBwL/view?usp=sharing))" numbered="false" >}}

***

### Principle

When projector 1 fires, its red light hits the surface and scatters diffusely in all directions. The camera records a red pixel.
Add projector 2's blue light, and the two scatters mix into purple at the same camera pixel. We can't tell which color came from which projector — and that's why simultaneous projection fails.
{{< video src="kawano-cvpr26-1.mp4" >}}

Our idea is to turn the camera into the target itself.
We embed the camera into the board, with its optical center aligned with the board surface. The lens sits flush with the plane, and the image sensor goes behind it. So the camera is no longer observing the target — it is the target.
Now both rays still pass through the same point on the board but they continue to different pixels on the image sensor, determined by their incident angles.
This is the core idea of our method.
{{< video src="kawano-cvpr26-2.mp4" >}}

In practice, the optical center is never perfectly on the board surface. And critically, As the projector moves, crossing point slides along the surface. So the naive assumption that one camera equals one fixed point breaks down.
{{< video src="kawano-cvpr26-3.mp4" >}}

Our fix: we calibrate this offset once, offline. Place one projector at $K$ different positions, and for each position record the pair $c$ and $k$.
Both clusters are related by a projective transformation — we fit it as a homography, $M_n$. This is done once per embedded camera, and only once.
{{< video src="kawano-cvpr26-4.mp4" >}}

When a new projector emits light during actual calibration, the embedded camera records a sensor pixel $c$. We push it through $M_n$ to recover the true board-surface coordinate $x$, and use this as world coordinate of a target. 
{{< video src="kawano-cvpr26-5.mp4" >}}

*** 

### Experimental setup

{{< figure src="kawano-cvpr26-system.jpg" caption="Prototype projector calibration board. A black acrylic board with four embedded cameras mounted through openings in the board." numbered="false" >}}

*** 

### Results

#### Experiment with Gray-code Projection Using 25 Projectors
{{< figure src="kawano-cvpr26-res1.jpg" caption="(Top) Gray-code projection for calibration: the conventional sequential approach projects Gray-code patterns from one projector at a time (left; the arrow indicates the projector currently projecting the Gray-code pattern), whereas the proposed method projects Gray-code patterns simultaneously from all 25 projectors (right). (Bottom) Alignment result after calibration, where the same image content is projected from all 25 projectors." numbered="false" >}}

#### Experiment with Line-shift Projection Using 3 Projectors
{{< video src="kawano-cvpr26-res3.mp4" caption="The proposed method supports both Gray-code and line-shift projections for high-accuracy homography estimation. Finally, the same checkerboard pattern was simultaneously projected from all three projectors, confirming accurate alignment among the three projections." >}}

#### Experiment evaluating robustness to ambient light with two projectors outdoors
{{< figure src="kawano-cvpr26-res2.jpg" caption="This experiment simulates bright-condition calibration, which is useful for scenarios such as completing calibration during the daytime before a nighttime projection-mapping event. (Top) Experimental setup under direct sunlight, showing the calibration board during simultaneous Gray-code projection. Although the projected patterns are washed out and not visible to the naked eye on the board, the image captured by one embedded camera is shown. At this instant, Projector 2 projects a white stripe onto the camera while Projector 1 projects a black stripe; consequently, only Projector 2 and the sun appear as bright spots in the camera image. (Bottom) Alignment result captured with direct sunlight blocked, where the same half-scale checkerboard pattern is simultaneously projected from the two projectors after homography-based alignment estimated with the proposed method." numbered="false" >}}

