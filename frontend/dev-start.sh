#!/bin/bash

(cd ..; ./switch-uri.sh local)
if [ $? -ne 0 ]; then
	exit
fi
ng serve --port 8080
