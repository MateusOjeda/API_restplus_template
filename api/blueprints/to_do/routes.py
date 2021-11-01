from flask_restplus import Resource, Namespace
from api.blueprints.to_do.services import toDoClass
import logging
from flask_restplus import fields

logger = logging.getLogger(__name__)

api = Namespace("example", "Rotas de exemplo para o namespace.")


@api.route("/<string:key>")
class RouteKey(Resource):
    @api.doc(responses={200: "Sucesso"}, params={"key": "Key for request."}, security=None)
    def get(self, key):
        return toDoClass.example_method(key)


serializer_engine = api.model(
    "example_parameters",
    {
        "key": fields.String,
        "key2": fields.String,
        "key3": fields.String,
    },
)


@api.route("/example_post")
class examplePost(Resource):
    @api.expect(serializer_engine)
    @api.doc(responses={200: "Sucesso"}, params={"payload": "Parâmetros post request."}, security=None)
    def post(self):
        """
        Example Post endpoint
        """
        if api.payload:
            return toDoClass.example_method(False)
        else:
            api.abort(400, "Error on payload.")
