#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install 'mkdocs[i18n]'

# Building i18n support
pybabel compile --statistics --directory lantana/locales -l en
pybabel compile --statistics --directory lantana/locales -l ja

# Install this package in editable mode
pip install -e .

# And i18n support for site
pip install mkdocs-static-i18n==1.2.3

mkdocs serve --watch-theme