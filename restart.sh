#!/bin/bash

sudo docker compose down -v
#RESUME="$(docker image ls | grep resume | awk '{print $3}')"
#MYSQL="$(docker image ls | grep mysql | awk '{print $3}')"
#sudo docker rmi -f "$RESUME" "$MYSQL"
#sudo rm -rf ./db
sudo docker compose build --no-cache
sudo docker compose up -d
