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

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html5lib')
    
    # コードブロックつかうコピーボタンのアイコン定義
    ICON_COPY = 'bi-clipboard'
    ICON_COPY_CHECK = 'bi-clipboard-check'

    # コードブロックがあった場合にtrue
    hasCodeBlock = False
    
    for hlight in soup.select('.highlight'):
        hasCodeBlock = True
        hlight.insert(0,BeautifulSoup('<button class="btn copybtn position-absolute top-0 end-0"><i class="bi '+ICON_COPY+'"></i></button>','html.parser'))

    # コードブロックがあった場合はスクリプトとかを生成
    if hasCodeBlock:
        addClass(soup,'.highlight',['position-relative'])
        rawcode = """$('.copybtn').click(function (){
    const selection = window.getSelection();
    const code = this.parentNode;
    selection.selectAllChildren(code.children[code.children.length-1]);
    document.execCommand('copy');
    this.querySelector('.ICON_COPY').classList.add('text-success');
    this.querySelector('.ICON_COPY').classList.replace('ICON_COPY','ICON_COPY_CHECK');
});"""
        rawcode = rawcode.replace("ICON_COPY_CHECK",ICON_COPY_CHECK).replace("ICON_COPY",ICON_COPY)
        soup.append(BeautifulSoup(f"<script>{rawcode}</script>"))

    return str(soup)

def addClass(soup,selector,ar):
    for tag in soup.select(selector):
        tag.attrs.setdefault('class', list())
        tag["class"] += ar

def makeExtension(*args, **kwargs):
    return CodeBlockCopyBtnExtension(*args, **kwargs)