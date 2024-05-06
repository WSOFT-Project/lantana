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

    # Alertにアイコンを適用
    addIcon(soup,'.admonition.note > .alert-heading','bi-check2')
    addIcon(soup,'.admonition.abstract > .alert-heading','bi-journal-text')
    addIcon(soup,'.admonition.info > .alert-heading','bi-info-circle')
    addIcon(soup,'.admonition.important > .alert-heading','bi-exclamation-circle')
    addIcon(soup,'.admonition.tip > .alert-heading','bi-lightbulb')
    addIcon(soup,'.admonition.success > .alert-heading','bi-check-all')
    addIcon(soup,'.admonition.question > .alert-heading','bi-question-circle')
    addIcon(soup,'.admonition.warning > .alert-heading','bi-exclamation-triangle')
    addIcon(soup,'.admonition.failure > .alert-heading','bi-window-x')
    addIcon(soup,'.admonition.danger > .alert-heading','bi-radioactive')
    addIcon(soup,'.admonition.caution > .alert-heading','bi-exclamation-octagon')
    addIcon(soup,'.admonition.bug > .alert-heading','bi-bug')
    addIcon(soup,'.admonition.example > .alert-heading','bi-window-sidebar')
    addIcon(soup,'.admonition.quote > .alert-heading','bi-chat-right-quote')

    # MaterialのAdmonition色をAlert色に置換
    replaceClass(soup,'.admonition.note','admonition',['alert','alert-primary'])
    replaceClass(soup,'.admonition.abstract','admonition',['alert','alert-secondary'])
    replaceClass(soup,'.admonition.info','admonition',['alert','alert-info'])
    replaceClass(soup,'.admonition.important','admonition',['alert','alert-info'])
    replaceClass(soup,'.admonition.tip','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.success','admonition',['alert','alert-success'])
    replaceClass(soup,'.admonition.question','admonition',['alert','alert-secondary'])
    replaceClass(soup,'.admonition.warning','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.failure','admonition',['alert','alert-danger'])
    replaceClass(soup,'.admonition.caution','admonition',['alert','alert-danger'])
    replaceClass(soup,'.admonition.danger','admonition',['alert','alert-danger'])
    replaceClass(soup,'.admonition.bug','admonition',['alert','alert-warning'])
    replaceClass(soup,'.admonition.example','admonition',['alert','alert-dark'])
    replaceClass(soup,'.admonition.quote','admonition',['alert','alert-light'])

    # Bootstrapのalert-linkを適用
    addClass(soup,'.alert a',['alert-link'])
    return str(soup)

def addIcon(soup,selector,iconPoint):
    for tag in soup.select(selector):
            alert_heading_icon_tag = soup.new_tag('i')
            alert_heading_icon_tag.attrs["class"] = ["bi",iconPoint]
            if tag.string:
                tag.string = ' ' + tag.string
            tag.insert(0,alert_heading_icon_tag)


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