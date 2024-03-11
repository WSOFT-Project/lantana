# Lantana CSS調整拡張機能
# この拡張機能は従来theme.jsで行っていたCSS関連の調整を事前に行います
from markdown import Extension
from markdown.postprocessors import Postprocessor
from bs4 import BeautifulSoup
import json
import base64
import zlib
import requests

class MermaidPrecompileExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('mermaid_precompile', MermaidPrecompilePostprocesser(self), '>raw_html')


class MermaidPrecompilePostprocesser(Postprocessor):

    def run(self, html):
        return editRawHtml(html)

def editRawHtml(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.select('.mermaid'):
        mermaid_code = tag.string
        tag.clear()
        tag.insert(0,BeautifulSoup(getSvg(mermaid_code)))

    return str(soup)

def getSvg(code):
    state = {
    'code': code,
    }
    ascii_bytes = json.dumps(state).encode("ascii")
    compressed = zlib.compress(ascii_bytes)
    base64_string = base64.urlsafe_b64encode(compressed).decode('ascii')
    request_url = f'https://mermaid.ink/svg/pako:{base64_string}'
    print(f'[MermaidPreCompiler] Requesting `{request_url}`')
    return requests.get(request_url).text

def makeExtension(*args, **kwargs):
    return MermaidPrecompileExtension(*args, **kwargs)