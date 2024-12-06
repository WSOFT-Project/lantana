# Lantana Tabs拡張機能
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import uuid

class TabsExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('tabs', TabsPostProcessor(self), '>raw_html')

class TabsPostProcessor(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('.tabbed-set.tabbed-alternate'):
        createAccordion(soup,tag)
    return str(soup)

def createAccordion(soup, tag) -> str:
    print(tag.prettify())
    input()
    pass

def makeExtension(*args, **kwargs):
    return TabsExtension(*args, **kwargs)