---
title: "符号化大開口フレネルレンズを用いた影なしプロジェクタ"
venue: "Optics Express 2026"
tags: [Projects, XR Displays, Computational Imaging]
date: 2026-02-25T00:00:00+09:00
paper_authors: "Hiroki Kusuyama, Tomoya Nakamura, and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1364/OE.587813"
  - label: "プロジェクトページ"
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
プロジェクションマッピングにおいてユーザーの手などが投影光を遮ると、影が生じて映像が見えなくなってしまいます。影問題の解決手法として、大型のフレネルレンズを用いて投影光を広い角度から集める大開口投影アプローチがあります。しかし大開口プロジェクタでは、レンズ収差や迷光などの影響で、投影画像に大きなボケが生じてしまいます。そこで本研究では、符号化開口と投影画像の事前鮮鋭化処理を順次最適化することで、投影ボケに対処します。まずフレネルレンズの表面形状を数理モデル化し、大開口プロジェクタの点像分布関数（PSF）の微分可能光学シミュレータを導入します。次に、シミュレートされたPSFに基づいた、符号化開口形状の最適化フレームワークを提案します。本研究ではPSFの広帯域フーリエスペクトル、光透過効率、影抑制性能という3つの損失関数を定義し，その線形結合を用いて符号化パターンを最適化します。最後に最適化されたマスクの下で、デコンボリューション処理によって投影画像を最適化します。シミュレーションと実機実験を通じて、上記の投影ボケ補償手法の有効性を検証しました。

***

{{< figure src="nofeatured.jpg" caption="微分可能PSFシミュレータを用いた開口最適化および実機セットアップを用いた影なしプロジェクションマッピング" numbered="false" >}}

***

{{< figure src="setup.jpg" caption="実験セットアップ" numbered="false" >}}

*** 

{{< figure src="PSFs_and_MTFs.jpg" caption="異なる開口条件におけるシミュレートPSF (Point Spread Function) とMTF (Modulation Transfer Function) の比較" numbered="false" >}}

*** 

<figure style="width: 100%; margin: 0;">
  {{< video src="Visualization_1.mp4" >}}
  <figcaption style="text-align: center; margin-top: 8px;">
    符号化開口の有無による投影結果の比較
  </figcaption>
</figure>

