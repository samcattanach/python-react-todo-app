

# Local database configuration
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class DeployedConfig:
    DEBUG = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False 
