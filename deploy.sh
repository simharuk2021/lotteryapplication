#!/bin/bash

rsync docker-compose.yaml nginx.conf swarm-manager:

exec sudo su -l jenkins

ssh swarm-manager