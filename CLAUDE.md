# CLAUDE.md — xrlab-website-new（大阪大学 岩井研究室 公式サイト）

Hugo 製の研究室サイト。**このファイルは Claude Code に前提知識を渡すためのもの**（人向け README は置かない）。`~/.claude/` の memory は使わず、知識はすべてここに集約する。

## 概要

- 公開 URL: **https://www.xr.sys.es.osaka-u.ac.jp/**（GitHub Pages、リポジトリ `xrgroup-uosaka/xrgroup-uosaka.github.io`、`static/CNAME` で独自ドメイン）
- 旧サイトは `diwai.github.io` 上の Blox（Wowchemy）製。2026-07 に本リポジトリ（plain Hugo、テーマ無し）へ移行
- 2言語：**和文がデフォルトで `/`、英文は `/en/`**（`defaultContentLanguageInSubdir: false`）。翻訳はファイル名方式：`index.md`＝和文、`index.en.md`＝英文（同一フォルダで画像を共有）
- Hugo は **extended v0.145.0**（ローカル brew も CI も同じ）。`.Site.LastChange` は v0.123 で削除済みなので使わない（`site.Lastmod`）
- 人材育成（`/teaching/`）は**和文のみ**。英文メニューには出さない

## ビルドとデプロイ

- ローカル: `hugo --gc --minify`。プレビューは `.claude/launch.json` の `hugo`（`hugo server -D --port 1315`）
- デプロイ: `main` に push → `.github/workflows/gh-pages.yml` → GitHub Pages（Source は「GitHub Actions」）
- `public/`・`resources/`・`.claude/` は gitignore 済み。このファイルは公開物には入らない（Hugo はリポジトリ直下の .md を出力しない）
- **ハマりどころ**
  - テンプレートエラーを直しても `hugo server` がエラー画面のまま固まることがある → サーバーを停止して起動し直す
  - `.band { padding-inline: 0 }` が後方にあり、同じ詳細度の指定を上書きする。帯の内側余白を変えるときは `.band.band-msg` のように詳細度を上げる
  - zsh では `status` が読み取り専用変数。シェルスクリプトで変数名に使わない
  - `/en`（末尾スラッシュ無し）→ `/en/` の 301 は正常動作。GSC で「リダイレクト」と出ても問題ではない
  - サイトマップは `sitemap.xml`（インデックス）→ `/ja/sitemap.xml`・`/en/sitemap.xml`。ルートに送信すれば両方読まれる

## 唯一の情報源（テンプレートを触らずデータで更新する）

- **研究業績** `content/publications/_index.md`・`_index.en.md` … **Google Apps Script が自動コミット**する（コミット名 `Update japanese/english publications - <日時>`）。元データはスプレッドシート側。**手で編集しない**（次回の自動コミットで上書きされる）
- **メンバー** `content/authors/<slug>/_index.md`（＋`_index.en.md`、`avatar.jpg`）
  - `last_name: 1_岩井` の数字接頭辞で表示順を制御
  - `user_groups` の値は `content/team/_index.md` の `groups` と**文字列一致**させる（一致しないと表示されない）。卒業生は `content/alumni/_index.md` の `groups` に合わせる
  - `content/member_register.py` は Blox 時代の GUI 登録ツール（`ja/`・`en/` ディレクトリ前提で現構成では動かない）。**content/ 配下にあるため公開サイトの `/member_register.py` として配信されている**（既知・未対応）
- **プロジェクト** `content/projects/YY-MM-DD-Author-Venue/`（`index.md`・`index.en.md`・`featured.jpg`）
  - front matter: `title` `venue` `tags` `date` `paper_authors` `links:[{label,url}]` `bibtex`
  - `tags` には必ず `Projects` ＋ 研究領域（`XR Displays` / `Computational Imaging` / `XR Interaction` のいずれか）。一覧のフィルタはこの3領域固定（`layouts/projects/list.html`）で、クライアント側 JS で切替
  - 本文は `### Abstract` → `***` 区切り → `{{< youtube >}}` / `{{< figure >}}` / `{{< video src= caption= >}}`
  - 和文アブストは英文の翻訳であること（過去に別論文の要旨が入っていた事故あり）
