#!/bin/bash
# Start Cloud SQL Proxy
./cloud-sql-proxy flask-react-todo-app:europe-west2:todo-app &

# Start Flask app
exec python3 -m flask run --host=0.0.0.0
