---
title: Jekyllサイトのディレクトリ構成
category: Web
tags:
  - Jekyll
---

`Jekyll`では、サイトを構成するために特定のディレクトリ・ファイルに役割が割り振られている．以下は、Jekyllの基本的なディレクトリ構成に関するのメモ書きである．

<!-- more -->


## 基本的なディレクトリ構成
Jekyllのプロジェクトを作成すると、以下のようなディレクトリ・ファイルが含まれます。

```
my-jekyll-site/
├── _posts/
├── _layouts/
├── _includes/
├── _data/
├── _sass/
├── _site/
├── assets/
├── _config.yml
├── index.html
└── README.md
```

> ![NOTE]
> `.`，`_`，`#`，`~`から始まるsourceディレクトリの全てのファイルやディレクトリは、デフォルトではビルド後のdestinationフォルダには含まれない．含めたい場合は，`_config.yml`の`include`にディレクトリを指定する．

なお，ディレクトリ構成の詳細は[ドキュメント][ドキュメント: ディレクトリ構成]を確認する．

## 各ディレクトリ・ファイルの役割

#### `_posts/`
**ブログ記事などのコンテンツ**をMarkdown形式で格納するディレクトリ．このディレクトリ内のファイルが`post`ととして認識される．

- ファイルの命名規則は `YYYY-MM-DD-title.md` にする必要がある．
- ファイル名が記事の「投稿日(date)」と「タイトル(title)」として設定される．（※Front-matterで指定しない場合）

#### `_layouts/`
ページのレイアウトテンプレートを格納するディレクトリ．例えば、`default.html` や `post.html` などのテンプレートを用意しておく．

#### `_includes/`
共通部分（ヘッダーやフッターなど）を部品として管理するディレクトリ．`{% include filename.html %}` を使って呼び出します。

#### `_data/`
YAML、JSON、CSV形式のデータを保存するディレクトリ．サイト内でデータを動的に扱う場合に使用する．

#### `_sass/`
Sass（SCSS）のスタイルシートを格納するディレクトリ．JekyllのSass機能と連携してCSSを生成できる．

#### `_site/`
Jekyllがビルドした際に生成されるHTMLファイルが格納されるディレクトリ．
※このディレクトリの内容は手動で編集しない．

#### `assets/`
CSS、JavaScript、画像などのアセットファイルを格納するディレクトリ．


#### `_config.yml`
サイトの設定を記述するファイル．タイトル，URL，ビルド設定，プラグインなどを定義します。

#### `index.html`
サイトのトップページのエントリーポイントとなるHTMLファイル．

#### `README.md`
プロジェクトの説明やセットアップ方法を記述するMarkdownファイル．


## 追加のディレクトリ
プロジェクトによっては、以下のディレクトリを追加することがある．

- `_plugins/`：Jekyll用のカスタムプラグインを格納．
- `_drafts/`：公開前の下書き記事を保存（`jekyll serve --drafts` でプレビュー可能）．
- `docs/`：プロジェクトのドキュメントを管理．
- `pages/`：固定ページ（About, Contact など）を整理するためのディレクトリ．


---

## 参考資料
- [qiita: Jekyll対応Liquid文法チートシート](https://qiita.com/mt_west/items/7a4f41c749ed582330e9)


<!-- リンク -->
[ドキュメント: ディレクトリ構成]: https://jekyllrb-ja.github.io/docs/structure/