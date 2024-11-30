#!/bin/sh

# Build i18n support
pybabel compile --statistics --directory lantana/locales -l en
pybabel compile --statistics --directory lantana/locales -l ja

# Build package
python3 setup.py sdist --formats=zip
