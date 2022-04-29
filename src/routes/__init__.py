from flask import Blueprint
from src.routes.extraction import extraction

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(extraction.extract_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    return "Homepage route setup!"
