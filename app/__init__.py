from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create the function which creates the flask app globally
def create_app():
    # create app
    app = Flask(__name__)
    
    # configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # optional, to suppress warnings
    
    db.init_app(app)
    
    # generate the secret key
    # app.secret_key = 'my-secret'

    # register the blueprint
    # from routes.auth import auth_bp
    # app.register_blueprint(auth_bp)

    return app
