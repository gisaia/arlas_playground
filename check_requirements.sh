#!/usr/bin/env sh

git --version     > /dev/null && echo "git ok"     || echo "ERROR: git not installed"
python3 --version > /dev/null && echo "python3 ok" || echo "ERROR: python3 not installed"
