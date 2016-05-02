#!/bin/bash

# Start mongodb docker container
# Port: 27017
# Dir: ~/data/db
# Name: mongodb
docker run -p 27017:27017 -v ~/data/db:/data/db --name mongodb -d mongo

# Start remote shell 
docker run -it --link mongodb:mongo --rm mongo sh -c 'exec mongo "$MONGO_PORT_27017_TCP_ADDR:$MONGO_PORT_27017_TCP_PORT/test"'
