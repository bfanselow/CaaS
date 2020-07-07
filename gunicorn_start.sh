#!/bin/sh
# Spawn 1 Gunicorn worker processes, running 1 thread. 
# Acepting connections from all interfaces:8080, overriding Gunicorn's default port (8000).
gunicorn --chdir app caas:api -w 1 --threads 1 -b 0.0.0.0:8080
