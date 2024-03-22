# Initializes Flask app and brings together other components
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config, DeployedConfig, TestConfig

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

    db.init_app(app)


    from app.models.tasks_model import Task

    # Create tables within the app context
    with app.app_context():
        db.create_all()  

    from app.routes.tasks_routes import tasks_bp
    app.register_blueprint(tasks_bp)

    return app
