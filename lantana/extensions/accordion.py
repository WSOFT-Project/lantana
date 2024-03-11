# Lantana Accordion拡張機能
# この拡張機能はAdomonition拡張機能で作成されたアラートをLantanaでも使用できるように調整します
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import uuid

class AccordionExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('Accordion', AccordionPostProcessor(self), '>raw_html')


class AccordionPostProcessor(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('details:not(.noaccordion)'):
        createAccordion(soup,tag)
    return str(soup)

def createAccordion(soup,tag):
    
    title = tag.summary.text
    isOpen = "open" in tag.attrs and tag.attrs["open"] == "open"
    unique_id = "accordion-"+str(uuid.uuid4())
    item_id = f"{unique_id}-details"
    accordion_box = soup.new_tag("div",id = unique_id)
    accordion_item = soup.new_tag("div")
    accordion_header = soup.new_tag("h2")
    accordion_btn = soup.new_tag("button")
    tag.attrs.setdefault('class', list())
    addClass(accordion_box,tag.attrs["class"])
    addClass(accordion_box,["accordion"])
    addClass(accordion_item,["accordion-item"])
    addClass(accordion_header,["accordion-header"])
    addClass(accordion_btn,["accordion-button"])
    if not isOpen:
        addClass(accordion_btn,["collapsed"])
    accordion_btn.attrs["type"] = "button"
    accordion_btn.attrs["data-bs-toggle"] = "collapse"
    accordion_btn.attrs["aria-controls"] = item_id
    accordion_btn.attrs["data-bs-target"] = f"#{item_id}"
    accordion_btn.attrs["aria-expanded"] = str(isOpen)
    accordion_btn.append(title)
    accordion_header.append(accordion_btn)
    accordion_item.append(accordion_header)
    accordion_inner = soup.new_tag("div", id = item_id)
    addClass(accordion_inner,["accordion-collapse", "collapse"])
    if isOpen:
        addClass(accordion_inner,["show"])
    accordion_body = soup.new_tag("div")
    addClass(accordion_body,["accordion-body"])
    
    loopCount = 0
    for child in tag.children:
        if loopCount > 2:
            accordion_body.append(child)
        loopCount += 1
    accordion_inner.append(accordion_body)
    accordion_item.append(accordion_inner)
    accordion_box.append(accordion_item)
    tag.insert_before(accordion_box)
    tag.extract()
    

def addClass(tag,ar):
    tag.attrs.setdefault('class', list())
    tag["class"] += ar

def makeExtension(*args, **kwargs):
    return AccordionExtension(*args, **kwargs)