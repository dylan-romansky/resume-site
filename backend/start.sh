#!/bin/bash

# Start the containerized Flask application in a
# standalone docker container for quick and easy
# testing of new frontend code

docker container rm -f "$(docker container ls | grep resume | awk '{print $1}' | cut -d: -f2)"
docker rmi -f "$(docker image ls | grep resume | awk '{print $3}')"
docker build --no-cache -t resume .
docker run -p "80:80" resume
