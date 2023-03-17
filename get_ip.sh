#!/bin/bash

# The command to get the ip address that minikube
# exposed for outside traffic

minikube service resume-service --url
