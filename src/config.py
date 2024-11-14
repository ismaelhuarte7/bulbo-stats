import os

class Config(object):
    SECRET_KEY = 'secret_key'
    TESTING = False
    SESSION_TYPE = 'filesystem'

class ProductionConfig(Config):
    # Obtén la cadena de conexión desde las variables de entorno de Azure
    connection_string = os.getenv('AZURE_POSTGRESQL_CONNECTIONSTRING', '')
    params = dict(item.split('=') for item in connection_string.split())
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['dbname']}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/bulbostatsdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
}
