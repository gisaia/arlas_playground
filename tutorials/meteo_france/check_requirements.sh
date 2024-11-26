#!/usr/bin/env sh

curl --version    > /dev/null && echo "curl ok"    || echo "ERROR: curl not installed"
jq --version      > /dev/null && echo "jq ok"      || echo "ERROR: jq not installed"
csvjson --version > /dev/null && echo "csvjson ok" || echo "ERROR: csvjson not installed"