- **お知らせ** `content/post/YY-MM-DD-Slug/`（`index.md`・`index.en.md`・`featured.jpg`）。`<!--more-->` より上が一覧の抜粋。和文の見出しは「お知らせ」（News ではない）
  - front matter の `date` は **`T00:00:00+09:00`（JST）で統一**する（10/23 に `+08:00` が 16 記事 × 和英の 32 ファイルに混入していたのを修正済み）。**同じ日付の記事の並びは秒で制御**する（例: `T00:00:01+09:00` のほうが新しい扱いで先に並ぶ）。サイトマップ・RSS の `lastmod`/日付はこの値から作られる（`enableGitInfo: false`）。記事を追加しても、`date` が出来事の日付のままだとサイトマップの更新日は増えない点に注意（GSC でサイトマップの再送信が必要な場合がある）
- **トップ** `content/_index.md`・`_index.en.md`
  - front matter `slides` がヒーロー画像（`assets/media/homepage/*.jpg`）
  - 本文は `## メッセージ` → `## お知らせ`（`{{< news count="5" >}}`）→ `<div class="contact-cols" id="contact">` 内に `### お問い合わせ` と右列（`### 人材育成` を上、`### 沿革` を下）
- **沿革** `content/history/_index.md` の `items:[{title,date_start,description}]`
- **メニュー** `config/_default/menus.ja.yaml`・`menus.yaml`（`params.icon` でアイコン名）。**サイト設定** `config/_default/hugo.yaml`・`languages.yaml`・`params.yaml`。**UI 文言** `i18n/ja.yaml`・`en.yaml`

## レイアウトの決まりごと

- 本文幅は **960px**（`.pgallery-wrap` `.band-inner` `.proj-section-inner` `.band-head` `.project-head-wrap`）。プロジェクト一覧は `minmax(210px,1fr)` で 4 枚横並び
- 背景帯: `layouts/partials/banded.html` が本文を `<h2>` 単位で白／グレー交互の全幅帯に分ける。トップの最初の帯だけ `firstClass: band-msg`（角丸カード＋影、画面端から `--pad` だけ内側。吹き出しの尻尾は付けない）
- ヒーロー: 画像は暗くしない（オーバーレイ 0%）。文字は多段 `text-shadow` の光彩で可読性を確保。`.hero-text` は `clamp(.85rem, 1.6vw, 1rem)`
- ナビ: ホバー／アクティブで `::after` の下線が `scaleX` で伸びる。メニューアイコンは `grid` `people` `file-text` `at`
- アイコン: `layouts/partials/icon-svg.html` の `$paths`（塗り＝Bootstrap Icons、線＝Tabler 風は `<g fill="none" stroke="currentColor">` で包む）と `$vb`（アイコン別 viewBox。切り詰めて見かけの大きさを調整）。本文では `{{< icon name="…" >}}`
- スクロール出現: `baseof.html` の IntersectionObserver。初期表示域より下の `.band` `.pcard` `.news-item` `.tl-item` にだけ `.reveal` を付ける（初期表示でちらつかせない）。`prefers-reduced-motion` で無効化
- カード影は控えめ（`.pcard` `.tl-card` `.news-item` `.person-photo`）。**帯の青色背景は不採用**（試して戻した）
- プロジェクトページのボタン `.project-btn` は灰色背景 `#eef0f3`
- `head.html`: `rel=canonical`・hreflang・OGP・**GSC の `google-site-verification` メタタグ（直書き）**。**ブラウザ言語による JS 自動転送は廃止済み**（復活させない）
- `layouts/robots.txt`: 全許可＋ `Sitemap:`。フッターの © 年は `site.Lastmod.Year`（コンテンツ最終更新年）
- 既知の未対応: `i18n` に `licensedUnder` キーが無く、フッターのライセンス表記に前置きが出ない

