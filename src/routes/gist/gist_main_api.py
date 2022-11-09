# Main API for the Gist platform.
from flask import Flask, jsonify, request, Blueprint

gist_bp = Blueprint("Gist", __name__, url_prefix="/gist")


@gist_bp.route("/", methods=["GET"])
def gist():
    # Component to read which news articles are picked.
    # Component to send the article to the summarizer using summarize_api (Just call local API using requests)
    # Create MongoDB account and save articles. Format mentioned as below.
    # [{"title": "title of article", "summary": "summary generated", "url": "url of news article", "date_and_time": "value"}, {repeat}]
    result = {"message": "Gist API"}
    return jsonify(result)
