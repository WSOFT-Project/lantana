#!/usr/bin/env python

from __future__ import annotations

import logging
import os
import shutil
import sys
import time
import textwrap
import traceback
import warnings
import logging
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import click

from mkdocs import __version__, config, utils

config_text = """site_name: MyDocs

docs_dir : 'docs'

extra_javascript:
  - https://polyfill.io/v3/polyfill.min.js?features=es6
  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js

language : ja


theme: lantana

visible_search : true

plugins:
    - search:
        lang : 'ja'
        min_search_length: 2
    - awesome-pages

markdown_extensions:
    - mdx_embedly
    - attr_list
    - pymdownx.highlight:
       anchor_linenums: true
    - admonition
    - pymdownx.arithmatex:
       generic : true
    - md_in_html
    - pymdownx.details
    - pymdownx.superfences:
        custom_fences:
          - name: mermaid
            class: mermaid
            format: !!python/name:pymdownx.superfences.fence_code_format
    - pymdownx.snippets
    - pymdownx.critic
    - pymdownx.caret
    - pymdownx.keys
    - pymdownx.mark
    - pymdownx.tilde
    - pymdownx.emoji:
        emoji_index: !!python/name:materialx.emoji.twemoji
        emoji_generator: !!python/name:materialx.emoji.to_svg
    - mdx_mermaid_precompile
    - pymdownx.tasklist:
        custom_checkbox: true
    - pymdownx.magiclink
    - pymdownx.striphtml
    - mdx_lantana
"""
index_text = """---
title: Hello,World!
summary: Lantana のプロジェクトテンプレートです。ここから、あなただけのサイトを作成しましょう。
---
編集の仕方について詳しく知るには、[Lantanaのサイト](https://lantana.wsoft.ws/)を参照してください。
"""

def cli():
    """
    Lantana - Project documentation with Markdown,flavor MkDocs.
    """


def new(output_dir: str) -> None:
    docs_dir = os.path.join(output_dir, 'docs')
    config_path = os.path.join(output_dir, 'mkdocs.yml')
    index_path = os.path.join(docs_dir, 'index.md')

    if os.path.exists(config_path):
        return

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_text)

    if os.path.exists(index_path):
        return
    if not os.path.exists(docs_dir):
        os.mkdir(docs_dir)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_text)



"""Create a new Lantana project"""

new('.')




if __name__ == '__main__':  # pragma: no cover
    cli()