## セキュリティ・インシデント（2026-07）

- 旧リポジトリから独自ドメインを外し新リポジトリで確保するまでの空白時間に、第三者が GitHub Pages で `www.xr.sys.es.osaka-u.ac.jp` を自分のリポジトリに紐付け（dangling CNAME によるサブドメイン乗っ取り）。約2日間、アダルトスパム数千ページが配信された
- 奪還: GitHub の**ドメイン所有権検証**（DNS TXT `_github-pages-challenge-xrgroup-uosaka`）。検証するのは `www.` ではなくルートの `xr.sys.es.osaka-u.ac.jp`。検証が通ると攻撃者側の紐付けが強制解除される
- 復旧時の注意: GitHub の Trust & Safety 対応で被害側アカウントも一時 404 になった。Pages はフラグ解除後も自動復旧しないので **Actions を手動再実行**する
- DNS: セカンダリ `sys-gw2` がシリアル遅延していた。`rndc reload` はローカルのゾーンファイル再読込、`rndc retransfer` はプライマリから再転送（後者が必要だった）。SOA の negative-cache TTL は 86400
- 提出済み: 大学 情報推進部への報告書、CSIRT への回答（GitHub Pages 利用の妥当性）、GitHub 通報（サポート番号 #4540141、攻撃者リポジトリのテイクダウン要請）
- **要確認の残件**: 過去に平文 PAT が git remote URL と Apps Script ファイルに埋め込まれていた。remote からは除去済みだが **GitHub 側での失効が済んでいるか未確認**。トークン文字列は絶対に出力・転記しない。GitHub Education の再申請も未完
- **企業・大学ファイアウォールの URL カテゴリ誤分類（10/16 判明）**: 他大学の先生から、本学ではなく先方大学のファイアウォール（Palo Alto）で本サイトがブロックされていたと連絡。乗っ取り時のスパムによる誤分類とみられる（推測）。Palo Alto 側の変更要求は https://urlfiltering.paloaltonetworks.com/ から**ドメイン管理者が申請**（審査に時間がかかる）。**10/16 に Palo Alto の公式検索で確認したところ、現在のカテゴリは Educational-Institutions／Low-Risk で正常**（変更要求は不要）。先方でのブロックは先方側のキャッシュか、当時の一時的な分類による可能性があるが原因は不明。他ベンダーも 10/16 に確認し**すべて正常**（Fortinet: Education、格付け履歴は 2019 年のまま／Cisco Talos: Education・Web Reputation Favorable・ブロックリスト無し／Symantec WebPulse: Education／Zscaler Zulu: Benign 5/100）。どのベンダーにも変更要求は不要。先方ブロックの原因はグローバルな分類ではなく先方側の設定やキャッシュとみられる（推測）
  - **続報（10/16 以降）**: 先方に問い合わせた結果、ブロックの原因は URL フィルタリング（カテゴリ）ではなく **「DNS セキュリティ」** だった。理由の記載は無く、詳細は不明。→ 上の各ベンダー確認は URL カテゴリ／レピュテーションであり **DNS セキュリティの判定は見ていない**ので、「どこも正常」とは言い切れない。乗っ取り（dangling DNS）の履歴が DNS レベルで記録されている可能性があるが推測。先方は設定変更で閲覧可能にしてもらった（根本の判定が解除されたかは未確認）。先方情報センターに、ログ上のカテゴリ名・ブロック日時を確認してもらうのが次の一手
- 再発防止: ドメインの付け替えは「新リポジトリで確保 → 旧から外す」の順。空白時間を作らない

## SEO / Google Search Console（2026-08〜09）

