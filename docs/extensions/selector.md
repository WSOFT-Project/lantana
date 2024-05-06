---
title : Selector
long_title : Selector拡張機能
summary : この記事では、Selector拡張機能の使用方法について説明します
date : 2024-05-06
---

<span class="badge bg-primary">対応バージョン:>=2.9.8</span>

Selector拡張機能は、Lantanaに選択可能なサイトへのリンクを追加する拡張機能です。

この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- リンクセレクター

この拡張機能は、[lantana拡張機能](./lantana.md)に依存しています。
この拡張機能を使用するには、lantana拡張機能の使用が必要です。

### 使用方法
引用の先頭に`[!SELECTOR] タイトル`をつけ、引用中にリンクを列挙します。

```markdown title="Markdown"
> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)
```

**結果**

> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

#### 注意事項

この拡張機能は、Alerts拡張機能と異なり、引用を使ってリンクを作成します。
MkDocsのMarkdownは、連続したふたつ以上の引用をひとつの引用として認識します。
このため、この拡張機能で生成されるリンクは連続して配置できないことにご注意ください。
次の例をご覧ください。

```md title="Markdown"
> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

> [!SELECTOR] もう一度サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)
```

**結果**

> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

> [!SELECTOR] もう一度サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

このような結果を避けるには、アラートの間に任意の要素を追加してください。

```md title="Markdown"
> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

*TIP*

> [!SELECTOR] もう一度サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)
```

> [!SELECTOR] サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

*TIP*

> [!SELECTOR] もう一度サイトを選択
> [WebSailing](https://docs.wsoft.ws/products/websailing)
> [AliceScript](https://docs.wsoft.ws/products/alice)

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana.selector
```
