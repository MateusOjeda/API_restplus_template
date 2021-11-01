import logging
from api import create_app
from api.blueprints import v1_blueprint
from flask_cors import CORS


if __name__ == "__main__":
    app = create_app(config_level="DevConfig")
    CORS(app)
    app.register_blueprint(v1_blueprint)
    app.run(host="0.0.0.0", port=5003)
else:
    app = create_app(config_level="ProdConfig")
    CORS(app)
    app.register_blueprint(v1_blueprint)
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
