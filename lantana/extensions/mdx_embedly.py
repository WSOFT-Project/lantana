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

from markdown import Extension
from markdown.postprocessors import Postprocessor
import re


class EmbedlyExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('embed', EmbedlyPostprocesser(self), '>raw_html')


class EmbedlyPostprocesser(Postprocessor):

    _pattern = re.compile(r"(embed(s)?(://[\w:;/.?%#&=+-]+))")

    def run(self, html):
        html = re.sub(self._pattern, self._replace_embed, html) 
        return html

    def _replace_embed(self, match):
        url = match.group(1).replace("embed","http",1)
        title = "embed.ly"
        return """
<a class="embedly-card" href="{0}">{1}</a>
<script async src="https://cdn.embedly.com/widgets/platform.js" charset="UTF-8"></script>
""".format(url, title)


def makeExtension(*args, **kwargs):
    return EmbedlyExtension(*args, **kwargs)