#!/bin/bash

SECRETS='src/secrets'
minikube delete
minikube start

kubectl create secret generic cockroachdb.client.root --from-file="$SECRETS"/certs/
kubectl create secret generic cockroachdb.node --from-file="$SECRETS"/certs

kubectl apply -f cockroachdb-statefulset.yaml
#kubectl exec -it cockroachdb-0 -- /cockroach/cockroach init --certs-dir=/cockroach/cockroach-certs
#kubectl apply -f cluster-init.yaml
