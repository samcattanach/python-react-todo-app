#!/bin/bash
# Start Cloud SQL Proxy
./cloud_sql_proxy -instances=flask-react-todo-app:europe-west2:todo-app=tcp:5432 &

# Start Flask app
exec python3 -m flask run --host=0.0.0.0
