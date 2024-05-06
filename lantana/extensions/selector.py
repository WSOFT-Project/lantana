# Lantana 拡張機能
# この拡張機能はAdomonition拡張機能で作成されたアラートをLantanaでも使用できるように調整します
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import re

class SelectorExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('Selector', SelectorPostProcessor(self), '>raw_html')

class SelectorPostProcessor(Postprocessor):

    def run(self, html):
        return self.editRawHtml(html)

    def editRawHtml(self,html):
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.select('blockquote > p > .lantana-fence-tmp.selector'):
            dropdown = soup.new_tag('div',attrs={"class": ["dropdown"]})
            button = soup.new_tag('button',attrs=
                                  {"class": ["btn", "btn-secondary", "dropdown-toggle"],
                                   "type":["button"],
                                   "data-bs-toggle":["dropdown"],
                                   "aria-expanded":["false"]})
            button.string = tag["href"]
            if not button.string:
                button.string = "リンクを選択"
            ul = soup.new_tag('ul',attrs={"class": ["dropdown-menu"]})
            tag.parent.wrap(ul)
            for a in tag.parent.findChildren(name="a"):
                a.attrs.setdefault('class', list())
                if "lantana-fence-tmp" in a["class"]:
                    continue
                li = soup.new_tag('li')
                a.attrs.setdefault('class', list())
                a["class"] += ["dropdown-item"]
                a.wrap(li)
            
            ul.wrap(dropdown)
            dropdown.insert(0,button)
            dropdown.parent.unwrap()
        return str(soup)

def makeExtension(*args, **kwargs):
    return SelectorExtension(*args, **kwargs)