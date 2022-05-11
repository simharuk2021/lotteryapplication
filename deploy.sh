#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

su -l jenkins

ssh swarm-manager