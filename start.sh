#!/bin/bash

# This script serves as a means of deploying and initializing
# the entire application so I don't have to go through this
# process every time

SECRETS='backend/secrets'
minikube delete --all
minikube start
minikube addons enable ingress

eval $(minikube -p minikube docker-env)
echo "cleaning up docker environment"
docker system prune --force
echo "removing old certs"
rm -rf $SECRETS
echo "generating new certs"
./gen_certs.sh
cd backend
docker rmi -f "$(docker image ls | grep resume | cut -d: -f2)"
docker build --no-cache -t resume-backend .
cd ../frontend
docker build --no-cache -t resume-frontend .
cd ..

kubectl create secret generic cockroachdb.client.root --from-file="$SECRETS"/certs/
kubectl create secret generic cockroachdb.node --from-file="$SECRETS"/certs

kubectl apply -f yaml/cockroachdb-statefulset.yaml

while [ -z "$(kubectl get pods | grep Running)" ]; do
	sleep 1
done

#DB_INIT="$(cat db_init/schema.sql)"
kubectl exec cockroachdb-0  -- /cockroach/cockroach init --certs-dir='/cockroach/cockroach-certs'
#kubectl exec cockroachdb-0  -- /cockroach/cockroach sql --certs-dir='/cockroach/cockroach-certs' -e "$DB_INIT"

kubectl apply -f yaml/backend.yaml
kubectl apply -f yaml/frontend.yaml

minikube tunnel
