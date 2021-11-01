from flask_restplus import Resource, Namespace, fields
import logging

logger = logging.getLogger(__name__)
api = Namespace("auth", "Authentication routes")

login = api.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)


@api.route("/login")
class Login(Resource):
    @api.expect(login, validate=True)
    @api.doc(
        responses={
            200: "Success",
            404: "Unauthorized",
        },
    )
    def post(self):
        """
        Authentication endpoint
        """
        username = api.payload.get("username")
        password = api.payload.get("password")

        logger.info(f"username: {username}")
        logger.info(f"password: {password}")

        if username == "invalid":
            api.abort(404, "Unauthorized")

        return {
            "username": "USER",
        }, 200
