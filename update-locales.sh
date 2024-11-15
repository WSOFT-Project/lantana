#!/bin/sh
python3 -m venv venv
source venv/bin/activate
pip3 install 'mkdocs[i18n]'

pybabel extract -F babel.cfg -o lantana/messages.pot --input-dirs=lantana
pybabel update --input-file lantana/messages.pot --output-dir lantana/locales -l en
pybabel update --input-file lantana/messages.pot --output-dir lantana/locales -l ja
