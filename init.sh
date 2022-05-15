#!/bin/bash
echo 'Installing locust in a venv'
python3 -m venv .env
source .env/bin/activate
python3 -m pip install --upgrade pip
pip3 install locust
source .env/bin/activate
locust -V

echo 'Starting node server'
npm install
curl http://jsonplaceholder.typicode.com/db >db.json
