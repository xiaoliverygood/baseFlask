from flask import Flask
from app.web import webBlue


def create_app():
    app = Flask(__name__)
    addBulePrint(app)
    return app


def addBulePrint(app):
    app.register_blueprint(webBlue)