### 経緯と現状
- 復旧後、GSC 上は登録済みなのに **検索結果に一切出ない**状態が約2か月続いた。技術要因（robots・noindex・canonical・削除ツール・手動対策・セキュリティ問題・セーフサーチ）はすべて確認済みで該当なし → ホスト単位のアルゴリズム抑制と判断
- 実施済み: 所有権確認（HTML タグ）、サイトマップ送信、8 つのスパムパス（`/tag/ /bkm/ /ypd/ /bio/ /ouy/ /nbn/ /tak/ /kgf/`）のプレフィックス削除申請、canonical、robots.txt、JS 言語転送の廃止、**全 177 ページの URL 検査→インデックス送信を 9/16 に一巡完了**（1日 10〜12 件が上限）
- 登録済みページ数の推移（正規／スパム）: 8/14 110／117 → 9/4 137／33 → **9/15 170／21**（残り 5 件は旧ページネーション等の残骸）。送信したページは当日クロール・2〜3 日で登録される
- **表示回数（検索パフォーマンス）**: 8/13〜9/12 は正規ページ 0 回 → **9/13 `/en/`（米国、クリック 1）、9/14 `/`（日本）、9/16 `/en/`（米国）で単発の表示**。9/17 時点では「抑制が解け始めた」と判断したが、**10/9 の再確認で 9/17〜10/6 は 0 回**（過去3か月の正規ページの表示は計 3 回のみ）→ 回復ではなく散発的な漏れと判断を修正。クエリは匿名化で空。なお 8/13 の 2 回はスパム URL（`/kgf/video/…`、ベトナム）とみられる（推測）
- **10/16 の再確認（データは 10/13 まで）**: 約 3 週間の 0 のあと **10/10 に 1 回・10/11 に 1 回・10/12 に 2 回（平均順位 5）、10/13 は 0**。いずれも `/`（和文トップ）で、日本 3・イタリア 1、モバイル中心。**初めて検索クエリが出た**: 「大阪大学 岩井研究室」（順位 3）「阪大 岩井研究室」（順位 7）。ただし**ユーザーが同じクエリで手元検索（10/16 以降）しても出てこなかった**ので、研究室名での表示も安定しておらず、一時的／断続的とみる。母数が 4 回と小さく、回復とは断定できない。tokoma noshi 氏のエスカレーション（9/30）との因果は不明。**ユーザーの見立て（有力）**: イタリアの学会に参加しており、そこで会った日本の研究者が、サイト訪問履歴のあるモバイルで研究室名を検索しただけ（パーソナライズ）の可能性が高い。履歴のない検索者への表示改善とは別物とみて、10/23 頃にブランド名以外のクエリでの表示が出るかで判断する
- 9/15〜16 送信分で登録未確認の 7 件: `/en/post/25-04-01-takes-flight/` `25-04-08-inaugural-members/` `25-04-18-zollmann-langlotz-visit/` `25-05-23-distinguished-professor/` `25-05-23-welcome-race/` `25-08-08-open-campus/` `25-09-25-sommart-graduation/`
- 相談スレッド（日本語コミュニティ）: https://support.google.com/webmasters/thread/462445673?hl=ja — 回答者 Wang Huaimin、tokoma noshi（プラチナ）、takano（プラチナ）。「クリーンに保って待つ」が共通見解
- 9/24 時点: インデックス登録 175／177（正規）まで進行、表示回数は 9/15〜9/21 の7日間で合計1回のみとほぼ変わらず → 同日、tokoma noshi 氏へエスカレーションを依頼
- **9/30、tokoma noshi 氏がエスカレーションを引き受ける旨を返信**（「エスカレーションしても明確な回答や解消案が出るとは限らない」と留保つき）。お礼を返信済み。
- **10/15 頃、ユーザーが tokoma 氏へ状況確認の追記を投稿 → 10/16 頃に tokoma 氏が返信**: 「エスカレーションは上げているが、まだ Google から連絡はない」「何かあればこちら（スレッド）で連絡する」。**結果待ちの状態（10/18 時点）**。こちらから催促する必要はなく、tokoma 氏の連絡を待つ
- 10/9 時点: 登録は総数 205（スパム 21、旧ページネーション残骸 9 を含む正規 184）。サイトマップ 177 件中 175 件登録で 9/22 以降横ばい。未登録は `/en/post/25-09-25-sommart-graduation/` と `/post/26-03-12-ieice-gc/`
- 10/16 時点: 総数 204（スパム 20、旧ページネーション残骸 9 を含む正規 184）。正規は 175／177 のまま。未登録は `/en/post/25-09-25-sommart-graduation/`（長期未登録）と `/en/post/25-04-01-takes-flight/`（今回抜けた）。`/post/26-03-12-ieice-gc/` は 10/9 のクロールで復帰。スパムは `bkm` の 1 件が index から消えて 21→20

