#!/bin/bash

if [ "$#" -ne 1 ];
then
    echo "Usage: visualize-yw.sh ./path/to/open-refine-operation-history.json"
    exit 1
fi

# Ensure that or2yw is installed
if ! command -v or2yw &> /dev/null
then
    echo "or2yw is not installed! (See: https://pypi.org/project/or2ywtool/)"
    exit 1
fi

or2yw -i $1 \
      -o openrefineworkflow.png \
      -ot png \
      -title "OpenRefine"