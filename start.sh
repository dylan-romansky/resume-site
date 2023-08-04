#!/bin/bash

minikube stop
minikube start
eval $(minikube -p minikube docker-env)
kubectl delete deployment resume-frontend
kubectl delete deployment resume-backend

while [ -z "$(kubectl get pods | grep Running)" ]; do
	sleep 1
done

echo "$(kubectl get pods)"
kubectl exec 'cockroachdb-0' -- /cockroach/cockroach init --certs-dir='/cockroach/cockroach-certs'
kubectl apply -f yaml/backend.yaml
kubectl apply -f yaml/frontend.yaml

minikube tunnel