- **10/23 時点**: 登録は 10/16 から**完全に横ばい**（総数 204、スパム 20、旧ページネーション残骸 9、チャートは 10/10 以降 204 のまま。データは 10/16 まで）。10/18 のコミットで**お知らせ 6 本（6/29 yomiuri、8/7 ieee-spectrum、8/19 kyushu-trip、9/6 vrsjac、9/14 ipg-autumn、9/14 ipg-award）が和英で追加**され、**サイトマップが 177→189 件（ja 95／en 94）**に増加。新規 12 件は公開済み（HTTP 200）だが未登録（公開から 5 日で未クロール、異常ではない）。未登録は計 14 件＝新規 12 ＋ `/en/post/25-04-01-takes-flight/`・`/en/post/25-09-25-sommart-graduation/`。既存の正規 175 件は変動なし

- **スパム 20 件の実態（10/23、ユーザーが URL 検査で 1 件確認）**: `/bio/video/SEXVIDEOSXXX-…2925868.html` は URL 検査で「**URL が Google に登録されていません（クロール済み - インデックス未登録）**」、前回のクロール 7/7、取得「成功」は当時の記録。つまり「登録済み」レポートに載っていても**URL 検査では index にない**。**ユーザーが残りも確認し、20 件すべて「登録されていません」と出た**。理由は不明で、(a) レポートの反映遅れ、(b) 以前から（7/7 のクロール時点から）未登録だった、(c) 削除申請（一時非表示）の影響で検査の表示が変わる、などが考えられるが切り分けられない。**いずれにせよ「登録済み」レポートのスパム件数は実態を表していない可能性があり、スパム件数の増減を回復の指標にしない**。**このため「インデックス登録をリクエスト」は押さない**（404 の URL に押しても意味がなく、スパム URL の index 登録を依頼する形になるため）。削除申請（プレフィックス）の期限（約 6 か月）前の再申請だけ忘れない

- **10/23 の検索パフォーマンス（データは 10/20 まで）**: 10/14 に 3 回（クリック 1、順位 2）、10/15 に 1 回、10/16 に 4 回（クリック 1、順位 4.2）、**10/17〜10/20 は 0 回**。**この 8 回・クリック 2 は、ユーザーが Google の AI モードで検索して表示されたものを複数回クリックした自作自演とみられる**（すべて日本、PC 中心、`/` に集中）→ **自然流入としては数えない**。クエリは「大阪大学 岩井研究室」計 4 回（順位 4）、「阪大 岩井研究室」計 2 回（順位 7）。累計は正規ページ 15 回・クリック 3 回だが、自作自演を除く自然な表示は 9/13〜9/16 と 10/10〜10/12 の計 7 回のみ。**自然な回復の兆候は無し**。教訓: ユーザー自身の検索・クリックは GSC に混ざるので、検索テストをした日付を控えておく。AI モードの引用ではブランド名検索で本サイトがリンクされることがある（通常の順位付けとは別の仕組みの可能性、推測）

