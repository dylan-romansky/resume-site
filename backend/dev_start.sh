#!/bin/bash

#TODO: figure out how to keep track of child pids
#so that I can background the Cockroach instance,
#start the Flask instance, and kill both from the
#same terminal

_term() {
	kill -TERM "$CHILD" 2>/dev/null
	kill -TERM "$PARENT" 2>/dev/null
}

rm -rf cockroach-data
cockroach start-single-node --advertise-addr 'localhost' --insecure #&
#CHILD=$!
#./resume.py &
#PARENT=$!
#wait "$PARENT"
