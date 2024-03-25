# python-react-todo-app
A todo app using Python, React, and PostgreSQL

Author: Samuel Cattanach
Date: 21/3/24

## Requirements:
python v3.12, pip v24, flask 
node.jsjs v20, react


Note: instuctions are for macos

## Install locally:
$ git clone 

### Tasks database:

### API server:
$ cd api
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install

### UI server:
$ cd ../ui
$ npm install


## Run API Unit Tests
$ export FLASK_APP=app
$ export FLASK_ENV=testing
$ pytest tests/api_tests.py

## Run locally:
Tasks database:

### API server:
$ cd api
$ export FLASK_APP=app
$ flask run

### UI server:
$ cd ../ui
$ npm start

## Deployment: