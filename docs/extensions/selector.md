---
title : Selector
long_title : Selector拡張機能
summary : この記事では、Selector拡張機能の使用方法について説明します
date : 2024-05-06
---

<span class="badge bg-primary">対応バージョン:>=2.9.8.1</span>

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

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana.selector
```
