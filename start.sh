#!/bin/bash

SECRETS='src/secrets'
minikube delete
minikube start
minikube addons enable ingress

eval $(minikube -p minikube docker-env)

cd src
docker rmi -f "$(docker image ls | grep resume | cut -d: -f2)"
docker build --no-cache -t resume .
cd ..

kubectl create secret generic cockroachdb.client.root --from-file="$SECRETS"/certs/
kubectl create secret generic cockroachdb.node --from-file="$SECRETS"/certs

kubectl apply -f yaml/cockroachdb-statefulset.yaml

while [ -z "$(kubectl get pods | grep Running)" ]; do
	sleep 1
done

DB_INIT="$(cat db_init/schema.sql)"
kubectl exec cockroachdb-0  -- /cockroach/cockroach init --certs-dir='/cockroach/cockroach-certs'
kubectl exec cockroachdb-0  -- /cockroach/cockroach sql --certs-dir='/cockroach/cockroach-certs' -e "$DB_INIT"

kubectl apply -f yaml/resume.yaml

minikube tunnel
