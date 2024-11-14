#!/bin/bash
source venv/bin/activate
pip3 install -e .
mkdocs serve --watch-theme