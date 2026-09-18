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
- 再発防止: ドメインの付け替えは「新リポジトリで確保 → 旧から外す」の順。空白時間を作らない

## SEO / Google Search Console（2026-08〜09）

### 経緯と現状
- 復旧後、GSC 上は登録済みなのに **検索結果に一切出ない**状態が約2か月続いた。技術要因（robots・noindex・canonical・削除ツール・手動対策・セキュリティ問題・セーフサーチ）はすべて確認済みで該当なし → ホスト単位のアルゴリズム抑制と判断
- 実施済み: 所有権確認（HTML タグ）、サイトマップ送信、8 つのスパムパス（`/tag/ /bkm/ /ypd/ /bio/ /ouy/ /nbn/ /tak/ /kgf/`）のプレフィックス削除申請、canonical、robots.txt、JS 言語転送の廃止、**全 177 ページの URL 検査→インデックス送信を 9/16 に一巡完了**（1日 10〜12 件が上限）
- 登録済みページ数の推移（正規／スパム）: 8/14 110／117 → 9/4 137／33 → **9/15 170／21**（残り 5 件は旧ページネーション等の残骸）。送信したページは当日クロール・2〜3 日で登録される
- **表示回数（検索パフォーマンス）**: 8/13〜9/12 は正規ページ 0 回 → **9/13 `/en/`（米国）、9/14 `/`（日本）で初表示**。抑制が解け始めたと判断（9/17 時点）
- 9/15〜16 送信分で登録未確認の 7 件: `/en/post/25-04-01-takes-flight/` `25-04-08-inaugural-members/` `25-04-18-zollmann-langlotz-visit/` `25-05-23-distinguished-professor/` `25-05-23-welcome-race/` `25-08-08-open-campus/` `25-09-25-sommart-graduation/`
- 相談スレッド（日本語コミュニティ）: https://support.google.com/webmasters/thread/462445673?hl=ja — 回答者 Wang Huaimin、tokoma noshi（プラチナ）、takano（プラチナ）。「クリーンに保って待つ」が共通見解

### 判断基準と次の一手
- 回復判定は **検索パフォーマンスの表示回数**で行う（`site:` 検索は網羅性が無く、出なくても登録されていない証拠にはならない）
- 9/23 頃に表示回数を再確認 → 増えていれば自然回復に任せる。9/14 の 1 件で止まっていれば tokoma noshi 氏の返信直下にエスカレーション依頼を投稿（要点: 登録は正常に進んでいる／表示回数だけが 0／大学公式サイトで実害／手動対策が無く再審査の経路が無い／Google 社員への確認を依頼）
- 10 月上旬になっても表示が無ければ、ホスト名変更（例 `xrlab.sys.es.osaka-u.ac.jp`）を検討。その場合 **旧ホストから 301 しない**（抑制を引き継がないため）
- 効く施策として被リンク（`diwai.github.io`・researchmap 等 → 本サイト）は未実施

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
- ホスト名を変える場合の旧ホストからの 301
- README.md

## よく使う確認コマンド

```bash
hugo --gc --minify 2>&1 | grep -iE "error|warn|Total"          # ビルド
curl -sI https://www.xr.sys.es.osaka-u.ac.jp/ | head -3          # 公開状態
for p in tag bkm ypd bio ouy nbn tak kgf; do printf "%s " $p; curl -s -o /dev/null -w "%{http_code}\n" https://www.xr.sys.es.osaka-u.ac.jp/$p/; done   # スパムパスが 404 か
curl -s https://www.xr.sys.es.osaka-u.ac.jp/ja/sitemap.xml | grep -c "<loc>"   # 和文 URL 数（89）
curl -s https://www.xr.sys.es.osaka-u.ac.jp/en/sitemap.xml | grep -c "<loc>"   # 英文 URL 数（88）
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
