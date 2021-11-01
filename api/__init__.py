from flask import Flask


def create_app(config_level):
    app = Flask(__name__)
    app.config.from_object(f"config.{config_level}")

    return app
