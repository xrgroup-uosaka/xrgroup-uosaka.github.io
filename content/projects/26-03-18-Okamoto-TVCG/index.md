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
プロジェクションマッピング（PM）は、ヘッドマウントディスプレイを装着することなく拡張現実（AR）体験を提供でき、複数ユーザでの同時利用にも対応します。卓上作業空間において拡張対象に重畳したコンテンツと対話する多様な応用—遠隔協調、ヘルスケア、工業デザイン、都市計画、アート制作、オフィスワークなど—に有望な技術と考えられています。しかし従来のPMでは、ユーザが投影光路を遮ると投影影が生じるという問題がありました。複数の分散配置プロジェクタを用いる従来手法は遮蔽を補償できますが、計算処理に伴う遅延が生じ、ユーザ体験を損ないます。本研究では、環境中に高密度に配置した多数のプロジェクタを用いる合成開口PMシステムを提案し、計算補償を必要とせずに、卓上作業空間に対して遅延のない影なし投影を実現します。重畳投影間のサブピクセルのずれに起因する空間解像度の劣化に対しては、計算時間がプロジェクタ台数に依存しないオフラインのボケ補償手法を開発し、その有効性を検証します。さらに、この影なしPMが、投影しているという印象を与えずに素材の見えを変えるというPM本来の目標の達成に重要な役割を果たすことを示します。具体的には、この知覚的印象を「投影感（sense of projection: SoP）」と定義し、ユーザスタディに基づいてSoPを最小化するPM設計フレームワークを確立します。

***

{{< youtube DEDGYcM5H84 >}}

***

{{< figure src="setup.jpg" caption="天井設置の25台のプロジェクタ" numbered="false" >}}

***

{{< figure src="shadowless-demo.jpg" caption="一般的なプロジェクションマッピング (左) と影なしプロジェクションマッピング (右)" numbered="false" >}}

*** 

{{< figure src="results.jpg" caption="ユーザスタディで用いた刺激 (10枚の紙を配置し、そのうち7枚には異なる言語の文字を印刷、残り3枚には白紙に文字パターンを投影)" numbered="false" >}}

