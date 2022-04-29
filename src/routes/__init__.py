from flask import Blueprint

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")


@api_blueprint.route("/", methods=["GET"])
def get_data():
    return "Homepage route setup!"
    return content
