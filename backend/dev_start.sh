#!/bin/bash

#TODO: figure out how to keep track of child pids
#so that I can background the Cockroach instance,
#start the Flask instance, and kill both from the
#same terminal

_term() {
	kill -TERM "$DB_PID" 2>/dev/null
	kill -TERM "$FLASK_PID" 2>/dev/null
}

rm -rf cockroach-data
cockroach start-single-node --advertise-addr 'localhost' --insecure &
DB_PID=$!
./resume.py &
FLASK_PID=$!
echo $DB_PID
echo $FLASK_PID
wait $FLASK_PID
_term
