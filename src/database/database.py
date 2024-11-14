from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(session_options={'expire_on_commit': False})

def init_app(app):
    db.init_app(app)
    config(app)
    return app

def config(app):
    @app.teardown_appcontext
    def close_session(exception=None):
        db.session.close()
    return app

def reset():
    db.drop_all()
    print ('Base de datos borrada')
    db.create_all()
    print ('Base de datos reiniciada')

    
    