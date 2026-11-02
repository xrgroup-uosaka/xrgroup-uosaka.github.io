---
title: "AeroPixels：身近なディスプレイをシュリーレン光源として活用する気流インタラクション"
venue: "ACM UIST 2026"
tags: [Projects, XR Displays, Computational Imaging, XR Interaction]
date: 2026-11-02T00:00:00+09:00
teaser_height: 340
paper_authors: "Yusuke Imoto, Takashi Amesaka, Daisuke Iwai"
links:
  - label: "論文"
    url: "https://doi.org/10.1145/3830398.3830604"
  - label: "動画"
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
空気の流れ（気流）は目に見えませんが、日常のあらゆる環境に存在し、呼気、熱対流、換気など、人の活動や環境の状態に関する豊富な情報を含んでいます。本研究では、身近なディスプレイ面を気流センシングの基盤として活用する手法 AeroPixels を提案します。
AeroPixels は、光の屈折によって気流を可視化する光学技術である焦点シュリーレン法に必要な光源格子パターンを、表示するコンテンツに埋め込み、相補的なパターンを高フレームレートで交互に表示することで知覚的に隠します。これにより、ユーザには本来の映像だけが見えます。ディスプレイのリフレッシュに同期したシュリーレンカメラが各相補フレームを独立に撮影し、気流の情報を再構成します。
埋め込んだ光源格子パターンとセンシングカメラとの幾何学的なずれや、コンテンツに依存するノイズといった、ディスプレイを用いたセンシングの課題にも対処し、プロジェクションマッピング環境のような理想的でない条件でも、安定したシュリーレン撮像を可能にしました。試作システムを構築し、人が見る本来の映像を保ったまま、投影面上で安定した気流の可視化ができることを示しました。最後に、AeroPixels によって実現できる、呼気の可視化、呼気による入力、教育・エンターテインメントを含む、ヒューマンコンピュータインタラクションのための3つの代表的な投影モードを紹介します。

***

{{< youtube ceCwP54D7yg >}}

***

{{< figure src="imoto-uist26-fig1.jpg" caption="AeroPixels の概要と応用例：(a) 試作システム, (b) 傾けたビーカーから放出した高密度ガスの可視化 (上から下へ時間順), (c) 呼気によるハンズフリーでの投影手順の送り (各ペアは左から右へ時間順)" numbered="false" >}}

***

### Principle

焦点シュリーレン法（FS）は、光源格子とカットオフ格子を組み合わせ、空気の密度勾配による光の屈折をコントラストとして撮影する手法です。ただし従来の FS は、高コントラストな格子を表示面にそのまま見せる必要があり、日常環境では使えませんでした。

AeroPixels は、光源格子とその反転パターンを映像に加減算して埋め込み、120 Hz で交互に表示します。人の目には平均、つまり元の映像だけが見え、表示に同期したカメラは正負それぞれのフレームから気流を取り出せます。映像の提示と気流のセンシングを、同じ表示面で並行して行えます。

{{< figure src="imoto-uist26-fig2.jpg" caption="AeroPixels システムの概要" numbered="false" >}}

***

### Applications

投影面を、映像の表示媒体と気流のセンシング基盤の両方に使い、3つの投影モードを示しました。

#### 直接可視化

計測した気流を、実際の位置や形に合わせて投影します。会話中の呼気の拡散や、密度差による流れの教育デモを試作しました。

{{< figure src="imoto-uist26-fig9.jpg" caption="直接可視化：(a) 会話中の呼気の可視化, (b) 冷水に温水を注いだときの対流 (いずれも左から右へ時間が進んでいる)" numbered="false" >}}

#### アウェアネス投影

気流を、環境に溶け込むアンビエントディスプレイとして提示します。換気の状態や、はんだごての放置といった安全上のリスクを伝えます。

{{< figure src="imoto-uist26-fig10.jpg" caption="アウェアネス投影：(a) 換気状態の可視化, (b) 放置された機器への警告 (いずれも左から右へ時間が進んでいる)" numbered="false" >}}

#### インタラクティブ投影

計測した気流を入力に使い、非接触で投影内容を変えます。両手がふさがるはんだ付け中に息を吹きかけて作業手順を進めるシステムや、エアダスターで空間に絵を描くインタラクションを試作しました。

{{< figure src="imoto-uist26-fig11.jpg" caption="インタラクティブ投影：(a) 描画, (b) 気流効果の探索, (c) 感情表現 (いずれも左から右へ時間が進んでいる)" numbered="false" >}}
