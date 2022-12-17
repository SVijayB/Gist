from flask import Blueprint, request
import json
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
from bson import json_util

load_dotenv()
gist_data_bp = Blueprint("gistData", __name__, url_prefix="/gist/data")
CONNECTION_STRING = getenv("MONGO_CONNECTION_STRING")
db = MongoClient(CONNECTION_STRING)
dbname = db["articles"]
collection_name = dbname["items"]


@gist_data_bp.route("/", methods=["GET"])
def gistData():
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
