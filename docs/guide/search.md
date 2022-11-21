---
title: 検索を使用する
summary: この記事では、Lantanaで検索を使用する方法を説明します
date : 2022-10-22
---
### 検索ページを作成する
ドキュメントディレクトリ直下に、`search.md`を作成し、下記の内容を貼り付けます。
```html
<div class="input-group mb-3">
  <input name="q" id="mkdocs-search-query" type="text" class="form-control" aria-label="検索" aria-describedby="inputGroup-sizing-default">
</div>

<div id="mkdocs-search-results">
  Sorry, page not found.
</div>
```

### 設定ファイルを編集する
このままでも検索は使用可能ですが、検索を使いやすくするためには、設定ファイルを編集する必要があります。
#### ヘッダーに検索ボックスを表示する
ヘッダーに検索ボックスを表示するには、下記の内容を追記します。
```yaml
visible_search : true
```
#### 言語の設定
検索で日本語を使用可能にするには、下記の内容を追記します。
```yaml
plugins:
    - search:
        lang : 'ja'
```