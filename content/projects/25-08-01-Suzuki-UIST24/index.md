---
title: "EarHover：ヒアラブルデバイスにおける音漏れ信号を用いた空中ジェスチャ認識"
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
私たちは、ヒアラブルデバイス向けの空中ジェスチャ入力を可能にする革新的なシステム「EarHover」を提案します。空中ジェスチャ入力は、デバイスに触れる必要がないため、手やデバイスを清潔に保つことができます。しかし、これまでのヒアラブルデバイスにおける空中ジェスチャ入力は、カメラや赤外線センサを追加する手法に限られていました。
本研究では、ヒアラブルデバイス特有の「音漏れ」現象に着目し、スピーカと外部マイクロホンという、デバイスと高い親和性を持つ構成で、空中ジェスチャ認識を実現しました。音漏れによってデバイスの外部に漏れた信号は、外部マイクロホンで計測され、手の動きの速度や形状によって生じる反射特性の違いを検出できます。
評価実験では、27種類のジェスチャの中から、信号の識別性とユーザ受容性の観点から、EarHoverに適した7種類のジェスチャを選定しました。さらに、現実世界の応用シナリオを想定し、2種類のプロトタイプデバイス（耳内装着型／開放型）におけるジェスチャ検出と分類性能を網羅的に評価しました。

***

{{< youtube FvmiPpnCMA0 >}}

***

{{< figure src="認識アルゴリズム.jpg" caption="認識システム" numbered="false" >}}

