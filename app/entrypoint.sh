#!/bin/bash

python3 manage.py runserver 0.0.0.0:8000 &

cd "python-flask-server-generated"
cd "python-flask-server"
ls
python3 -m swagger_server
