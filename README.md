# python-react-todo-app
Author: Samuel Cattanach
Date: 25/3/24

A todo app using Python, React, and PostgreSQL.

Deployment to the Google Cloud Platform is handled automaticaclly by a Github Actions workflow. The flask and react servers are dockerized, uploaded to the Artifact Registry, and then deployed as Cloud Run services.



Requirements:
python v3.12, pip v24, flask 
node.jsjs v20, react



### Install locally:
```
$ git clone git@github.com:samcattanach/python-react-todo-app.git
```

API server:
```
$ cd python-react-todo-app/api
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install
```

UI server:
```
$ cd ../ui/app
$ npm install
```

### Run API Unit Tests
```
$ export FLASK_APP=app
$ export FLASK_ENV=testing
$ pytest api/tests/api_tests.py
```


### Run locally:

 API server:
```
$ cd api
$ export FLASK_APP=app
$ gunicorn -b 0.0.0.0:8080 run:app
```

 UI server:
```
$ cd ui/api
$ npm start
```

