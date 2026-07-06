---
title: "符号化開口と拡散モデルを融合した三次元イメージング"
venue: "IEEE Trans. Computational Imaging 2026"
tags: [Projects, Computational Imaging]
date: 2026-05-28T00:00:00+09:00
paper_authors: "H. Kawachi, J. R. C. S. A. V. S. Neto, Y. Yagi, H. Nagahara and T. Nakamura"
links:
  - label: "Paper"
    url: "https://doi.org/10.1109/TCI.2026.3697618"
  - label: "プレスリリース"
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
本研究では、レンズ内に配置した特殊なマスク（符号化開口）が写し出す、距離ごとに異なるボケの模様を手がかりに、撮影された1枚の写真から、被写体までの距離情報とピントの合った画像を物理法則に基づいて同時に復元する新たな手法を開発しました。ピントが合っていない部分に生じる「ボケ」には距離の情報が含まれていますが、ボケから距離と画像を同時に復元するには手がかりが足りず、答えが一つに定まりません。従来は、人間が経験的に作ったルールを手がかりにする方法や、大量のデータで答えを学習する深層学習の方法が用いられてきましたが、高い精度の実現が困難である点や、撮影条件が変わると性能が落ちる点が課題でした。そこで本研究では、撮影の物理法則に沿って、観測されたボケ画像と矛盾しない答えを探す枠組みを構築しました。通常の方法では答えを絞り切れないため、補助情報として、「拡散モデル」と呼ばれるAI技術が学習した「自然な画像らしさ」の知識を利用しています。AIは撮影条件に依存しない汎用的な補助情報としてのみ働くため、カメラやノイズの条件が変わっても安定した復元が可能です。シミュレーション実験と試作カメラによる実験の両方で有効性を確認しました。本成果は、LiDARなどの専用センサに比べて小型・低コストな装置の実現や、さらなる精度向上と適用範囲の拡大が期待されます。

*** 

{{< figure src="figure1.jpg" caption="研究成果の概要。符号化開口を用いて撮影した1枚のぼけ画像から、撮影の物理法則に基づいて被写体の距離と全焦点画像を同時に復元する。拡散モデルを事前知識として活用することで高い精度を達成。" numbered="false" >}}

***

{{< figure src="figure2.jpg" caption="技術の概要。再構成アルゴリズムは、観測画像と矛盾しない被写体距離・画像情報を最適化により探索する。この最適化問題は不良設定問題と呼ばれ、観測データと矛盾しない解が多数存在するため、答えを一つに絞ることが困難である。この問題を解決するために、本研究では、符号化開口が実現する距離情報の強力な特徴づけと、拡散モデルが持つ自然画像に関する強力な事前知識を援用する。" numbered="false" >}}

