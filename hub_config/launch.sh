#! /bin/bash

export OAUTH2_AUTHORIZE_URL="http://localhost:8000/o/authorize"
export OAUTH2_TOKEN_URL="http://localhost:8000/o/token/"

jupyterhub -f jupyterhub_config.py