- **トップページの URL 検査（10/23、ユーザーが実施）**: 「URL は Google に登録されています」。前回のクロール **10/22 14:04（スマホ用 Googlebot、取得成功）**、サイトマップ経由で検出。**参照元ページ**は 3 件: ① `alphaxiv.org/zh/abs/2604.24024`（外部の論文サイト）、② **`/nbn/video/XXXokxxx-…-0442865-….html`（乗っ取り時のスパムページ。現在 404）**、③ **`https://www.es.osaka-u.ac.jp/ja/department/laboratory/`（大学の研究室一覧）**。②は Google が保持しているスパムページの旧コピーが、トップへのリンク（ホームへ戻るリンク等）を含んでいるための名残で、再クロールで消えるまで残る（推測）。②の URL は「登録済み」レポートの 20 件に無く、**Google が把握しているスパム URL は 20 件より多い**。③から、**大学内リンクは検査画面上では認識されている**（GSC リンクレポートに出ないのはレポート側の問題とみられる。上の「osaka-u.ac.jp が 1 件も出ない」の見立ては修正）

- **「ページがインデックスに登録されなかった理由」（10/23、ユーザーのスクリーンショット）**: 404 **4,251**（検証:開始前。スパム URL とみられる）／クロール済み・未登録 **220**（Google システム）／リダイレクト 3（検証:失敗）／代替ページ canonical 2／5xx 1／noindex 1／重複・正規に選ばれず 1。サイト側の確認: **`/ja/` は Hugo が生成する転送ページ**（`meta refresh`→`/`、`noindex`、canonical は `/`）で、`noindex` 1 件と `リダイレクト` の一部はこれと、`http→https` の 301・`/en`→`/en/` の 301 とみられる（いずれも意図通り、要対応なし）。テンプレートに `aliases` や独自の `noindex` は無い。**220 件の内訳（10/23 のエクスポートで確認）**: スパムの動画 URL **212 件**（`/tag/` 50・`/ypd/` 44・`/bkm/` 39・`/tak/` 32・`/bio/` 21・`/nbn/` 20・`/ouy/` 6。**すべて最終クロールが 7/6〜7/7 のまま、3 か月半一度も再クロールされていない**）＋ 旧サイト由来の RSS `index.xml` 5 件と旧 Blox の `/publication_types/` ＋ **正規ページは英文記事 2 件のみ**（`/en/post/25-04-01-takes-flight/`・`/en/post/25-09-25-sommart-graduation/`、いずれも 9/15〜16 にクロールされたが index されず。本文が 1 文＋画像だけの薄い記事。ただし同程度に薄い `inaugural-members` は登録済みなので、薄さが決定要因かは不明）。**Google がクロールして登録を見送った正規ページは 189 件中この 2 件だけ**。**5xx 1 件・重複 1 件・noindex 1 件の実 URL は、ユーザー確認の結果すべてスパム URL（`/tag/video/…`・`/bkm/video/…`、現在 404）で、サイトの正規ページではない**。上記「noindex は `/ja/` とみられる」は誤りで、`/ja/` は Google の記録上この分類に入っていない（`/ja/` 自体は Hugo 生成の転送ページで問題なし）。**サイト側で直すべき項目は無い**

- **サイトマップ（10/23）**: `/sitemap.xml`（索引）は 8/15 送信・10/21 読み込み・成功・**検出 183**（189 のうち 6 件足りず＝片方の言語が未再読込と推測）→ 10/23 に `ja/sitemap.xml`・`en/sitemap.xml` を個別送信 → **ja 95・en 94 と全件検出、読み込み 10/23・成功**（新規 12 件を Google が認識）。索引の 183 は集計の更新待ちとみられる。コミット `7403ba9`「日付情報修正」（date の `+08:00`→`+09:00`）はデプロイ済み

