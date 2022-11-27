#The MIT License (MIT)
#
#Copyright (c) 2015 yymm
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# WSOFTDownloadCenter ダウンロード番号自動変換拡張機能
# この拡張機能は「[WS00000]」のようなダウンロード番号を自動的にリンクへと置き換えます
from markdown import Extension
from markdown.postprocessors import Postprocessor
import re

class WSIDExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('wsid', WSIDPostprocesser(self), '>raw_html')


class WSIDPostprocesser(Postprocessor):

    _pattern = re.compile(r"\[WS[0-9]{5}\]")

    def run(self, html):
        html = re.sub(self._pattern, self._replace_wsid, html) 
        return html

    def _replace_wsid(self, match):
        url = match.group(0).lstrip("[WS").rstrip("]")
        title = "WSOFTダウンロードセンターからダウンロード"
        return """
<a href="https://download.wsoft.ws/WS{0}" title="{1}">WS{0}</a>
""".format(url, title)


def makeExtension(*args, **kwargs):
    return WSIDExtension(*args, **kwargs)