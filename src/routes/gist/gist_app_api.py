import xmltodict
from bs4 import BeautifulSoup
from flask import Flask, jsonify, Blueprint, request
import json
import requests
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
from bson import json_util

load_dotenv()
gist_app_bp = Blueprint("GistApp", __name__, url_prefix="/gist/app")
CONNECTION_STRING = getenv("MONGO_CONNECTION_STRING")
db = MongoClient(CONNECTION_STRING)
dbname = db["articles"]
collection_name = dbname["items"]


@gist_app_bp.route("/", methods=["GET"])
def gistApp():
    # Read Documents from Mongo Collection
    # Read Page Number
    page = request.args.get("page")
    if page is None or int(page) < 0:
        page = 0
    resp = []
    # cursor = collection_name.find().skip(10).limit(10) not efficient
    skip = 12 * int(page)
    cursor = collection_name.aggregate([{"$skip": skip}, {"$limit": 12}])
    for doc in cursor:
        data = json.loads(json_util.dumps(doc))
        resp.append(data)
    return json.dumps(resp)
