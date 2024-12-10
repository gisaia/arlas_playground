#!/bin/sh -e

## CREATE TARGET DIRECTORY ##
rm -rf target/generated-docs
mkdir target/generated-docs

cp -r docs/docs/* target/generated-docs
