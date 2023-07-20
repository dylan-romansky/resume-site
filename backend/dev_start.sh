#!/bin/bash

#TODO: figure out how to wait for cockroachdb to start

_term() {
	kill -TERM "$DB_PID" 2>/dev/null
	kill -TERM "$FLASK_PID" 2>/dev/null
}

rm -rf cockroach-data
cockroach start-single-node --advertise-addr 'localhost' --insecure &
DB_PID=$!
./bin/python ./resume.py &
FLASK_PID=$!
echo $DB_PID
echo $FLASK_PID
wait $FLASK_PID
_term
