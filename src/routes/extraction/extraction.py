from flask import Flask, jsonify, request, Blueprint, current_app, redirect, url_for
from src.components import extraction

extract_bp = Blueprint("extraction", __name__, url_prefix="/extract")


@extract_bp.route("/", methods=["GET"])
def extract():
    type = request.args.get("type")
    link = request.args.get("link")
    result = extraction.extraction(int(type), link)
    return jsonify(result)
