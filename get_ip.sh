#!/bin/bash

# The following command no longer works properly,
# however I have kept it here for my notes
#minikube service resume-service --url

# This command exposes the backend service to my
# local machine. This way I can test and verify
# the backend's behaviour in the cluster using
# a known-good frontend instance running on my
# local machine

kubectl port-forward service/frontend-service 5000:5000
