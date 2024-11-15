#!/bin/sh
python3 -m venv venv
source venv/bin/activate
pip3 install 'mkdocs[i18n]'

# Build i18n support
pybabel compile --statistics --directory lantana/locales -l en
pybabel compile --statistics --directory lantana/locales -l ja

# Build package
python3 setup.py sdist --formats=zip