#!/bin/bash

if [ -d secrets ]; then
	rm -rf secrets
fi
mkdir secrets
cockroach cert create-ca --certs-dir='./secrets/certs' --ca-key='./secrets/ca_key.ca'
