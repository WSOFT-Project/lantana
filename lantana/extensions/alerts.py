# Lantana Alerts拡張機能
# この拡張機能はAdomonition拡張機能で作成されたアラートをLantanaでも使用できるように調整します
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup

class AlertsExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('alerts', AlertsPostProcessor(self), '>raw_html')


class AlertsPostProcessor(Postprocessor):

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
    return str(soup)

def addClass(soup,selector,ar):
    for tag in soup.select(selector):
        tag.attrs.setdefault('class', list())
        tag["class"] += ar

def replaceClass(soup,selector,remove,add):
    for tag in soup.select(selector):
        tag["class"].remove(remove)
        tag["class"] += add

def makeExtension(*args, **kwargs):
    return AlertsExtension(*args, **kwargs)