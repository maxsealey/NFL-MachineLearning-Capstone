"""
__init__.py

Creates flask app, loads configurations, registers blueprints, and returns it
"""
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Load configurations
    app.config.from_object('config.Config')

    # Register Blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app