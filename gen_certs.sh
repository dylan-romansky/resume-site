#!/bin/bash

SECRETS="src/secrets"

if [ -d "$SECRETS" ]; then
	rm -rf "$SECRETS"
fi
mkdir "$SECRETS"
cockroach cert create-ca --certs-dir="$SECRETS/certs" --ca-key="$SECRETS/ca_key.ca"

cockroach cert create-client root --certs-dir="$SECRETS/certs" --ca-key="$SECRETS/ca_key.ca"
cockroach cert create-node localhost 127.0.0.1 cockroachdb-public cockroachdb-public.default cockroachdb-public.default.svc.cluster.local *.cockroachdb *.cockroachdb.default *.cockroachdb.default.svc.cluster.local --certs-dir="$SECRETS/certs" --ca-key="$SECRETS/ca_key.ca"
