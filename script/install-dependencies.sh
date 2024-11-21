#!/bin/sh

# Install dependencies for building package
python -m pip install --upgrade pip
pip install pipenv
pip install wheel
pip install 'mkdocs[i18n]'