- **10/27 時点（チャートは 10/23 まで）**: 総数 **206**（スパム動画 URL **19**＋旧 Blox の `/tag/publications/` 1、旧ページネーション残骸 9 を含む正規 186。**以降スパムは「`/…/video/…`」だけを数える**。従来の「20」は `/tag/publications/` を含む数え方だった）。チャートは 10/17 に 204→206。**サイトマップ 189 件のうち登録済み 177 件**（10/16 の 175 から +2）。**新規登録**: `kyushu-trip` の和英（10/18 追加記事。10/19 にクロールされ登録）と `/en/post/25-04-01-takes-flight/`（10/18 にクロール。9/16 に一度「登録見送り」だったページが再クロールで登録された）。**抜けた**: `/post/26-05-10-kobe-animal-kingdom/`（和文。英文は登録済み）。**未登録 12 件**＝新規 5 本の和英 10 件（yomiuri・ieee-spectrum・vrsjac・ipg-autumn・ipg-award）＋ `/en/post/25-09-25-sommart-graduation/` ＋ `/post/26-05-10-kobe-animal-kingdom/`。直近のクロール日は 10/24（`/projects/26-05-28-nakamura-ieee/`）まで進んでいる。スパム 20 件は同一で変化なし（指標にしない）

### 判断基準と次の一手
- 回復判定は **検索パフォーマンスの表示回数**で行う（`site:` 検索は網羅性が無く、出なくても登録されていない証拠にはならない）
- エスカレーション待ちの間も、表示回数は定期的に再確認する（増えていれば自然回復、動きが無ければエスカレーションの返答待ち）
- **10/16 時点の方針**: 10/10〜12 の表示は履歴による漏れの可能性が高く（上記）、**ユーザーの手元検索（履歴なし）でも出ず、`site:xr.sys.es.osaka-u.ac.jp` は 0 件のまま**＝抑制は解けていないとみる。**ホスト名変更は行わない（ユーザーの確定方針、10/16）**。待ちとエスカレーション結果、被リンクなどホスト名を変えない施策で対応する。次回（10/23 頃）は表示回数の増加とブランド名以外のクエリを確認
- 切り分け結果（ユーザーが実施、10/16）: `site:es.osaka-u.ac.jp` と `site:sys.es.osaka-u.ac.jp` はいずれも結果が出る → 親ドメインは正常で、抑制は **`xr.sys.es.osaka-u.ac.jp` ホスト単位**とみられる（推測）
- （廃案・参考）かつての案: 10 月上旬になっても表示が無ければ、ホスト名変更（例 `xrlab.sys.es.osaka-u.ac.jp`）を検討。その場合 **旧ホストから 301 しない**（抑制を引き継がないため）。ただしエスカレーション結果が出ていればそちらを優先して判断
- 被リンクの状況（ユーザー確認、10/16）: `diwai.github.io` から本サイトへ設置済み。大学の `es.osaka-u.ac.jp`／`sys.es.osaka-u.ac.jp` 等からも設置済みとのこと。researchmap は本サイトではなく `diwai.github.io` へリンクしており、**変更しない（確定）**
- **GSC「上位のリンク元サイト」（10/16、24 サイト）**: github.io 9ページ、amesaka.me／complightlab.com／kaanaksit.com／cvl.osaka／daisukeiwai.org（共同研究者・個人サイト）、arxiv.org／ieee.org／computer.org、x.com／bsky.app、paperverse.io、asiaresearchnews.com 等が認識されている。**`osaka-u.ac.jp` 配下は 1 件も出ていない**（大学内リンクを Google がまだ認識していない）。**10/16 に実ページを取得して確認**: `https://www.sys.es.osaka-u.ac.jp/faculty_members/`（「研究室HP」）と `https://www.es.osaka-u.ac.jp/ja/department/laboratory/`（「拡張現実」）に、`<a href="https://www.xr.sys.es.osaka-u.ac.jp/">` がサーバー出力の HTML として存在。表記は正しく、nofollow・noindex・canonical・robots.txt による制限なし → **リンクの書き方は原因ではない**。さらにユーザー確認: **リンクは数年前から設置済みで、リンク元 2 ページとも Google にインデックスされている**（`site:` で出る）→ 設置が新しい・リンク元が未インデックス、という説明は否定された。GSC のリンクレポートに出ない理由は不明（レポートが全件を載せない／7 月の乗っ取りでホストのリンク情報が影響を受けた、などは推測にとどまる）。**このレポートは網羅的でないものとして扱い、これ以上追わない**。`google.com` と `google.cl`・`.co.il`・`.com.pe`・`.fr`・`.lt`・`.si` が各 1〜4 ページ出ているが意味は不明
- 外部の学術系リンクが認識されていても抑制は解けていないので、被リンクの総量不足が主因ではないとみる（推測）。残る手段はエスカレーションの結果待ちと時間

