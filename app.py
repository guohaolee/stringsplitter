from flask import Flask, Blueprint
from flask_restplus import Api, Resource

from apiv1 import v1

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1, url_prefix='/api/v1')
    return app
