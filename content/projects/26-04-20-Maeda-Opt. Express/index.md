---
title: "2次元分光放射計を用いたプロジェクタ色補償"
venue: "Optics Express 2026"
tags: [Projects, XR Displays]
date: 2026-04-20T00:00:00+09:00
paper_authors: "Yoshiaki Maeda and Daisuke Iwai"
links:
  - label: "Paper"
    url: "https://doi.org/10.1364/OE.596052"
  - label: "プロジェクトページ"
    url: "https://maedayoshiaki.github.io/projects/projector-radiometric-compensation/"
bibtex: |
  @article{maeda2026projector,
    author  = {Yoshiaki Maeda and Daisuke Iwai},
    title   = {Projector radiometric compensation using a 2D spectroradiometer},
    journal = {Optics Express},
    volume  = {34},
    number  = {9},
    pages   = {15979--15993},
    year    = {2026}
  }
---

### Abstract
プロジェクションマッピング（PM）は、コンピュータ生成画像を実世界の物体上に光学的に重畳することで、ユーザが表示デバイスを装着することなく拡張現実を体験できるようにする技術である。しかし、投影対象の表面テクスチャはしばしば色ずれを引き起こし、表示される色が所望の色からずれる原因となる。そこで本研究では、2D分光放射計（2DSR）を用いて、目標画像と投影結果との色差を最小化するプロジェクタ放射輝度補償手法を提案する。提案手法では、プロジェクタと2DSRの間の色変換を微分可能な形でモデル化する。この定式化に基づき、プロジェクタ色補償のための二つの最適化戦略を提案する。すなわち、（i）目標外観と投影結果とのスペクトル誤差の最小化、および（ii）人間の視覚知覚を反映するよう設計された微分可能な色空間において測定される色差の最小化、である。実機プロトタイプを用いた実験により、提案手法は、RGBカメラを用いる従来手法と比較して、より高精度なプロジェクタ色補償を実現し、人間の色知覚との整合性も高いことを示した。

*** 

{{< figure src="system_setup_revised.jpg" caption="実験セットアップ。プロジェクタ（EPSON EB-FH52）、2次元分光放射計（TOPCON SR-5100）、投影面（インクジェットで模様を印刷した紙）で構成。プロジェクタと投影面の距離は0.8 m" numbered="false" >}}

***

{{< figure src="ablation2_revised2.jpg" caption="各目的関数による投影結果の比較（アブレーション）。(a) 2DSRで撮影した投影結果をsRGB色空間に変換した可視化画像と、目標スペクトル画像に対する∆E76およびスペクトルMAEのヒートマップ。(b) 可視化画像中の矩形領域における平均スペクトルの比較。Ospe・Orgb・Olabおよびそれらの組み合わせを評価。" numbered="false" >}}

*** 

{{< figure src="convergence_plot.jpg" caption="提案する反復最適化の収束挙動。評価指標（スペクトルMAE・PSNR・∆E76）を反復回数の関数としてプロット。" numbered="false" >}}

*** 

{{< figure src="comparison2.jpg" caption="各手法による投影結果の比較。従来手法（Yoshidaら、CompenNeSt w/SL）と提案手法（Orgb+Olab、Ospe+Orgb+Olab）を比較。(a) 可視化画像と誤差ヒートマップ、(b) 平均スペクトルの比較。提案手法が目標スペクトルに最も近い形状を再現。" numbered="false" >}}

