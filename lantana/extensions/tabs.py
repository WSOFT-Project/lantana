# Lantana Tabs拡張機能
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup

class TabsExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('tabs', TabsPostProcessor(self), '>raw_html')

class TabsPostProcessor(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('.tabbed-set.tabbed-alternate'):
        # デバッグのために、古いHTMLの後に新しいHTMLを挿入する
        # tag.insert_after(createTab(soup,tag))
        tag.replace_with(createTab(soup,tag))
    return str(soup)

def createTab(soup, tag):
    outer = soup.new_tag('div')
    id_list, selectedMap = getId(soup, tag)
    nav_tag = createTabButtons(soup, tag, id_list, selectedMap)
    outer.append(nav_tag)
    content_tag = createTabContents(soup, tag, id_list, selectedMap)
    outer.append(content_tag)
    return outer

# navを作る関数
def createTabButtons(soup, tag, id_list, selectedMap):
    nav_tag = soup.new_tag('nav')
    nav_div_tag = soup.new_tag('div')
    nav_tag = soup.new_tag('nav')
    nav_div_tag = soup.new_tag('div')
    nav_div_tag.attrs.setdefault('class', ['nav','nav-underline'])
    nav_div_tag.attrs.setdefault('role', ['tablist'])
    for label in tag.select('.tabbed-labels > label'):
        tab_btn = createButton(soup, label['for'], selectedMap[label['for']], label.string)
        nav_div_tag.append(tab_btn)
    nav_tag.append(nav_div_tag)
    return nav_tag

# contentを作る関数
def createTabContents(soup, tag, id_list, selectedMap):
    div_tag = soup.new_tag('div', attrs={'class':['tab-content', 'border-top']})
    ind = 0
    for block in tag.select('.tabbed-content > .tabbed-block'):
        content_tag = createContent(soup, id_list[ind], selectedMap[id_list[ind]], block)
        div_tag.append(content_tag)
        ind += 1
    return div_tag

def getId(soup, tag):
    id_list = list()
    selected_map = dict()
    for label in tag.select('input'):
        label.attrs.setdefault('checked', 'false')
        if 'id' in label.attrs:
            id_list.append(label['id'])
            selected_map[label['id']] = label['checked'] == 'checked'
    return id_list, selected_map

def createButton(soup, target_id: str, selected: bool, content: str):
    button_tag = soup.new_tag('button')
    button_tag.attrs.setdefault('class', ['nav-link'])
    if selected:
        button_tag['class'].append('active')
    button_tag.attrs.setdefault('aria-controls', target_id)
    button_tag.attrs.setdefault('data-selected', 'true' if selected else 'false')
    button_tag.attrs.setdefault('data-bs-target', f'#{target_id}')
    button_tag.attrs.setdefault('data-bs-toggle', 'tab')
    button_tag.attrs.setdefault('role', 'tab')
    button_tag.attrs.setdefault('type', 'button')
    button_tag.string = content
    return button_tag

def createContent(soup, target_id: str, selected: bool, content):
    div_tag = soup.new_tag('div', id=target_id, attrs={ 'class': ['tab-pane'],
                                                               'role': 'tabpanel', 'tabindex': '0'})
    div_tag.append(content)
    if selected:
        div_tag['class'] += ['show', 'active']
    return div_tag

def makeExtension(*args, **kwargs):
    return TabsExtension(*args, **kwargs)