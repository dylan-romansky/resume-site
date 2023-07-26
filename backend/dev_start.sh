#!/bin/bash

#TODO: figure out how to wait for cockroachdb to start

_term() {
	kill -TERM "$DB_PID" 2>/dev/null
	kill -TERM "$FLASK_PID" 2>/dev/null
}

rm -rf cockroach-data
cockroach start-single-node --advertise-addr 'localhost' --insecure > /dev/null 2>&1 &
DB_PID=$!
sleep 5
./.env/bin/python ./resume.py
#./.env/bin/gunicorn --bind 0.0.0.0:5000 resume:app
_term
