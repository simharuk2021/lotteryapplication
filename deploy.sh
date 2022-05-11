#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

su -i jenkins

ssh swarm-manager