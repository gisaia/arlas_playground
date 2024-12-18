#!/bin/sh -e

## CREATE TARGET DIRECTORY ##
mkdir -p target/generated-docs
rm -rf target/generated-docs/*

cp -r docs/docs/* target/generated-docs
