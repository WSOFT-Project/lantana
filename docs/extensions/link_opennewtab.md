---
title : Link OpenNewTab
long_title : Link OpenNewTab拡張機能
summary : この記事では、Link OpenNewTab拡張機能の使用方法について説明します
date : 2024-03-11
---

<span class="badge bg-primary">対応バージョン:>=2.9.1</span>

Link OpenNewTab拡張機能は、外部サイトへのリンクを新規タブで開くようにする拡張機能です。

この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- 外部サイトへのリンク

この拡張機能は絶対リンクの指定されたリンクについて、新規タブで開くようにします。

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - lantana.link_opennewtab
```

このとき、`link_opennewtab`はリンクを生成する拡張機能より後に追加してください。