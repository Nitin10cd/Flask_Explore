from flask import Flask
from routes.auth import auth_bp # login blue print we seperete the logic in routes 

# create the function which creaes the flask app globally and return in the run.py
def create_app():
    # crete app
    app = Flask(__name__)
    # genereate the secret key
    app.secret_key = 'my-secret'

    # register the blue print 
    app.register_blueprint(auth_bp)

    return app
