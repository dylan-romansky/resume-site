#!/bin/bash

sudo docker compose down -v
RESUME="$(docker image ls | grep resume | awk '{print $3}')"
sudo docker rmi -f "$RESUME"
sudo docker compose build --no-cache
sudo docker compose up -d
sudo docker exec "$(docker container ls | grep cockroach | awk '{print $1}' | cut -d: -f2)" bash -c "cockroach sql --insecure < /docker-entrypoint-initdb.d/schema.sql"
