---
title : Link OpenNewTab
long_title : Link OpenNewTab拡張機能
summary : この記事では、Link OpenNewTab拡張機能の使用方法について説明します
date : 2024-03-11
mt_type: extension
---

<span class="badge bg-primary">対応バージョン:>=2.9.1</span>

Link OpenNewTab拡張機能は、外部サイトへのリンクを新規タブで開くようにする拡張機能です。

この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- 外部サイトへのリンク

この拡張機能は絶対リンクの指定されたリンクについて、新規タブで開くようにします。

### オプション
<span class="badge bg-primary">対応バージョン:>=2.10</span>

`mkdocs.yml`にオプションとしてルールを書くことで、特定のドメインやそのサブドメイン、パスなどへジャンプするリンクについて、新規タブで開かないように構成できます。

```yml title="mkdocs.yml"
markdown_extensions:
  - lantana.link_opennewtab:
      ignore_rules:
        - base_url: "https://wsoft.ws/"
          subdomain_depth: 1
      rules:
        - base_url: "https://xyz.wsoft.ws/"
          subdomain_depth: 2
```

この設定を適用すると、ページは次のようになります。

**例**

```md
ignore_rulesが適用されるので、

- [これは新規タブにならない](https://wsoft.ws/)
- [これも新規タブにならない](https://docs.wsoft.ws/)

rulesが適用されるので、

- [これは新規タブになる](https://xyz.wsoft.ws/)
- [これも新規タブになる](https://a.xyz.wsoft.ws/)
```

> [!NOTE] 優先順位
> OpenNewTab拡張機能のルールは、`ignore_rules`よりも`rules`の設定が優先されます。

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
  - lantana.link_opennewtab
```

このとき、`link_opennewtab`はリンクを生成する拡張機能より後に追加してください。