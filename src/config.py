class Config(object):
    SECRET_KEY = 'secret_key'
    TESTING = False
    SESSION_TYPE = 'filesystem'
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/bulbostatsdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/bulbostatsdb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    
    pass

config = {
    "production" : ProductionConfig,
    "development": DevelopmentConfig,
}