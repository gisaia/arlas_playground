#!/usr/bin/env sh

csvjson --version > /dev/null && echo "csvjson ok" || echo "ERROR: csvjson not installed"
git --version     > /dev/null && echo "git ok"     || echo "ERROR: git not installed"
python3 --version > /dev/null && echo "python3 ok" || echo "ERROR: python3 not installed"
curl --version    > /dev/null && echo "curl ok"    || echo "ERROR: curl not installed"
jq --version      > /dev/null && echo "jq ok"      || echo "ERROR: jq not installed"
