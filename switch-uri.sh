#!/bin/bash

LOC="'http://localhost:5000"
URI_RES="/resume-item/'"
VAR_RES="private uri ="
RES_FIND="${VAR_RES}.*"
SERV_RES="./frontend/src/app/res-it.service.ts"

case "$1" in
	local)
		RES_REPLACE="$VAR_RES $LOC$URI_RES"
		FLAG="-z"
		;;
	k8s)
		RES_REPLACE="$VAR_RES \'$URI_RES"
		FLAG="-n"
		;;
	prod)
		echo "cloud based k8s functionality not implemented yet. exiting"
		exit
		;;
esac

sed -i "s|$RES_FIND|$RES_REPLACE|" $SERV_RES
if [ $FLAG "$(grep localhost $SERV_RES)" ]; then
	echo "error: incorrect uri"
	exit 1
fi
