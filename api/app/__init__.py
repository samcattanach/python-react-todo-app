# Initializes Flask app and brings together other components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
import os, json, pg8000, sqlalchemy
from config import Config, DeployedConfig, TestConfig
from google.cloud.sql.connector import Connector, IPTypes
from google.cloud import secretmanager

# get cloud secret
def access_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")
    try:
        credentials = json.loads(payload)
    except json.JSONDecodeError:
        raise ValueError("Failed to decode secret data as JSON.")
    return credentials

# get DB conn details
project_id = "flask-react-todo-app"
secret_id = "todo-app-db"
credentials = access_secret_version(project_id, secret_id)

db_url = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(credentials["user"], credentials["password"], credentials["host"], credentials["port"], credentials["database"])



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    print("Launching...")

    if os.getenv('FLASK_ENV') == 'production':
        print("Config: DeployedConfig")
        app.config.from_object(DeployedConfig)
    elif os.getenv('FLASK_ENV') == 'tests':
        print("Config: TestConfig")
        app.config.from_object(TestConfig)
    else:
        print("Config: Config")
        app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    print("Connecting to DB...")
    db.init_app(app)
    print("Connected")

    from app.models.tasks_model import Task

    # Create tables within the app context
    with app.app_context():
        db.create_all()  

    from app.routes.tasks_routes import tasks_bp
    app.register_blueprint(tasks_bp)

    print("Ready")
    return app
