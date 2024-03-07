# Lantana CSS調整拡張機能
# この拡張機能は従来theme.jsで行っていたCSS関連の調整を事前に行います
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup

class LantanaExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('lantana', LantanaPostprocesser(self), '>raw_html')


class LantanaPostprocesser(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    # MaterialのAdmonitionタイトルをAlertタイトルに置換
    replaceClass(soup,'.admonition .admonition-title','admonition-title',['alert-heading'])

    # MaterialのAdmonition色をAlert色に置換
    replaceClass(soup,'.admonition.note','admonition',['alert','alert-primary'])
    replaceClass(soup,'.admonition.abstract','admonition',['alert','alert-secondary'])
    replaceClass(soup,'.admonition.info','admonition',['alert','alert-info'])
    replaceClass(soup,'.admonition.tip','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.success','admonition',['alert','alert-success'])
    replaceClass(soup,'.admonition.question','admonition',['alert','alert-secondary'])
    replaceClass(soup,'.admonition.warning','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.failure','admonition',['alert','alert-danger'])
    replaceClass(soup,'.admonition.danger','admonition',['alert','alert-danger'])
    replaceClass(soup,'.admonition.bug','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.example','admonition',['alert','alert-dark'])
    replaceClass(soup,'.admonition.quote','admonition',['alert','alert-light'])

    # Bootstrapのalert-linkを適用
    addClass(soup,'.alert a',['alert-link'])

    # Bootstrapクラス追加処理
    addClass(soup,'table:not(.disable-lantana)',['table'])
    addClass(soup,'img:not(.disable-lantana)',['img-fluid'])
    addClass(soup,'blockquote:not(.disable-lantana)',['blockquote'])

    # コードブロックにコピーボタンを追加
    ICON_COPY = 'bi-clipboard'

    addClass(soup,'.highlight',['position-relative'])
    for hlight in soup.select('.highlight'):
        hlight.insert(0,BeautifulSoup('<button class="btn copybtn position-absolute top-0 end-0"><i class="bi '+ICON_COPY+'"></i></button>'))
    return str(soup)

def addClass(soup,selector,ar):
    for tag in soup.select(selector):
        tag.attrs.setdefault('class', list())
        tag["class"] += ar

def removeClass(soup,selector,ar):
    for tag in soup.select(selector):
        tag["class"].remove(ar)

def replaceClass(soup,selector,remove,add):
    for tag in soup.select(selector):
        tag["class"].remove(remove)
        tag["class"] += add

def makeExtension(*args, **kwargs):
    return LantanaExtension(*args, **kwargs)