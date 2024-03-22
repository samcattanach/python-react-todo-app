import os

DB_URI = 'postgresql://user:password@localhost/testdb'

# Local database configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:537802364684@localhost/tasksdatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

# Google Cloud Platform configuration
# run $ export FLASK_ENV=production
class DeployedConfig:
    # SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://your_user:your_password@/your_database_name?host=/cloudsql/your_connection_name')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class TestConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://your_user:your_password@/your_database_name?host=/cloudsql/your_connection_name')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False  # Disable CSRF tokens in the form
