#!/bin/bash

./switch-uri.sh "k8s-dev"
if [ $? -ne 0 ]; then
	exit
fi
minikube stop
minikube start
eval $(minikube -p minikube docker-env)

while [ -z "$(kubectl get pods | grep Running)" ]; do
	sleep 1
done

echo "$(kubectl get pods)"
kubectl exec 'cockroachdb-0' -- /cockroach/cockroach init --certs-dir='/cockroach/cockroach-certs'
./reapply.sh

minikube tunnel
