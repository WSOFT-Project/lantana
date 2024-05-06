# Lantana 拡張機能
# この拡張機能はAdomonition拡張機能で作成されたアラートをLantanaでも使用できるように調整します
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import re

class Alerts2Extension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('Alerts2-Post', Alerts2PostProcessor(self), '>raw_html')

    
class Alerts2PostProcessor(Postprocessor):

    def run(self, html):
        return self.editRawHtml(html)

    def editRawHtml(self,html):
        soup = BeautifulSoup(html, 'html.parser')

        for tag in soup.select('blockquote > p > .lantana-fence-tmp'):
            alert_tag = soup.new_tag('div')
            alert_tag.attrs.setdefault('class', list())
            alert_tag["class"] += ['alert']
            tagname = ""
            iconPoint = ""
            processed = False
            for name in tag["class"]:
                tagname = name
                if name == "note":
                    iconPoint = "bi-check2"
                    alert_tag["class"] += ['alert-primary']
                    processed = True
                if name == "question":
                    iconPoint = "bi-question-circle"
                    alert_tag["class"] += ['alert-secondary']
                    processed = True
                if name == "abstract":
                    iconPoint = "bi-journal-text"
                    alert_tag["class"] += ['alert-secondary']
                    processed = True
                if name == "info":
                    iconPoint = "bi-info-circle"
                    alert_tag["class"] += ['alert-info']
                    processed = True
                if name == "important":
                    iconPoint = "bi-exclamation-circle"
                    alert_tag["class"] += ['alert-info']
                    processed = True
                if name == "tip":
                    iconPoint = "bi-lightbulb"
                    alert_tag["class"] += ['alert-warning']
                    processed = True
                if name == "warning":
                    iconPoint = "bi-exclamation-triangle"
                    alert_tag["class"] += ['alert-warning']
                    processed = True
                if name == "bug":
                    iconPoint = "bi-bug"
                    alert_tag["class"] += ['alert-warning']
                    processed = True
                if name == "failure":
                    iconPoint = "bi-window-x"
                    alert_tag["class"] += ['alert-danger']
                    processed = True
                if name == "danger":
                    iconPoint = "bi-radioactive"
                    alert_tag["class"] += ['alert-danger']
                    processed = True
                if name == "caution":
                    iconPoint = "bi-exclamation-octagon"
                    alert_tag["class"] += ['alert-danger']
                    processed = True
                if name == "success":
                    iconPoint = "bi-check-all"
                    alert_tag["class"] += ['alert-success']
                    processed = True
                if name == "example":
                    iconPoint = "bi-window-sidebar"
                    alert_tag["class"] += ['alert-dark']
                    processed = True
                if name == "quote":
                    iconPoint = "bi-chat-right-quote"
                    alert_tag["class"] += ['alert-light']
                    processed = True
            if not processed:
                continue
            tag.parent.parent.wrap(alert_tag)
            tag.parent.parent.unwrap()
            if not tag["href"]:
                tag["href"] = tagname.capitalize()
            alert_heading_tag = soup.new_tag('p')
            alert_heading_icon_tag = soup.new_tag('i')
            alert_heading_icon_tag.attrs["class"] = ["bi",iconPoint]
            alert_heading_tag.string = ' ' + tag["href"]
            alert_heading_tag.insert(0,alert_heading_icon_tag)
            alert_heading_tag.attrs["class"] = ["alert-heading"]
            alert_tag.insert(0,alert_heading_tag)
            tag.extract()
        addClass(soup,'.alert a',['alert-link'])
        return str(soup)

def addClass(soup,selector,ar):
        for tag in soup.select(selector):
            tag.attrs.setdefault('class', list())
            tag["class"] += ar
def makeExtension(*args, **kwargs):
    return Alerts2Extension(*args, **kwargs)