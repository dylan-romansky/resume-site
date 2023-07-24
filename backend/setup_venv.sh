#!/bin/bash

mkdir .env
python -m venv ./.env/
./.env/bin/python -m pip install --upgrade pip
./.env/bin/pip install -r requirements.txt