### GSC の読み方（結論済み・再調査不要）
- 表示回数は「検索結果に出た回数」であり訪問数ではない。直接アクセスや `curl` は一切カウントされない。アクセス解析は入れていない
- 404 になったページでも、Google が再クロールして処理を終えるまでは検索結果に出る（表示回数が付く）
- 検索パフォーマンスのデータはプロパティ確認日（8/13）以降のみ。それ以前は遡れない
- 「ページのインデックス登録」レポートの更新は不定期（1〜2 週間空くことがある）。停滞しても異常ではない
- 表示回数が少ないうちは「クエリ」タブは匿名化されて空
- GSC の CSV エクスポートはフォルダ名が `Performance-on-Search-Generative-AI-Features-…` でも通常の検索パフォーマンスの内容
- 未登録ページの洗い出し手順: `/ja/sitemap.xml`＋`/en/sitemap.xml` の全 URL − 「登録済み」CSV の URL（スパム 8 プレフィックスを除外）。CSV はユーザーが添付後すぐ削除するので、**受け取ったらその場で読み切る**
- Claude の WebSearch ツールは `site:` 検索に使えない（無関係な結果が混ざる）。実測はブラウザで行う

## やらないと決めたこと

- スパム URL を列挙したクリーンアップ用サイトマップ（大学ドメインにアダルト URL の一覧を公開することになる）
- GSC 一括削除の Chrome 拡張（プレフィックス削除で足りている。未検証の拡張に GSC 権限を渡さない）
- Google Analytics などのアクセス解析
- 帯の青色背景、吹き出しの尻尾、電話アイコン（お問い合わせは `at`）、ブラウザ言語による自動転送
- **ホスト名の変更そのもの**（`xrlab.sys.es.osaka-u.ac.jp` 等への移行。ユーザーが「絶対にしたくない」と確定、10/16）。したがって旧ホストからの 301 の議論も不要
- README.md

## よく使う確認コマンド

```bash
hugo --gc --minify 2>&1 | grep -iE "error|warn|Total"          # ビルド
curl -sI https://www.xr.sys.es.osaka-u.ac.jp/ | head -3          # 公開状態
for p in tag bkm ypd bio ouy nbn tak kgf; do printf "%s " $p; curl -s -o /dev/null -w "%{http_code}\n" https://www.xr.sys.es.osaka-u.ac.jp/$p/; done   # スパムパスが 404 か
curl -s https://www.xr.sys.es.osaka-u.ac.jp/ja/sitemap.xml | grep -c "<loc>"   # 和文 URL 数（95、10/23 時点）
curl -s https://www.xr.sys.es.osaka-u.ac.jp/en/sitemap.xml | grep -c "<loc>"   # 英文 URL 数（94、10/23 時点）
dig +short CNAME www.xr.sys.es.osaka-u.ac.jp                     # xrgroup-uosaka.github.io. を指すこと
```

## 作業の進め方

- やり取りは日本語。数値は根拠（コマンド出力・CSV）を添えて示す。推測で断言しない（誤りは即座に指摘される）
- **コミット／プッシュはユーザー自身が行う**。変更後は内容を報告して「コミットしますか？」と確認する
- GSC の CSV や画面を添付されたら、まず読み切って要点を返す。ファイルは残らない前提で扱う
- 定期監視のスケジュールタスクは**設定していない**。フォーラムや GSC の確認は依頼があったときに行う
- デザイン変更は小さく試し、確認を取りながら進める（一度に大きく変えない）

## 更新ルール

**サイトの方針や仕組み（構成・データの持ち方・レイアウトの決まりごと・SEO の状況や判断）を変えたときは、このファイルも合わせて更新する。**
