#!/bin/bash

# This makes sure the uris are consistently set to
# localhost in the code on the actual repo
./switch-uri.sh local
git "$@"
