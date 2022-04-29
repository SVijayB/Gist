from flask import Flask, jsonify, request, Blueprint
from src.components.extraction import extract
from src.components import summarizer

summarize_bp = Blueprint("summarize", __name__, url_prefix="/summarize")


@summarize_bp.route("/", methods=["GET"])
def summarize():
    type = request.args.get("type")
    link = request.args.get("link")
    data = extract(int(type), link)
    result = summarizer.summarize(data)
    return jsonify(result)
