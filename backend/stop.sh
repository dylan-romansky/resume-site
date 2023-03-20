#!/bin/bash

# A quick and easy shutdown and cleanup for the
# application when deployed via Docker

docker container rm -f "$(docker container ls | grep resume | awk '{print $1}' | cut -d: -f2)"
docker rmi -f "$(docker image ls | grep resume | awk '{print $3}')"
