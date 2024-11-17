#!/bin/bash
pip install 'mkdocs[i18n]'

# Building i18n support
pybabel compile --statistics --directory lantana/locales -l en
pybabel compile --statistics --directory lantana/locales -l ja

# Install this package
pip install .

# And i18n support for site
pip install mkdocs-static-i18n==1.2.3

# Build site
mkdocs build
