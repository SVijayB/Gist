from flask import Flask, jsonify, request, Blueprint
from src.components import categorizer

category_bp = Blueprint("categorizer", __name__, url_prefix="/category")


@category_bp.route("/", methods=["GET"])
def category():
    link = request.args.get("link")
    result = categorizer.category(link)
    return jsonify(result)
