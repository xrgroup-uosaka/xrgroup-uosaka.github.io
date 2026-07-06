---
title: "拡散零空間モデルの知識蒸留による高速・物理忠実・高品質レンズレスイメージング"
venue: "IEEE ICCP 2026"
tags: [Projects, Computational Imaging]
date: 2026-06-19T00:00:00+09:00
paper_authors: "J. R. C. S. A. V. S. Neto, H. Kawachi, Y. Yagi, and T. Nakamura"
links:
  - label: "arXiv"
    url: "https://arxiv.org/abs/2511.12024"
  - label: "コード"
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
　レンズレスイメージングは符号化光学系と画像再構成処理の組み合わせにより小型撮像系を実現する情報光学技術です。レンズレスイメージングの画像再構成処理は多数の光情報の重畳を解く悪条件逆問題であるため、アルゴリズム設計の工夫がその成否を分ける鍵となります。古典的な逆解析手法は復元画像の品質に限界があり、近年の深層学習型手法は物理モデルに対する解の忠実性に課題がありました。これらの課題を解決するため、近年、拡散零空間モデル（逆解析で復元できない画像成分に限定して生成による情報補完を行う拡散モデル）を用いることで物理忠実性と高品質を同時実現する技術が提案されていますが、生成のために反復処理を必要とするため、速度に課題がありました。<br>
　本研究では、拡散零空間モデルにおいて、零空間成分の生成系に知識蒸留を行うことで、非反復で物理忠実かつ高品質なレンズレス画像再構成を実現する技術（NSDD: Null-Space Diffusion Distillation）を提案しています。数値実験により、NSDDが従来手法では不可能であった高速・物理忠実・高品質の三項目を同時達成できることを定量的に示しました。また、光学実験により、実環境下でも提案手法が有効であることを実証しました。さらに、NSDDが学習データの分布から外れた対象物に対しても良好に動作する汎化性能を有することを実験的に実証しました。加えて、知識蒸留の対象を零空間生成系に限定することが、単純な蒸留に比べて高い効果をもたらすことも確認しました。<br>
　本成果は、レンズレスイメージングの速さ・正しさ・画質の全てを同時に実現するとともに、実環境下での高い汎化性能も備えることから、レンズレスカメラの実用化に向けた重要な基盤技術となり得ます。

<!-- *** 

{{< figure src="figure1.jpg" caption="研究成果の概要。符号化開口を用いて撮影した1枚のぼけ画像から、撮影の物理法則に基づいて被写体の距離と全焦点画像を同時に復元する。拡散モデルを事前知識として活用することで高い精度を達成。" numbered="false" >}}

***

{{< figure src="figure2.jpg" caption="技術の概要。再構成アルゴリズムは、観測画像と矛盾しない被写体距離・画像情報を最適化により探索する。この最適化問題は不良設定問題と呼ばれ、観測データと矛盾しない解が多数存在するため、答えを一つに絞ることが困難である。この問題を解決するために、本研究では、符号化開口が実現する距離情報の強力な特徴づけと、拡散モデルが持つ自然画像に関する強力な事前知識を援用する。" numbered="false" >}}

***  -->
