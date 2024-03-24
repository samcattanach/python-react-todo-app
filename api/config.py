import os

# Local database configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

# Google Cloud Platform configuration
# run $ export FLASK_ENV=production
class DeployedConfig:
    # SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class TestConfig(Config):
    TESTING = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the form
