---
title: Welcome to Lantana!
summary: Lantana は、シンプルで軽量なMKDocsのテーマです。LantanaとMkDocsを使用すると、簡単に自分のサイトを作成できます。
author : taiseiue
author_url : https://github.com/taiseiue
---
Lantanaは、Bootstrapを使用した軽量なMkDocsのテーマです。
LantanaとMkDocsを使用すると、簡単に自分のサイトを作成できます。

Lantanaはシンプルながらも、多言語に対応しており、フリーソフトかつオープンソースプロジェクトで開発されています。LantanaはMITライセンスのもとで頒布されているので、オープンソースのプロジェクトとプロプライエタリのプロジェクトの両方で使用できます。

### 使用法

- [作業開始](./tutrial/getstarted/index.md)

### サポート
Lantanaの使用に際してサポートが必要な場合は、お気軽にお問合せください。

- 些細な質問でも、お気軽にGitHubの[Discussions](https://github.com/WSOFT-Project/lantana/discussions)に投稿してください！
- 不具合を報告したり、新機能をリクエストするには、GitHubで[Issue](https://github.com/WSOFT-Project/lantana/issues)を開いてください。

### 貢献
Lantanaプロジェクトは、世界中の開発者やユーザーからの貢献を歓迎しています。 どのように貢献できるかを知るには、[コントリビュートガイド](./contribute/index.md)をご覧ください。

=== "Not Me"
    Markdown **content**.

    Multiple paragraphs.

===+ "Select Me"
    More Markdown **content**.

    - list item a
    - list item b

=== "Not Me Either"
    Another Tab

===! "Tab A"
    Different tab set.

=== "Tab B"
    ```cs title="C#"
    Console.WriteLine("Hello,World!");
    ```

<nav>
  <div class="nav nav-underline" id="nav-tab" role="tablist">
    <button class="nav-link active" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home" type="button" role="tab" aria-controls="nav-home" aria-selected="true">Home</button>
    <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile" type="button" role="tab" aria-controls="nav-profile" aria-selected="false">Profile</button>
    <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact" type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Contact</button>
    <button class="nav-link" id="nav-disabled-tab" data-bs-toggle="tab" data-bs-target="#nav-disabled" type="button" role="tab" aria-controls="nav-disabled" aria-selected="false" disabled>Disabled</button>
  </div>
</nav>
<div class="tab-content" id="nav-tabContent">
  <div class="tab-pane fade show active" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab" tabindex="0">...</div>
  <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab" tabindex="0">...</div>
  <div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledby="nav-contact-tab" tabindex="0">...</div>
  <div class="tab-pane fade" id="nav-disabled" role="tabpanel" aria-labelledby="nav-disabled-tab" tabindex="0">...</div>
</div>