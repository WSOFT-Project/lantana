# Lantana CSS調整拡張機能
# この拡張機能は従来theme.jsで行っていたCSS関連の調整を事前に行います
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import re

class LantanaExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('lantana-Pre',LantanaPreProcessor(self),'>html_block')
        md.postprocessors.add('lantana-Post', LantanaPostprocesser(self), '>raw_html')

class LantanaPreProcessor(Preprocessor):

    _pattern = re.compile(r"> \[\!(.*)] *(.*)")

    def run(self, lines: list):
        for i in range(len(lines)):
            matches = re.findall(self._pattern,lines[i])
            if len(matches) > 0:
                lines[i] = f'> []({matches[0][1].lower()}){{: .lantana-fence-tmp .{matches[0][0].lower()} }}'
        return lines

class LantanaPostprocesser(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Bootstrapクラス追加処理
    addClass(soup,'table:not(.disable-lantana)',['table'])
    addClass(soup,'img:not(.disable-lantana)',['img-fluid'])
    addClass(soup,'blockquote:not(.disable-lantana)',['blockquote'])

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