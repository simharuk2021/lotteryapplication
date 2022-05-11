#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

ssh swarm-manager