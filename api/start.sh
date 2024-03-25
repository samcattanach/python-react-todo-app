#!/bin/bash
# Start Cloud SQL Proxy
./cloud_sql_proxy -instances=flask-react-todo-app:europe-west2:todo-app=tcp:5432 &

# Wait a little to ensure Cloud SQL Proxy starts
sleep 5

# Start Flask app
# export FLASK_APP=run.py
# exec python3 -m flask run --host=0.0.0.0
# exec gunicorn -b 0.0.0.0:8000 run:app
echo Starting Gunicorn.
exec gunicorn run:app \
    --bind 0.0.0.0:8080
