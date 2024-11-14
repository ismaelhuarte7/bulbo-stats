from flask import Flask, Blueprint, session
from flask_session import Session
from src.config import config
from src.web import routes
from src.database import database
from src.web import commands
session = Session()

def create_app(env="development"):
    app = Flask(__name__)
    
    app.config.from_object(config[env])
    
    database.init_app(app)
    
    session.init_app(app)
    
    routes.register(app)
    
    commands.register(app)
    
    
    return app
