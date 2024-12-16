---
title: マークダウン記法
summary: この記事では、Lantanaで使用できるマークダウン記法の一覧を示します
date : 2022-10-22
order : 1
---

Lantanaの記事は、すべてMarkdown記法で記述します。
Lantanaの記事は、[Python Markdown(PyMdown)](https://facelessuser.github.io/PyMdown/)を使ってHTMLにレンダリングされます。
Lantanaでは、一般的なMarkdown記法に加えて独自の記法や、[拡張機能](../extensions/index.md)で導入されている記法を使用できます。
この記事では、Lantanaで使用できるMarkdown記法の一覧を示します。

この記事のサンプルは、Markdown記法とビルド結果のHTML、最終的な表示を順番に示します。もしあなたがMarkdownでどのような記事を書けるか調べている場合、「表示」タブを確認することをおすすめします。以下のボタンをクリックして、すべての表示を一斉に切り替えられます。

<div class="btn-group btn-group-sm padding-bottom" role="group">
    <button type="button" id="switch-btn-1" class="btn btn-outline-primary">Markdown</button>
    <button type="button" id="switch-btn-2" class="btn btn-outline-primary">HTML</button>
    <button type="button" id="switch-btn-3" class="btn btn-outline-primary">表示</button>
</div>

<br/>
記事の先頭に書く、記事のタイトルや説明などを設定するメタタグの書き方を知るには、[メタタグ](./metatag.md)をご覧ください。

## 見出し
記事に見出しをつけます。見出しは目次の表示され、見出しへのリンクが生成されます。また、記事にタイトルが指定されていない場合、自動的に記事の一番最初の見出しがタイトルになります。

=== "Markdown"

    ```markdown
    ## これはH2タグになります
    ### これはH3タグになります
    #### これはH4タグになります
    ```
=== "HTML"

    ```html
    <h2>これはH2タグになります</h2>
    <h3>これはH3タグになります</h3>
    <h4>これはH4タグになります</h4>
    ```
=== "表示"

    <h2>これはH2タグになります</h2>
    <h3>これはH3タグになります</h3>
    <h4>これはH4タグになります</h4>
    ---

## テキスト
Markdownでテキストを記述する方法を説明します。
#### 基本的なテキスト
装飾や特殊文字の無いテキストは、そのまま記述します。

=== "Markdown"

    ```markdown
    Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。

    段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、  
    行末に半角スペースを2つ付けます。
    ```
=== "HTML"

    ```html
    <p>Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。</p>
    <p>段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、<br>
    行末に半角スペースを2つ付けます。</p>
    ```
=== "表示"

    Lantanaは、シンプルで軽量なMKDocsのテーマです。
    HTMLの知識がなくても簡単にサイトを作成できます。

    段落を変えるには、1行空行を挟みます。
    段落を変えないで改行するには、  
    行末に半角スペースを2つ付けます。
    ---

#### エスケープ
特殊文字（たとえば、\*や\#など）をテキストとして表示するには、`\`を使って文字をエスケープする必要があります。

=== "Markdown"

    ```markdown
    Markdownで特殊文字を表示するには、\\を使って文字をエスケープします。
    例えば、\*や\#、\!、\`などをエスケープできます。

    HTMLタグをエスケープするには、<br/\>のように書きます。
    ```
=== "HTML"

    ```html
    <p>Markdownで特殊文字を表示するには、\を使って文字をエスケープします。
    例えば、*や#、!、`などをエスケープできます。</p>
    <p>HTMLタグをエスケープするには、&lt;br/&gt;のように書きます。</p>
    ```
=== "表示"

    Markdownで特殊文字を表示するには、\\を使って文字をエスケープします。
    例えば、\*や\#、\!、\`などをエスケープできます。

    HTMLタグをエスケープするには、<br/\>のように書きます。

    ---

#### 装飾
文章を様々に装飾する方法をまとめて紹介します。

=== "Markdown"

    ```markdown
    付けたい部分を\*\*(アスタリスク1つ)で囲むと、**太字**に、
    \*(アスタリスク1つ)で囲むと、*斜体*になります。

    \*\*\*(アスタリスク3つ)で囲むことで、太字と斜体を***組み合わせる***こともできます。

    付けたい部分を\~(チルダ1つ)で囲むと~下付き文字~に、
    \^(キャレット1つ)で囲むと^上付き文字^になります。

    \~\~(チルダ2つ)で囲むと~~打ち消し線~~が、
    \^\^(キャレット2つ)で囲むと^^下線^^が、
    \=\=(イコール2つ)で囲むと==ハイライト==がつきます。
    ```
=== "HTML"

    ```html
    <p>付けたい部分を**(アスタリスク1つ)で囲むと、<strong>太字</strong>に、
    *(アスタリスク1つ)で囲むと、<em>斜体</em>になります。</p>
    <p>***(アスタリスク3つ)で囲むことで、太字と斜体を<strong><em>組み合わせる</em></strong>こともできます。</p>
    <p>付けたい部分を~(チルダ1つ)で囲むと<sub>下付き文字</sub>に、
    ^(キャレット1つ)で囲むと<sup>上付き文字</sup>になります。</p>
    <p>~~(チルダ2つ)で囲むと<del>打ち消し線</del>が、
    ^^(キャレット2つ)で囲むと<ins>下線</ins>が、
    ==(イコール2つ)で囲むと<mark>ハイライト</mark>がつきます。</p>
    ```
=== "表示"

    付けたい部分を\*\*(アスタリスク1つ)で囲むと、**太字**に、
    \*(アスタリスク1つ)で囲むと、*斜体*になります。

    \*\*\*(アスタリスク3つ)で囲むことで、太字と斜体を***組み合わせる***こともできます。

    付けたい部分を\~(チルダ1つ)で囲むと~下付き文字~に、
    \^(キャレット1つ)で囲むと^上付き文字^になります。

    \~\~(チルダ2つ)で囲むと~~打ち消し線~~が、
    \^\^(キャレット2つ)で囲むと^^下線^^が、
    \=\=(イコール2つ)で囲むと==ハイライト==がつきます。

    ---

#### 脚注
`[^1]`のように文章の任意の場所に脚注へのリンクを設置すると、ページの末尾の説明へ移動します。
説明は文章中の任意の場所で`[^1]: <説明>`とすることで記述できます。

=== "Markdown"
    ```md
    そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 [^1]でしたから役所のなかでも、ずうっと下の方でしたし俸給[^2]もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。

    [^1]: ロシア帝国では、軍隊、政府、および宮廷における地位と階級を**[官等表](https://en.wikipedia.org/wiki/Table_of_Ranks)**と呼ばれるもので管理していました。
    [^2]: 役所や会社に務める人の給料のことを指す言葉です。
    ```

=== "HTML"
    
    ```html
    <p>そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 <sup id="fnref2:1"><a class="footnote-ref" href="#fn:1">1</a></sup>でしたから役所のなかでも、ずうっと下の方でしたし俸給<sup id="fnref2:2"><a class="footnote-ref" href="#fn:2">2</a></sup>もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。</p>

    <!-- 以下が、ページ末尾に生成されます -->
     <div class="footnote">
        <hr>
        <ol>
            <li id="fn:1">
                <p>ロシア帝国では、軍隊、政府、および宮廷における地位と階級を<strong><a href="https://en.wikipedia.org/wiki/Table_of_Ranks" rel="noopener noreferrer" target="_blank">官等表</a></strong>と呼ばれるもので管理していました。&nbsp;<a class="footnote-backref" href="#fnref:1" title="Jump back to footnote 1 in the text">↩</a></p>
            </li>
            <li id="fn:2">
                <p>役所や会社に務める人の給料のことを指す言葉です。&nbsp;<a class="footnote-backref" href="#fnref:2" title="Jump back to footnote 2 in the text">↩</a></p>
            </li>
        </ol>
    </div>
    ```
=== "表示"

    そのころわたくしは、モリーオ市の博物局に勤めて居りました。
    十八等官 [^1]でしたから役所のなかでも、ずうっと下の方でしたし俸給[^2]もほんのわずかでしたが、受持ちが標本の採集や整理で生れ付き好きなことでしたから、わたくしは毎日ずいぶん愉快にはたらきました。

    [^1]: ロシア帝国では、軍隊、政府、および宮廷における地位と階級を**[官等表](https://en.wikipedia.org/wiki/Table_of_Ranks)**と呼ばれるもので管理していました。
    [^2]: 役所や会社に務める人の給料のことを指す言葉です。

    ---

## リンク
記事にリンクを貼って、サイト内の他のページや他のサイトとリンクできます。

#### 基本的なリンク
リンクには、テキストとUrlを設定します。
[Link OpenNewTab](../extensions/lantana/link_opennewtab.md)拡張機能を使用している場合、自動的に他のサイトへのリンクが新規タブで開きます。

=== "Markdown"

    ```markdown
    サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、[設定ファイル](./config.md)と書きます。
    
    外部サイトへのリンクは、絶対Urlで書きます。
    例えば、[example.com](https://example.com/)と書きます。
    ```
=== "HTML"

    ```html
    <p>サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、<a href="../config/">設定ファイル</a>と書きます。</p>
    <p>外部サイトへのリンクは、絶対Urlで書きます。
    例えば、<a href="https://example.com/" rel="noopener,noreferrer" target="_blank">example.com</a>と書きます。</p>
    ```
=== "表示"

    サイト内の記事にリンクを貼るには、記事のMarkdownファイルへのパスを書きます。
    例えば、[設定ファイル](./config.md)と書きます。
    
    外部サイトへのリンクは、絶対Urlで書きます。
    例えば、[example.com](https://example.com/)と書きます。

    ---

#### 自動リンク
Urlやメールアドレスを書くだけで、自動的にリンクになります。

=== "Markdown"

    ```markdown
    https://example.com/

    user@example.com
    ```
=== "HTML"

    ```html
    <p><a href="https://example.com/" rel="noopener noreferrer" target="_blank">https://example.com/</a></p>
    <p><a href="mailto:user@example.com">user@example.com</a></p>
    ```
=== "表示"

    https://example.com/

    user@example.com

    ---

#### タイトル付きリンク
HTMLのtitle属性を指定できます。
一部のブラウザでリンクをホバーした時に表示されます。

=== "Markdown"

    ```markdown
    [WSOFT](https://wsoft.ws/ "WSOFTのサイト")をぜひご覧になってください。
    ```
=== "HTML"

    ```html
    <p><a href="https://wsoft.ws/" rel="noopener noreferrer" target="_blank" title="WSOFTのサイト">WSOFT</a>をぜひご覧になってください。</p>
    ```
=== "表示"

    [WSOFT](https://wsoft.ws/ "WSOFTのサイト")をぜひご覧になってください。

    ---

#### 複数リンク
リンクを定義して、簡単に複数の場所で使いまわせます。

=== "Markdown"

    ```markdown
    [WSOFT]は、Lantanaの開発元です。[WSOFTのサイト][WSOFT]で、他の作品もご覧いただけます。

    [WSOFT]: https://wsoft.ws/
    ```
=== "HTML"

    ```html
    <p><a href="https://example.com/" rel="noopener noreferrer" target="_blank">https://example.com/</a></p>
    <p><a href="mailto:user@example.com">user@example.com</a></p>
    ```
=== "表示"

    [WSOFT]は、Lantanaの開発元です。[WSOFTのサイト][WSOFT]で、他の作品もご覧いただけます。

    [WSOFT]: https://wsoft.ws/

    ---

## 箇条書き
#### 基本の箇条書き
箇条書きで書くには、\*か\*、\+のいずれかを文頭につけます。
箇条書きの上には空行が必要です。

=== "Markdown"

    ```markdown
    - 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
    - 記号のあとには**スペースが必要**です
    - 同じリストでは同じ記号を使うことを推奨します。
    ```
=== "HTML"

    ```html
    <ul>
        <li>文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります</li>
        <li>記号のあとには<strong>スペースが必要</strong>です</li>
        <li>同じリストでは同じ記号を使うことを推奨します。</li>
    </ul>
    ```
=== "表示"

    - 文頭に"*"、"+"、"-"のいずれかを入れると順序なしリストになります
    - 記号のあとには**スペースが必要**です
    - 同じリストでは同じ記号を使うことを推奨します。
  
    ---

#### 数字付きの箇条書き
数字付きの箇条書きを書くには、数字を先頭につけます。
箇条書きの上には空行が必要です。数字はどんな場合でも、ブラウザによって1から始まる数字にレンダリングされます。

=== "Markdown"

    ```markdown
    1. 文頭に"数字."を入れると番号付きリストになります。
    2. "数字."のあとには**スペースが必要**です
    3. ブラウザによって1から始まる数字にレンダリングされます。
    ```
=== "HTML"

    ```html
    <ol>
        <li>文頭に"数字."を入れると番号付きリストになります。</li>
        <li>"数字."のあとには<strong>スペースが必要</strong>です</li>
        <li>ブラウザによって1から始まる数字にレンダリングされます。</li>
    </ol>
    ```
=== "表示"

    1. 文頭に"数字."を入れると番号付きリストになります。
    2. "数字."のあとには**スペースが必要**です
    3. ブラウザによって1から始まる数字にレンダリングされます。

#### タスクリスト
箇条書きに`[ ]`を追加すると、タスクリストになり、チェックボックスが表示されます。`[x]`と書くとチェックが入ります。
順序なしリストの記述の後ろに[ ]を入れるとチェックボックスが生成されます。
また、チェックが入った状態のボックスを生成する場合は[x]を入力します。

=== "Markdown"

    ```markdown
    - [x] バナナを買う
    - [ ] りんごを買う
    - [ ] ぶどうを買う
    ```
=== "HTML"

    ```html
    <ul class="task-list">
        <li class="task-list-item"><label class="task-list-control"><input checked="" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> バナナを買う</li>
        <li class="task-list-item"><label class="task-list-control"><input checked="false" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> りんごを買う</li>
        <li class="task-list-item"><label class="task-list-control"><input checked="false" disabled="" type="checkbox"><span class="task-list-indicator"></span></label> ぶどうを買う</li>
    </ul>
    ```
=== "表示"

    - [x] バナナを買う
    - [ ] りんごを買う
    - [ ] ぶどうを買う

---

## 画像
記事内で画像を埋め込んで表示できます。
画像の説明と画像へのパスを順番に記述します。

=== "Markdown"

    ```markdown
    ![Aliceの正面写真](./media/alice.jpg)
    ```
=== "HTML"

    ```html
    <p>
        <img alt="Aliceの正面写真" class="img-fluid" src="../media/alice.jpg">
    </p>
    ```
=== "表示"

    ![Aliceの正面写真](./media/alice.jpg)

---

## 引用
文頭に>を置くことで引用になります。引用文が複数行にまたがる場合、すべての文頭に>を置きます。引用をネストすることもできます。

=== "Markdown"

    ```markdown
    > 本郷の大学前の電車通りを、轟々と音立てて電車が通った。  
    > 葉の散りかかった銀杏並木の上に、天が凄まじい高さで拡がっている。
    > <figcaption class="blockquote-footer">
    >   梅崎春生 「風宴」
    > </figcaption>
    ```
=== "HTML"

    ```html
    <blockquote class="blockquote">
        <p>
            本郷の大学前の電車通りを、轟々と音立てて電車が通った。
            <br/>
            葉の散りかかった銀杏並木の上に、天が凄まじい高さで拡がっている。
        </p>
        <figcaption class="blockquote-footer">
            梅崎春生 「風宴」
        </figcaption><p></p>
    </blockquote>
    ```
=== "表示"

    > 本郷の大学前の電車通りを、轟々と音立てて電車が通った。  
    > 葉の散りかかった銀杏並木の上に、天が凄まじい高さで拡がっている。
    > <figcaption class="blockquote-footer">
    >   梅崎春生 「風宴」
    > </figcaption>

---

## 表
縦棒でカラムを分けることで、表を作成できます。

### 基本の表
次の例をご覧ください。

=== "Markdown"

    ```markdown
    #|学年|組| 名前 
    -|---|--|------
    1|  1| 1| 青木 太郎
    2|  1| 2| 井上 二郎
    3|  2| 1| 佐藤 花子 
    ```
=== "HTML"

    ```html
    <table class="table">
        <thead>
            <tr>
                <th>#</th>
                <th>学年</th>
                <th>組</th>
                <th>名前</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>1</td>
                <td>1</td>
                <td>青木 太郎</td>
            </tr>
            <tr>
                <td>2</td>
                <td>1</td>
                <td>2</td>
                <td>井上 二郎</td>
            </tr>
            <tr>
                <td>3</td>
                <td>2</td>
                <td>1</td>
                <td>佐藤 花子</td>
            </tr>
        </tbody>
    </table>
    ```
=== "表示"

    #|学年|組| 名前 
    -|---|--|------
    1|  1| 1| 青木 太郎
    2|  1| 2| 井上 二郎
    3|  2| 1| 佐藤 花子 

---

### 表の左右中央寄せ
左右どちらか、または両方の端にコロン(:)をつけることで、表内の文を左右中央寄せにできます。

=== "Markdown"

    ```markdown
    | Left align | Right align | Center align |
    |:-----------|------------:|:------------:|
    | This       | This        | This         |
    | column     | column      | column       |
    | will       | will        | will         |
    | be         | be          | be           |
    | left       | right       | center       |
    | aligned    | aligned     | aligned      |
    ```
=== "HTML"

    ```html
    <table class="table">
        <thead>
            <tr>
                <th align="left">Left align</th>
                <th align="right">Right align</th>
                <th align="center">Center align</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td align="left">This</td>
                <td align="right">This</td>
                <td align="center">This</td>
            </tr>
            <tr>
                <td align="left">column</td>
                <td align="right">column</td>
                <td align="center">column</td>
            </tr>
            <tr>
                <td align="left">will</td>
                <td align="right">will</td>
                <td align="center">will</td>
            </tr>
            <tr>
                <td align="left">be</td>
                <td align="right">be</td>
                <td align="center">be</td>
            </tr>
            <tr>
                <td align="left">left</td>
                <td align="right">right</td>
                <td align="center">center</td>
            </tr>
            <tr>
                <td align="left">aligned</td>
                <td align="right">aligned</td>
                <td align="center">aligned</td>
            </tr>
        </tbody>
    </table>
    ```
=== "表示"

    | Left align | Right align | Center align |
    |:-----------|------------:|:------------:|
    | This       | This        | This         |
    | column     | column      | column       |
    | will       | will        | will         |
    | be         | be          | be           |
    | left       | right       | center       |
    | aligned    | aligned     | aligned      |

---

## コメント

HTMLと同じようにコメントが書けます。コメントはレンダリング時に削除されます。

=== "Markdown"

    ```markdown
    ここより下にコメントがあります。
    <!-- これはコメントです -->
    ```
=== "HTML"

    ```html
    <p>ここより下にコメントがあります。</p>
    ```
=== "表示"

    ここより下にコメントがあります。
    <!-- これはコメントです -->

---

## コード
インラインコード要素と、コードブロックのふたつを使って、コードをシンタックスハイライトできます。
Lantanaは、既定では[Pygments](https://pygments.org/)によるシンタックスハイライトが提供されます。

### インラインコード
文の途中でコードを表すには、バッククオート（\`）でテキストを囲みます。また、シンタックスハイライトを行うには、コロン（`:::`）3つの後に言語を指定します。次に例を示します。

=== "Markdown"

    ```markdown
    Pythonでモジュールを読み込むには、`:::py3 import`文を使います。  
    例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。
    ```

=== "HTML"
    ```html
    <p>Pythonでモジュールを読み込むには、<code class="highlight"><span class="kn">import</span></code>文を使います。<br>
    例えば、<code>sys</code>モジュールを読み込むには、<code class="highlight"><span class="kn">import</span> <span class="nn">sys</span></code>と書きます。</p>
    ```

=== "表示"
    Pythonでモジュールを読み込むには、`:::py3 import`文を使います。  
    例えば、`sys`モジュールを読み込むには、`:::py3 import sys`と書きます。

---

### コードブロック
記事内のテキストのある部分がコードであることを表すには、バッククォート（\`）3つで囲んでフェンスを作成します。コードブロック内で使用されているプログラミング言語を指定するには、開始時のバッククォートの後に言語名を記述します。シンタックスハイライトに対応している言語の一覧は、[Languages — Pygments](https://pygments.org/languages/)をご覧ください。次に例を示します。

=== "Markdown"

    ````markdown
    ```c
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
    ````
=== "HTML"

    ```html
    <div class="highlight position-relative">
        <button class="btn lantana_codeblock_copybtn position-absolute top-0 end-0"><i class="bi bi-clipboard"></i></button>
        <pre>
            <span></span>
            <code>
                <a href="#__codelineno-28-1" id="__codelineno-28-1" name="__codelineno-28-1"></a><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdio.h&gt;</span>
                <a href="#__codelineno-28-2" id="__codelineno-28-2" name="__codelineno-28-2"></a>
                <a href="#__codelineno-28-3" id="__codelineno-28-3" name="__codelineno-28-3"></a><span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(){</span>
                <a href="#__codelineno-28-4" id="__codelineno-28-4" name="__codelineno-28-4"></a><span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"Hello World.</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
                <a href="#__codelineno-28-5" id="__codelineno-28-5" name="__codelineno-28-5"></a><span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
                <a href="#__codelineno-28-6" id="__codelineno-28-6" name="__codelineno-28-6"></a><span class="p">}</span>
            </code>
        </pre>
    </div>
    ```
=== "表示"

    ```c
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
---

#### コードのタイトル
ファイル名などを指定するために、コードにタイトルをつけられます。
コードにタイトルをつけると、コードブロックにヘッダーがつきます。
次に例を示します。

=== "Markdown"

    ````markdown
    ```c title="hello_world.c"
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
    ````
=== "HTML"

    ```html
    <div class="highlight position-relative">
        <button class="btn lantana_codeblock_copybtn position-absolute top-0 end-0"><i class="bi bi-clipboard"></i></button>
        <span class="filename">hello_world.c</span>
        <pre><span></span>
            <code><a href="#__codelineno-32-1" id="__codelineno-32-1" name="__codelineno-32-1"></a><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdio.h&gt;</span>
                <a href="#__codelineno-32-2" id="__codelineno-32-2" name="__codelineno-32-2"></a>
                <a href="#__codelineno-32-3" id="__codelineno-32-3" name="__codelineno-32-3"></a><span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(){</span>
                <a href="#__codelineno-32-4" id="__codelineno-32-4" name="__codelineno-32-4"></a><span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"Hello World.</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
                <a href="#__codelineno-32-5" id="__codelineno-32-5" name="__codelineno-32-5"></a><span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
                <a href="#__codelineno-32-6" id="__codelineno-32-6" name="__codelineno-32-6"></a><span class="p">}</span>
            </code>
        </pre>
    </div>
    ```
=== "表示"

    ```c title="hello_world.c"
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
---

#### コードのマーカー
コード内で注目して欲しい部分を表現するために、コードにマーカーを引くことができます。
マーカーを引くには、`hl_lines`にハイライトしたい行番号を書きます。

=== "Markdown"

    ````markdown
    ```c hl_lines="1 4-5"
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
    ````
=== "HTML"

    ```html
    <div class="highlight position-relative">
        <button class="btn lantana_codeblock_copybtn position-absolute top-0 end-0"><i class="bi bi-clipboard"></i></button>
        <pre><span></span>
            <code>
                <a href="#__codelineno-36-1" id="__codelineno-36-1" name="__codelineno-36-1"></a><span class="hll"><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;stdio.h&gt;</span>
                </span><a href="#__codelineno-36-2" id="__codelineno-36-2" name="__codelineno-36-2"></a>
                <a href="#__codelineno-36-3" id="__codelineno-36-3" name="__codelineno-36-3"></a><span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">(){</span>
                <a href="#__codelineno-36-4" id="__codelineno-36-4" name="__codelineno-36-4"></a><span class="hll"><span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"Hello World.</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
                </span><a href="#__codelineno-36-5" id="__codelineno-36-5" name="__codelineno-36-5"></a><span class="hll"><span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
                </span><a href="#__codelineno-36-6" id="__codelineno-36-6" name="__codelineno-36-6"></a><span class="p">}</span>
            </code>
        </pre>
    </div>
    ```
=== "表示"

    ```c hl_lines="1 4-5"
    #include <stdio.h>

    int main(){
        printf("Hello World.\n");
        return 0;
    }
    ```
---

## 数式
LaTex記法を使って美しい数式を書けます。
この機能は、[MathJax](https://www.mathjax.org/)を使ってレンダリングされます。

### インライン数式
文中に数式を埋め込むには、数式部分を\$で囲みます。

=== "Markdown"

    ```markdown
    ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 ${\displaystyle p}p$ と、
    ${\displaystyle p-1}p-1$ を割り切る大きな素数 ${\displaystyle q}q$ を用意します。
    また、 ${\displaystyle g}g$ を
    ${\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}{\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}$ の元で、
    位数が ${\displaystyle q}q$ である値とします。
    この ${\displaystyle p,q,g}{\displaystyle p,q,g}$ の値は公開されているものとします。
    ```
=== "HTML"

    ```html
    <p>ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="0" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>p</mi></mstyle></mrow><mi>p</mi></math></mjx-assistive-mml></mjx-container></span> と、
        <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="1" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-mstyle></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>p</mi><mo>−</mo><mn>1</mn></mstyle></mrow><mi>p</mi><mo>−</mo><mn>1</mn></math></mjx-assistive-mml></mjx-container></span> を割り切る大きな素数 <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="2" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>q</mi></mstyle></mrow><mi>q</mi></math></mjx-assistive-mml></mjx-container></span> を用意します。
        また、 <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="3" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D454 TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D454 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>g</mi></mstyle></mrow><mi>g</mi></math></mjx-assistive-mml></mjx-container></span> を
        <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="4" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-texatom texclass="ORD"><mjx-texatom texclass="ORD"><mjx-mi class="mjx-ds mjx-b"><mjx-c class="mjx-c2124 TEX-A"></mjx-c></mjx-mi></mjx-texatom></mjx-texatom><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2F"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-texatom texclass="ORD"><mjx-mi class="mjx-ds mjx-b"><mjx-c class="mjx-c2124 TEX-A"></mjx-c></mjx-mi></mjx-texatom></mjx-texatom><mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-script style="vertical-align: 0.413em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2217"></mjx-c></mjx-mo></mjx-texatom></mjx-script></mjx-msup></mjx-mstyle></mjx-texatom><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-texatom texclass="ORD"><mjx-texatom texclass="ORD"><mjx-mi class="mjx-ds mjx-b"><mjx-c class="mjx-c2124 TEX-A"></mjx-c></mjx-mi></mjx-texatom></mjx-texatom><mjx-texatom texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2F"></mjx-c></mjx-mo></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-texatom texclass="ORD"><mjx-texatom texclass="ORD"><mjx-mi class="mjx-ds mjx-b"><mjx-c class="mjx-c2124 TEX-A"></mjx-c></mjx-mi></mjx-texatom></mjx-texatom><mjx-msup><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-script style="vertical-align: 0.413em;"><mjx-texatom size="s" texclass="ORD"><mjx-mo class="mjx-n"><mjx-c class="mjx-c2217"></mjx-c></mjx-mo></mjx-texatom></mjx-script></mjx-msup></mjx-mstyle></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mo stretchy="false">(</mo><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><mi mathvariant="double-struck">Z</mi></mrow></mrow><mrow data-mjx-texclass="ORD"><mo>/</mo></mrow><mi>p</mi><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><mi mathvariant="double-struck">Z</mi></mrow></mrow><msup><mo stretchy="false">)</mo><mrow data-mjx-texclass="ORD"><mo>∗</mo></mrow></msup></mstyle></mrow><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mo stretchy="false">(</mo><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><mi mathvariant="double-struck">Z</mi></mrow></mrow><mrow data-mjx-texclass="ORD"><mo>/</mo></mrow><mi>p</mi><mrow data-mjx-texclass="ORD"><mrow data-mjx-texclass="ORD"><mi mathvariant="double-struck">Z</mi></mrow></mrow><msup><mo stretchy="false">)</mo><mrow data-mjx-texclass="ORD"><mo>∗</mo></mrow></msup></mstyle></mrow></math></mjx-assistive-mml></mjx-container></span> の元で、
        位数が <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="5" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>q</mi></mstyle></mrow><mi>q</mi></math></mjx-assistive-mml></mjx-container></span> である値とします。
        この <span class="arithmatex"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="6" style="font-size: 113.1%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D454 TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45D TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D454 TEX-I"></mjx-c></mjx-mi></mjx-mstyle></mjx-texatom></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>p</mi><mo>,</mo><mi>q</mi><mo>,</mo><mi>g</mi></mstyle></mrow><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mi>p</mi><mo>,</mo><mi>q</mi><mo>,</mo><mi>g</mi></mstyle></mrow></math></mjx-assistive-mml></mjx-container></span> の値は公開されているものとします。
    </p>
    ```
=== "表示"

    ディッフィー・ヘルマン鍵共有プロトコルでは、まず大きな素数 ${\displaystyle p}p$ と、
    ${\displaystyle p-1}p-1$ を割り切る大きな素数 ${\displaystyle q}q$ を用意します。
    また、 ${\displaystyle g}g$ を
    ${\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}{\displaystyle ({\mathbb {Z} }/p{\mathbb {Z} })^{\ast }}$ の元で、
    位数が ${\displaystyle q}q$ である値とします。
    この ${\displaystyle p,q,g}{\displaystyle p,q,g}$ の値は公開されているものとします。

---

### 数式ブロック
\$\$で囲んだブロック内にLaTex記法を書きます。

=== "Markdown"

    ```markdown
    $$
    \begin{eqnarray}
        i\hbar\frac{\partial}{\partial t}\psi(x,t)=
        \left(-\frac{\hbar^2}{2m}+V(x)\right)\psi(x,t)
    \end{eqnarray}
    $$
    ```
=== "HTML"

    ```html
    <div class="arithmatex">
        <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" display="true" tabindex="0" ctxtmenu_counter="0" style="font-size: 113.1%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mtable style="min-width: 16.63em;">
            <mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="text-align: right;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-var"><mjx-c class="mjx-c210F"></mjx-c></mjx-mi><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D715"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D715"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D713 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mrow space="4"><mjx-mo class="mjx-s3"><mjx-c class="mjx-c28 TEX-S3"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-msup><mjx-mi class="mjx-var"><mjx-c class="mjx-c210F"></mjx-c></mjx-mi><mjx-script style="vertical-align: 0.363em; margin-left: 0.051em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-s3"><mjx-c class="mjx-c29 TEX-S3"></mjx-c></mjx-mo></mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D713 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mtable displaystyle="true" columnalign="right" columnspacing="" rowspacing="3pt"><mtr><mtd><mi>i</mi><mi data-mjx-alternate="1">ℏ</mi><mfrac><mi>∂</mi><mrow><mi>∂</mi><mi>t</mi></mrow></mfrac><mi>ψ</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>t</mi><mo stretchy="false">)</mo><mo>=</mo><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">(</mo><mo>−</mo><mfrac><msup><mi data-mjx-alternate="1">ℏ</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mo>+</mo><mi>V</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo><mo data-mjx-texclass="CLOSE">)</mo></mrow><mi>ψ</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>t</mi><mo stretchy="false">)</mo></mtd></mtr></mtable></math></mjx-assistive-mml>
        </mjx-container>
    </div>
    ```
=== "表示"

    $$
    \begin{eqnarray}
        i\hbar\frac{\partial}{\partial t}\psi(x,t)=
        \left(-\frac{\hbar^2}{2m}+V(x)\right)\psi(x,t)
    \end{eqnarray}
    $$

---

## 図式
Mermaid記法を使ってフローチャートなどの図式を書けます。

バージョン2.9以降では、[MermaidPrecompile](../extensions/mermaid_precompiler.md)拡張機能の導入するか、
[Mermaid.jsのCDN](https://www.jsdelivr.com/package/npm/mermaid)を`mkdocs.yml`内で`extra_javascript`として読み込む必要があります。
PreCompileを行うにはビルド時に、CDNを読み込むには使用者に、インターネット接続が必要です。

=== "Markdown"

    ````markdown
    ```mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    ```
    ````
=== "HTML"

    ```html
    <div class="arithmatex">
        <mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" display="true" tabindex="0" ctxtmenu_counter="0" style="font-size: 113.1%; position: relative;"><mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mtable style="min-width: 16.63em;">
            <mjx-table><mjx-itable><mjx-mtr><mjx-mtd style="text-align: right;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mi class="mjx-var"><mjx-c class="mjx-c210F"></mjx-c></mjx-mi><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D715"></mjx-c></mjx-mi></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D715"></mjx-c></mjx-mi><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D713 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mrow space="4"><mjx-mo class="mjx-s3"><mjx-c class="mjx-c28 TEX-S3"></mjx-c></mjx-mo><mjx-mo class="mjx-n"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mfrac><mjx-frac type="d"><mjx-num><mjx-nstrut type="d"></mjx-nstrut><mjx-msup><mjx-mi class="mjx-var"><mjx-c class="mjx-c210F"></mjx-c></mjx-mi><mjx-script style="vertical-align: 0.363em; margin-left: 0.051em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c32"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-num><mjx-dbox><mjx-dtable><mjx-line type="d"></mjx-line><mjx-row><mjx-den><mjx-dstrut type="d"></mjx-dstrut><mjx-mrow><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-mrow></mjx-den></mjx-row></mjx-dtable></mjx-dbox></mjx-frac></mjx-mfrac><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D449 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-s3"><mjx-c class="mjx-c29 TEX-S3"></mjx-c></mjx-mo></mjx-mrow><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D713 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D465 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D461 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-tstrut></mjx-tstrut></mjx-mtd></mjx-mtr></mjx-itable></mjx-table></mjx-mtable></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mtable displaystyle="true" columnalign="right" columnspacing="" rowspacing="3pt"><mtr><mtd><mi>i</mi><mi data-mjx-alternate="1">ℏ</mi><mfrac><mi>∂</mi><mrow><mi>∂</mi><mi>t</mi></mrow></mfrac><mi>ψ</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>t</mi><mo stretchy="false">)</mo><mo>=</mo><mrow data-mjx-texclass="INNER"><mo data-mjx-texclass="OPEN">(</mo><mo>−</mo><mfrac><msup><mi data-mjx-alternate="1">ℏ</mi><mn>2</mn></msup><mrow><mn>2</mn><mi>m</mi></mrow></mfrac><mo>+</mo><mi>V</mi><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo><mo data-mjx-texclass="CLOSE">)</mo></mrow><mi>ψ</mi><mo stretchy="false">(</mo><mi>x</mi><mo>,</mo><mi>t</mi><mo stretchy="false">)</mo></mtd></mtr></mtable></math></mjx-assistive-mml>
        </mjx-container>
    </div>
    ```
=== "表示"

    ```mermaid
    graph TD;
        A-->B;
        A-->C;
        B-->D;
        C-->D;
    ```

---

## アコーディオン
細かな情報を折りたたんでおいて、必要に応じてユーザーが参照できるようにできます。


=== "Markdown"

    ```markdown
    ??? "ポラーノの広場"
        あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
        またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。
    ```

=== "HTML"
    ```html
    <div class="accordion" id="accordion-2ca8651f-30ad-4bd1-b5a9-9ef3052b2001">
        <div class="accordion-item">
            <h2 class="accordion-header">
                <button aria-controls="accordion-2ca8651f-30ad-4bd1-b5a9-9ef3052b2001-details" aria-expanded="false" class="accordion-button collapsed" data-bs-target="#accordion-2ca8651f-30ad-4bd1-b5a9-9ef3052b2001-details" data-bs-toggle="collapse" type="button">
                    ポラーノの広場
                </button>
            </h2>
        <div class="accordion-collapse collapse" id="accordion-2ca8651f-30ad-4bd1-b5a9-9ef3052b2001-details" style="">
            <div class="accordion-body">
                <p>
                    あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。
                </p>
            </div>
        </div>
    </div>
    ```

=== "表示"
    
    ??? "ポラーノの広場"
        あのイーハトーヴォのすきとおった風、夏でも底に冷たさをもつ青いそら、うつくしい森で飾られたモリーオ市、郊外のぎらぎらひかる草の波。
        またそのなかでいっしょになったたくさんのひとたち、ファゼーロとロザーロ、羊飼のミーロや、顔の赤いこどもたち、地主のテーモ、山猫博士のボーガント・デストゥパーゴなど、いまこの暗い巨きな石の建物のなかで考えていると、みんなむかし風のなつかしい青い幻燈のように思われます。では、わたくしはいつかの小さなみだしをつけながら、しずかにあの年のイーハトーヴォの五月から十月までを書きつけましょう。

---

## アラート
読者に注意を促したい内容などを、目を引く形で表示できます。
一部のアラートはGFM(GitHub Flavored Markdown)と互換性があります。

=== "Markdown"

    ```markdown
    > [!NOTE] メモ
    > 流し読みしているユーザーにも読んでもらいたい情報を記述します。
    ```

次に、アラート記法で使用できる色とアイコンの一覧を示します。


NOTE
> [!NOTE]
> `NOTE`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
> 
> このアラートはGFMのアラートと互換性があります。

TIP
> [!TIP]
> `TIP`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
> 
> このアラートはGFMのアラートと互換性があります。

IMPORTANT
> [!IMPORTANT]
> `TIP`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
> 
> このアラートはGFMのアラートと互換性があります。

CAUTION
> [!CAUTION]
> `CAUTION`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
> 
> このアラートはGFMのアラートと互換性があります。

WARNING
> [!WARNING]
> `WARNING`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。
> 
> このアラートはGFMのアラートと互換性があります。

ABSTRACT
> [!ABSTRACT]
> `ABSTRACT`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

INFO
> [!INFO]
> `INFO`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

SUCCESS
> [!SUCCESS]
> `SUCCESS`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

QUESTION
> [!QUESTION]
> `QUESTION`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

FAILURE
> [!FAILURE]
> `FAILURE`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

DANGER
> [!DANGER]
> `DANGER`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

BUG
> [!BUG]
> `BUG`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

EXAMPLE
> [!EXAMPLE]
> `EXAMPLE`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

QUOTE
> [!QUOTE]
> `QUOTE`で使用できる装飾です。[リンク](#)は自動的に適切な色になります。

### 記事一覧
` = "" =`で囲い、その中にディレクトリを指定すると、そのディレクトリの記事一覧を出力します。

```markdown title="例"
= "cheatsheet" =\
```

### スニペットの埋め込み
`--8<--`で囲い、その中にファイル名を書き込むと、そのファイルを埋め込みます。
```markdown title="例"
;--8<--
snippet.md
;--8<--
```

### HTMLの埋め込み
HTMLコードは、そのまま記述することで埋め込むことができます。
```html title="例"
<h4>これはHTMLのH4タグです</h4>
```
表示
<h4>これはHTMLのH4タグです</h4>

### 属性の追加
`{: 属性名}`とするとマークダウンで生成される要素に特定の属性を追加することができます。
```markdown title="例"
### この要素にはqueryというIdがつきます {: #query }
```
表示

以下のようなHTMLが生成されます
```html
<h3 id="query">この要素にはqueryというIdがつきます</h3>
```

<script>
function switchPreview(type){
    document.querySelectorAll(`button[data-bs-target^="#__tabbed_"][data-bs-target$="_${type}"]`).forEach((element) => (new bootstrap.Tab(element)).show());
}
document.getElementById('switch-btn-1').addEventListener("click", ()=>switchPreview(1));
document.getElementById('switch-btn-2').addEventListener("click", ()=>switchPreview(2));
document.getElementById('switch-btn-3').addEventListener("click", ()=>switchPreview(3));
</script>