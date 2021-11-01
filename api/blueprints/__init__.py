# -*- coding: utf-8 -*-
from flask import Blueprint
from flask_restplus import Api
from api.blueprints.auth.routes import api as routes_auth
from api.blueprints.to_do.routes import api as to_do

v1_blueprint = Blueprint("v1", __name__, url_prefix="")

api = Api(
    v1_blueprint,
    doc="/docs",
    title="API",
    version="1.0.0",
    description="Descrição da API.",
)

api.add_namespace(routes_auth)
api.add_namespace(to_do)
