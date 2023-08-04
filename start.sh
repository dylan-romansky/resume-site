#!/bin/bash

minikube start
kubectl exec cockroachdb-0 -- /cockroach/cockroachinit --certs-dir='/cockroach/cockroach-certs'
