#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip3 install 'mkdocs[i18n]'

# Building i18n support
pybabel compile --statistics --directory lantana/locales -l en
pybabel compile --statistics --directory lantana/locales -l ja

pip3 install -e .
mkdocs serve --watch-theme
