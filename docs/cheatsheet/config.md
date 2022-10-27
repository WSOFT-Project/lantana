---
title: 設定ファイル
summary: この記事では、mkdocs.ymlで指定できる設定の一覧を示します
author : Taiseiue
author_url : https://github.com/taiseiue
date : 2022-10-22
---

Lantanaでは、`mkdocs.yml`を使ってサイト全体の設定を変更できます。

### サイト名
サイトの名前を指定します。これは、サイト上部に表示されるほか、ページのタイトルにも含まれます。
```yaml
site_name: サイト名
```

### 著作権表示
サイトの著作権表示を指定します。これは、サイト下部に表示されます。
```yaml
copyright : 'Copyright &copy; 2022 ME All Rights Reserved.'
```

### ドキュメントディレクトリ
記事が保存されているディレクトリを指定します。
```yaml
docs_dir : 'docs'
```

### JavaScript
サイトの各ページに挿入されるJavaScriptを指定します。
```yaml
extra_javascript:
  - 'main.js'
```

### スタイルシート
サイトの各ページに挿入されるスタイルシートを指定します。
```yaml
extra_stylesheet:
  - 'main.js'
```

### ファビコン
サイトのアイコンです。これは、サイト上部に表示されるほか、サイトのファビコンにも使用されます。
```yaml
favicon : favicon.png
```

### Svg形式のファビコン
Svc形式のファビコンです。これは、サイトのファビコンに使用されます。
```yaml
favicon_svg : favicon.svg
```

### フッターアイコン
サイトのサブアイコンです。これは、サイト下部に表示されます。
```yaml
footimg : favicon.svg
```

### サイトの画像
サイトの画像です。これは、記事に指定された画像が存在しないときに使用されます。
```yaml
image : thumbnail.png
```

### サイトの言語
サイトの言語です。これは、ページの言語としてブラウザに伝えられます。
```yaml
language : ja
```

### テーマ
MKDocsのテーマです。これを`lantana`に指定することでLantanaが有効になります。
```yaml
theme : lantana
```

### プラグイン
MKDocsで使用するプラグインです。
```yaml
plugins:
    - search:
```

### 検索の言語
サイト内検索で使用される言語を指定します。この項目で`'ja'`を指定することで、サイト内検索で日本語を検索可能になります。
```yaml
plugins:
    - search:
        lang : 'ja'
```

### マークダウン拡張
記事内で使用できるマークダウンの拡張機能です。Lantanaのコードハイライトなどの機能はこれを用いて実装されています。
```yaml
markdown_extensions:
    # コードハイライトの設定
    - codehilite
    # アラート修飾の設定
    - admonition
    # スーパーフェンス機能の設定
    - pymdownx.superfences
    # コンテンツの折りたたみ
    - pymdownx.details
```

### 検索の表示
サイトのヘッダーに検索ボックスが表示されるかどうかの値です。
```yaml
visible_seartch : true
```

### ヘッダーを非表示
サイトのヘッダーを非表示にするかどうかの値です。
```yaml
disable_header : false
```

### フッターを非表示
サイトのフッターを非表示にするかどうかの値です。
```yaml
disable_footer : false
```