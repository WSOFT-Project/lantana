---
title : MermaidPrecompiler
long_title : MermaidPrecompiler拡張機能
summary : この記事では、MermaidPrecompiler拡張機能の使用方法について説明します
date : 2024-03-07
---

<span class="badge bg-primary">対応バージョン:>=2.9</span>

MermaidPrecompiler拡張機能は、LantanaでMermaid図表を使用できるようにする拡張機能です。
この拡張機能を有効化することで、以下のコンポーネントが使用できるようになります。

- Mermaidブロック

この拡張機能は、従来ユーザーサイドでJavaScriptを使用して行っていたMermaidのレンダリング処理を事前に行うために導入されました。

この拡張機能を使用するには、インターネット接続が必要です。

### 使用方法

```markdown title="例"
```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

**結果**

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

### 導入方法
設定ファイル(`mkdocs.yml`)に以下の行を追加します。

```yml title="mkdocs.yml"
markdown_extensions:
      (中略)
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:mermaid2.fence_mermaid
    - lantana.mermaid_precompile
      (中略)
```

このとき、`lantana.mermaid_precompile`は`markdown_superfences`より後に追加してください。