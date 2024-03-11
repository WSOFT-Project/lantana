# Lantana Link OpenNewTab拡張機能
# この拡張機能は外部サイトへのリンクを新しいタブで開きます
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup

class OpenNewTabExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('link_opennewtab', OpenNewTabPostprocesser(self), '>raw_html')


class OpenNewTabPostprocesser(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('a[href*="://"]:not(.unnewtab)'):
        tag.attrs["target"] = ['_blank']
        tag.attrs["rel"] = ['noopener" ,"noreferrer']

    return str(soup)

def makeExtension(*args, **kwargs):
    return OpenNewTabExtension(*args, **kwargs)