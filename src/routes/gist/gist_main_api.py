# Main API for the Gist platform.
from flask import Flask, jsonify, Blueprint
import json
import requests
import os

gist_bp = Blueprint("Gist", __name__, url_prefix="/gist")


@gist_bp.route("/", methods=["GET"])
def gist():
    # Component to read which news articles are picked.
    # Component to send the article to the summarizer using summarize_api (Just call local API using requests)
    # Create MongoDB account and save articles. Format mentioned as below.
    # [{"title": "title of article", "summary": "summary generated", "url": "url of news article", "date_and_time": "value"}, {repeat}]
    #.format is not working check once
    url="https://content.guardianapis.com/search?api-key=a30ecd9a-662c-431b-9d69-ded54b8c51f7"
    #.format(os.getenv("Guardian_API_Key"))
    response = requests.get(url)
    data= response.json()["response"]
    result = []
    for article in data["results"]:
        article={
            "title":article["webTitle"],
            "summary":"will generate",
            "url":article["webUrl"],
            "date_and_time":article["webPublicationDate"]
        }
        result.append(article)

    return jsonify(result)

