import os

class Config(object) :
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')

class DevelopmentConfig(Config) :
    DEBUG = True

class StagingConfig(Config) :
    DEBUG = True

class TestingConfig(Config) :
    DEBUG = True
    TESTING = True

class ProductionConfig(Config) :
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'staging' : StagingConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig
}