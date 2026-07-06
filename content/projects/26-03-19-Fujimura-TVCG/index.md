---
title: "ライトフィールド照明による高コントラストなプロジェクションマッピング"
venue: "IEEE TVCG 2026"
tags: [Projects, XR Displays]
date: 2026-03-19T00:00:00+09:00
paper_authors: "Kotaro Fujimura, Hiroki Kusuyama, Masaki Takeuchi, and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TVCG.2026.3679878"
  - label: "arXiv"
    url: "https://arxiv.org/abs/2603.11573"
  - label: "プレスリリース"
    url: "https://resou.osaka-u.ac.jp/ja/research/2026/20260319_2"
  - label: "講演動画"
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
プロジェクションマッピング（PM）は、物理的な物体表面に映像を投影し、特別なデバイスなしで複数のユーザーが拡張現実体験を共有できる技術です。しかし、高品質な投影を確保するためには暗い環境が必要であり、その実用化は「暗室の制約」によって制限されてきました。この制約を克服するため、本研究では、PMの投影対象を避けつつ周囲の環境を選択的に照らす新しい「ターゲット回避照明」手法を提案します。本システムは、LEDディスプレイと最適化された非周期レンズアレイを組み合わせることでライトフィールド照明を実現します。主な貢献は、一般的な照明と同等の自然なソフトシャドウを再現できる広い有効光源面積をコンパクトな構成で提供しつつ、投影対象を正確に回避するために必要な空間制御性を維持したことです。また、ターゲット回避照明時のクロストークに起因する意図しないダークスポットを抑制するための非周期レンズ配置の最適化手法に加え、ダイナミックPMに対応するリアルタイム手法を含む、3種類のLED輝度パターン算出手法を提案しました。プロトタイプシステムを用いた実験により、本アプローチが明るい環境下でも高コントラストなPMを実現することを示しました。

***

{{< youtube lILZRiP7yps >}}

***

{{< figure src="prototype.jpg" caption="プロトタイプ" numbered="false" >}}

*** 

{{< figure src="target-excluding-lighting-jp.jpg" caption="ターゲット回避照明" numbered="false" >}}

*** 

{{< figure src="optimized-lens-array.jpg" caption="ターゲット回避照明時の比較。従来の規則的なレンズ配列（左）で生じるターゲット周辺の意図しない暗所を、提案手法のレンズ配置最適化（右）で大幅に低減" numbered="false" >}}

***

{{< video src="comparison.mp4" >}}

