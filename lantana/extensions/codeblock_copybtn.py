# Lantana CodeBlock CopyBtn拡張機能
# この拡張機能はLantanaのコードブロック中にコピーボタンを追加します
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup

class CodeBlockCopyBtnExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('codeblock_copybtn', CodeBlockCopyBtnProcessor(self), '>raw_html')


class CodeBlockCopyBtnProcessor(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

HIGHLIGHT_TARGET_SELECTOR = 'div.highlight'

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html5lib')
    
    # コードブロックつかうコピーボタンのアイコン定義
    ICON_COPY = 'bi-clipboard'
    ICON_COPY_CHECK = 'bi-clipboard-check'

    # コードブロックがあった場合にtrue
    hasCodeBlock = False
    
    for hlight in soup.select(HIGHLIGHT_TARGET_SELECTOR):
        hasCodeBlock = True
        hlight.insert(0,BeautifulSoup('<button class="btn lantana_codeblock_copybtn position-absolute top-0 end-0"><i class="bi '+ICON_COPY+'"></i></button>','html.parser'))

    # コードブロックがあった場合はスクリプトとかを生成
    if hasCodeBlock:
        addClass(soup,HIGHLIGHT_TARGET_SELECTOR,['position-relative'])
        rawcode = """
        const lantana_codeblock_copybtn_onclick = (btn) => {
            const codeBlock = btn.parentNode.children[btn.parentNode.children.length - 1];
            const icon = btn.querySelector('.bi-clipboard');

            window.getSelection().selectAllChildren(codeBlock);
            document.execCommand('copy');

            icon.classList.add('text-success');
            icon.classList.replace('bi-clipboard', 'bi-clipboard-check');
        };
        document.querySelectorAll('.lantana_codeblock_copybtn').forEach((element) => {
            element.addEventListener('click', () => lantana_codeblock_copybtn_onclick(element));
        });
        """
        rawcode = rawcode.replace("ICON_COPY_CHECK",ICON_COPY_CHECK).replace("ICON_COPY",ICON_COPY)
        soup.append(BeautifulSoup(f"<script>{rawcode}</script>"))

    return str(soup)

def addClass(soup,selector,ar):
    for tag in soup.select(selector):
        tag.attrs.setdefault('class', list())
        tag["class"] += ar

def makeExtension(*args, **kwargs):
    return CodeBlockCopyBtnExtension(*args, **kwargs)
