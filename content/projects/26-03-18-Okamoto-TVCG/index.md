---
title: "合成開口プロジェクタによる影なしプロジェクションマッピング"
venue: "IEEE TVCG 2026"
tags: [Projects, XR Displays, XR Interaction]
date: 2026-03-18T00:00:00+09:00
paper_authors: "Takahiro Okamoto, Masaki Takeuchi, Masataka Sawayama, Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TVCG.2026.3679111"
  - label: "arXiv"
    url: "https://doi.org/10.48550/arXiv.2603.11551"
  - label: "プレスリリース"
    url: "https://resou.osaka-u.ac.jp/ja/research/2026/20260318_2"
  - label: "講演動画"
    url: "https://youtu.be/ue1W2vhWk38"
bibtex: |
  @article{okamoto2026shadowless,
    author  = {Takahiro Okamoto and Masaki Takeuchi and Masataka Sawayama and Daisuke Iwai},
    title   = {Shadowless Projection Mapping for Tabletop Workspaces with Synthetic Aperture Projector},
    journal = {IEEE Transactions on Visualization and Computer Graphics},
    note    = {Proceedings of 2026 IEEE Conference on Virtual Reality and 3D User Interfaces (VR)},
    year    = {2026}
  }
---

### Abstract
プロジェクションマッピングにおいてユーザーの手などが投影光を遮ると、影が生じて映像が見えなくなってしまいます。影問題の解決手法として、大型のフレネルレンズを用いて投影光を広い角度から集める大開口投影アプローチがあります。しかし大開口プロジェクタでは、レンズ収差や迷光などの影響で、投影画像に大きなボケが生じてしまいます。そこで本研究では、符号化開口と投影画像の事前鮮鋭化処理を順次最適化することで、投影ボケに対処します。まずフレネルレンズの表面形状を数理モデル化し、大開口プロジェクタの点像分布関数（PSF）の微分可能光学シミュレータを導入します。次に、シミュレートされたPSFに基づいた、符号化開口形状の最適化フレームワークを提案します。本研究ではPSFの広帯域フーリエスペクトル、光透過効率、影抑制性能という3つの損失関数を定義し，その線形結合を用いて符号化パターンを最適化します。最後に最適化されたマスクの下で、デコンボリューション処理によって投影画像を最適化します。シミュレーションと実機実験を通じて、上記の投影ボケ補償手法の有効性を検証しました。

***

{{< youtube DEDGYcM5H84 >}}

***

{{< figure src="setup.jpg" caption="天井設置の25台のプロジェクタ" numbered="false" >}}

***

{{< figure src="shadowless-demo.jpg" caption="一般的なプロジェクションマッピング (左) と影なしプロジェクションマッピング (右)" numbered="false" >}}

*** 

{{< figure src="results.jpg" caption="ユーザスタディで用いた刺激 (10枚の紙を配置し、そのうち7枚には異なる言語の文字を印刷、残り3枚には白紙に文字パターンを投影)" numbered="false" >}}

