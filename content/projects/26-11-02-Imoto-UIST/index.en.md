---
title: "AeroPixels: Repurposing Ubiquitous Displays as Imperceptible Schlieren Light Sources for Airflow Interaction"
venue: "ACM UIST 2026"
tags: [Projects, XR Displays, Computational Imaging, XR Interaction]
date: 2026-11-02T00:00:00+09:00
teaser_height: 340
paper_authors: "Yusuke Imoto, Takashi Amesaka, Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1145/3830398.3830604"
  - label: "Video"
    url: "https://www.youtube.com/watch?v=ceCwP54D7yg"
bibtex: |
  @inproceedings{imoto2026aeropixels,
    author    = {Yusuke Imoto and Takashi Amesaka and Daisuke Iwai},
    title     = {AeroPixels: Repurposing Ubiquitous Displays as Imperceptible Schlieren Light Sources for Airflow Interaction},
    booktitle = {Proceedings of the ACM Symposium on User Interface Software and Technology (UIST)},
    articleno = {90},
    pages     = {1--12},
    year      = {2026},
    doi       = {10.1145/3830398.3830604}
  }
---

### Abstract
Airflow is an invisible yet ubiquitous phenomenon in everyday environments, encoding rich information about human activities and environmental conditions such as exhalation, thermal convection, and ventilation. We present AeroPixels, a method that leverages ubiquitous display surfaces as an airflow sensing infrastructure. AeroPixels embeds the source grid pattern required for focusing schlieren imaging, an optical technique that visualizes airflow through light refraction, into displayed visual content and perceptually hides it via alternating complementary, high-frame-rate frames, allowing users to perceive only the intended imagery. A schlieren camera synchronized with the display refresh captures each complementary frame independently and reconstructs airflow information. We address key challenges in display-based sensing, including geometric misalignment between the embedded source grid pattern and the sensing camera, as well as content-dependent noise, enabling robust schlieren imaging under non-ideal conditions such as projection mapping environments. We build a prototype system and demonstrate stable airflow visualization on projected surfaces while preserving the intended visual content for human observers. Finally, we present three representative projection modes for human-computer interaction enabled by AeroPixels, including exhalation visualization, breath-based input, education, and entertainment.

***

{{< youtube ceCwP54D7yg >}}

***

{{< figure src="imoto-uist26-fig1.jpg" caption="Overview of AeroPixels and example applications. (a) Prototype system. (b) Visualization of a dense gas released from a tilted beaker (top to bottom). (c) Breath-based hands-free control for advancing projected instructions (each pair progresses left to right)." numbered="false" >}}

***

### Principle

Focusing schlieren (FS) imaging combines a source grid and a cutoff grid to capture the refraction of light caused by air density gradients as image contrast. Conventional FS, however, requires a high-contrast grid to be shown directly on the display or projected surface, which is unsuitable for everyday environments.

AeroPixels embeds the source grid and its inverse into the displayed content and alternates them at 120 Hz. Users perceive only the average, that is, the original content, while a display-synchronized camera captures the positive and negative frames to extract airflow. Visual presentation and airflow sensing run in parallel on the same surface.

{{< figure src="imoto-uist26-fig2.jpg" caption="Overview of the AeroPixels system." numbered="false" >}}

***

### Applications

AeroPixels uses the projected surface both as a display and as an airflow sensor. We present three projection modes.

#### Real Projection

Measured airflow is projected at its actual position and shape. We prototyped visualization of exhaled breath in conversation and an educational demonstration of density-driven flow.

{{< figure src="imoto-uist26-fig9.jpg" caption="Real projection. (a) Visualization of exhaled airflow in conversation. (b) Convective flow from pouring warm water over cold water. Sequences progress left to right." numbered="false" >}}

#### Awareness Projection

Airflow is presented as an ambient display that blends into the environment, conveying ventilation conditions and safety risks such as an unattended soldering iron.

{{< figure src="imoto-uist26-fig10.jpg" caption="Awareness projection. (a) Ambient visualization of ventilation. (b) Warning for unattended equipment. Sequences progress left to right." numbered="false" >}}

#### Interactive Projection

Measured airflow serves as contactless input. We prototyped a system where a user with both hands occupied while soldering advances projected instructions by blowing, and an interaction for painting with air from an air duster.

{{< figure src="imoto-uist26-fig11.jpg" caption="Interactive projection. (a) Drawing, (b) exploring airflow effects, (c) emotional expression. Sequences progress left to right." numbered="false" >}}
