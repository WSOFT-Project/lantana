# Cards 拡張機能
from markdown import Extension
from markdown.postprocessors import Postprocessor
import re
import os
import glob
from natsort import natsorted

class CardsExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('cards', CardsPostprocesser(self), '>raw_html')

class Card:
    title=""
    content_dir=""
    summary=""
    date=""
    author=""
    dir_title=""
    order=""

COL_NUM = 3

def get_thumbnail_element(dir, index_filename='index.md',pages_filename='.pages'):
    dir_title=read_property(f'docs/{dir}/{pages_filename}','title')
    filenames = natsorted(glob.glob(f'docs/{dir}/*.md'))
    cards=list()
    for i, filename in enumerate(filenames):
        if not filename.endswith(index_filename):
            card=Card()
            card.title = read_property(filename,'title')
            card.summary = read_property(filename,'summary')
            card.date = read_property(filename,'date')
            card.author = read_property(filename,'author')
            card.order = read_property(filename,'order',filename)
            card.content_dir = filename.lstrip('docs/').rstrip('.md')
            card.dir_title=dir_title
            cards.append(card)
    
    cards = natsorted(cards,key=lambda x:x.order)
    cards.reverse()

    html = '<div class="container-fluid">\n'
    for card in cards:
        html += '    <div class="row mb-3 card">\n'
        html += get_card_element(card.title, card.content_dir,card.summary,card.date,card.author,card.dir_title)
        html += '    </div>\n'
    html += '</div>'
    return html

def read_property(filename,key,default=""):
    """記事や.pagesファイルからプロパティを読みだす関数
    
    filename=ファイル名、key=プロパティの名前
    """
    with open(filename, "r", encoding="utf-8") as f:
        search=re.search(key+'\ *:\ *(.+)*\n*', f.read())
        if search != None:
            return search.group(1)
        else:
            return default

def get_card_element(title, dir,summary,date,author,dir_title):
    card = ''
    card += f'    <div class="card-header">{dir_title}</div>\n'
    card += f'      <div class="card-body">\n'
    card += f'        <h5 class="card-title">{title}</h5>\n'
    card += f'        <p class="card-text">{summary}</p>\n'
    card += f'        <a href="/{dir}/" class="btn btn-primary"><i class="bi bi-file-earmark-richtext"></i>この記事を読む</a>\n'
    card += f'      </div>\n'
    card += f'    <div class="card-footer text-muted">{author}  {date}</div>'

    return card

class CardsPostprocesser(Postprocessor):

    _pattern = re.compile("=\\\".*\\\"=")
    #_pattern = re.compile(r"\[WS[0-9]{5}\]")
    def run(self, html):
        html = re.sub(self._pattern, self._replace_card, html) 
        return html

    def _replace_card(self, match):
        return get_thumbnail_element(match.group(0).lstrip("=(\"").rstrip("\")="))



def makeExtension(*args, **kwargs):
    return CardsExtension(*args, **kwargs)

