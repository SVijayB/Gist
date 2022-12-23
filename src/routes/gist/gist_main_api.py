# Main API for the Gist platform.
import xmltodict
from bs4 import BeautifulSoup
from flask import Flask, jsonify, Blueprint
import json
import requests
from dotenv import load_dotenv
from os import getenv
from pymongo import MongoClient
from lxml import etree

load_dotenv()
gist_bp = Blueprint("Gist", __name__, url_prefix="/gist")
CONNECTION_STRING = getenv("MONGO_CONNECTION_STRING")
db = MongoClient(CONNECTION_STRING)
dbname = db["articles"]
collection_name = dbname["items"]


@gist_bp.route("/", methods=["GET"])
def gist():
    # Component to read which news articles are picked.
    # Component to send the article to the summarizer using summarize_api (Just call local API using requests)
    # Create MongoDB account and save articles. Format mentioned as below.
    # [{"title": "title of article", "summary": "summary generated", "url": "url of news article", "date_and_time": "value"}, {repeat}]

    url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
    response = requests.get(url)
    my_dict = xmltodict.parse(response.content)
    data = my_dict["rss"]["channel"]["item"]
    result = []
    for article in data:
        article_url = article["link"]
        reqs = requests.get(article_url)
        soup = BeautifulSoup(reqs.text, "html.parser")
        img_s = soup.find_all("img")
        og_img = soup.find("meta",attrs={"property":"og:image"})
        img_url = og_img.get('content')
        print(img_url)
        gist_data = requests.get(
            f"http://127.0.0.1:5000/api/summarize?type=1&link={article_url}"
        ).json()
        article = {
            "title": gist_data["title"],
            "summary": gist_data["summary"],
            "url": article["link"],
            "dateAndTime": article["pubDate"],
            "image": img_url,
        }
        result.append(article)
    collection_name.insert_many(result)
    print("[!] Server log: Database updated successfully!")
    return jsonify({"status": "success", "message": "Gist data added to database"})
