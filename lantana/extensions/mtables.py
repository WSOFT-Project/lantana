# MetaTable 拡張機能
from markdown import Extension
from markdown.postprocessors import Postprocessor
import re
import os
import glob
from natsort import natsorted

class MetaTablesExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('mtables', MetaTablesPostprocesser(self), '>raw_html')

class Card:
    title=""
    content_dir=""
    summary=""
    date=""
    author=""
    dir_title=""
    order=""

COL_NUM = 3

def get_thumbnail_element(dir, options, index_filename='index.md',pages_filename='.pages'):
    dir_title=read_property(f'docs/{dir}/{pages_filename}','title')
    filenames = natsorted(glob.glob(f'docs/{dir}/*.md'))
    contain_index = "include-index" in options
    contain_subdir = "include-subdir" in options
    meta_type = options[0]
    style_lite = "style-lite" in options
    smart_jump = "smart-jump" in options
    cards=list()
    for i, filename in enumerate(filenames):
            if read_property(filename, 'mt_type') == meta_type:
                overloads = count_property(filename, 'mt_title')
                if overloads <= 0:
                    overloads = 1
                for k in range(overloads):
                    card=Card()
                    card.title = read_property(filename,'mt_title', read_property(filename, 'title'), k)
                    card.summary = read_property(filename,'mt_summary', read_property(filename, 'summary'), k)
                    card.date = read_property(filename,'mt_date', read_property(filename, 'date'), k)
                    card.order = read_property(filename,'mt_order', read_property(filename, 'order'), k) 
                    card.content_dir = remove_filename(filename)
                    card.dir_title=dir_title
                    if smart_jump:
                        card.content_dir += f'#{convert_to_id(card.title)}'
                    if not filename.endswith(index_filename):
                        cards.append(card)
                    elif contain_index:
                        card.order = -1
                        cards.insert(0,card)

    # 指定されている場合はサブディレクトリも見る
    if contain_subdir:
        filenames = natsorted(glob.glob(f'docs/{dir}/*/index.md'))
        for i, filename in enumerate(filenames):
                if read_property(filename, 'mt_type') == meta_type:
                    overloads = count_property(filename, 'mt_title')
                    if overloads <= 0:
                        overloads = 1
                    for k in range(overloads):
                        card=Card()
                        card.title = read_property(filename,'mt_title', read_property(filename, 'title'), k)
                        card.summary = read_property(filename,'mt_summary', read_property(filename, 'summary'), k)
                        card.date = read_property(filename,'mt_date', read_property(filename, 'date'), k)
                        card.order = read_property(filename,'mt_order', read_property(filename, 'order'), k)
                        card.content_dir = remove_filename(filename)
                        card.dir_title=dir_title
                        cards.append(card)

                        if smart_jump:
                            card.content_dir += f'#{convert_to_id(card.title)}'
    
    cards = natsorted(cards,key=lambda x:x.order)

    if style_lite:
        html = '<ul>'

        for card in cards:
            html += f'<li><a href="/{card.content_dir}/">{card.title}</a></li>'

        html += '</ul>'
    else:
        html = '<table class="table"><thead><th></th><th></th></thead><tbody>\n'
        for card in cards:
            html += '<tr>\n'
            html += f'<td><a href="/{card.content_dir}">{card.title}{card.order}</a></td>'
            html += f'<td>{card.summary}</td>'
            html += '</tr>'
        html += '</tbody></table>'
    return html

def convert_to_id(name) -> str:
    name = name.lower()
    name = name.replace(' ', '-')
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace(',', '')
    return name

def remove_filename(filename):
    """
        docs/***.mdのようなファイル名を**のみに切り出す関数
    """
    filename = filename.replace("docs/","",1)
    filename=filename[::-1].replace("dm.","",1)
    return filename[::-1]

def count_property(filename,key):
    """記事や.pagesファイルにプロパティがいくつあるかを調べる関数
    
    filename=ファイル名、key=プロパティの名前
    """
    with open(filename, "r", encoding="utf-8") as f:
        search=re.findall(key+'\ *:\ *(.+)*\n*', f.read())
        if search != None:
            return len(search)
        else:
            return 0


def read_property(filename,key,default="",index=0):
    """記事や.pagesファイルからプロパティを読みだす関数
    
    filename=ファイル名、key=プロパティの名前
    """
    with open(filename, "r", encoding="utf-8") as f:
        search=re.findall(key+'\ *:\ *(.+)*\n*', f.read())
        if search != None and len(search) > 0:
            if len(search) > index:
                return search[index]
            else:
                return search[index]
        else:
            return default


class MetaTablesPostprocesser(Postprocessor):
    _pattern = re.compile("=\!\\\"(.*)\\\"(\\|\\[(.*)\\])?\!=")
    #_pattern = re.compile(r"\[WS[0-9]{5}\]")
    def run(self, html):
        html = re.sub(self._pattern, self._replace_card, html) 
        return html

    def _replace_card(self, match):
        return get_thumbnail_element(match.group(1),(match.group(3) or "").split(','))



def makeExtension(*args, **kwargs):
    return CardsExtension(*args, **kwargs)

