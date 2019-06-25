#!/bin/bash -e

function stop_server {
    echo "Stopping local server"
	docker rm -f postgres-obnk nginx-obnk django-obnk
}

# Build docker images 
docker-compose build

# Start local server
docker-compose -f docker-compose.yml -f envs/docker-compose.local.yml up -d 


# Trap to stop docker containers
trap 'stop_server' EXIT

# Run Postman tests
newman run obnk/tests/OBnk.postman_collection.json

# online collection
# newman run https://www.getpostman.com/collections/0629c9d2abf64d63a63c

