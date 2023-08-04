#!/bin/bash

# For when the minkube cluster is currently running
# so we don't want to fully recreate the cluster,
# just the backend and frontend deployments and services

eval $(minikube -p minikube docker-env)
kubectl delete deployment resume-frontend
kubectl delete deployment resume-backend
kubectl delete service frontend-service
kubectl delete service backend-service
cd backend
docker build --no-cache -t resume-backend .
cd ../frontend
docker build --no-cache -t resume-frontend .
cd ..
kubectl apply -f yaml/backend.yaml
kubectl apply -f yaml/frontend.yaml
