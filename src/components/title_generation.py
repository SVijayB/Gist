from dotenv import load_dotenv
import requests
import re
import json
from os import getenv


def title_generation(data):
    try:
        print("[!] Server logs: Title generation has started")
        try:
            text = data["article"]
        except KeyError as k:
            text = data["text"]
        API_URL = "https://api-inference.huggingface.co/models/Michau/t5-base-en-generate-headline"
        text = {"inputs": f"{text}"}
        load_dotenv()
        HF_TOKEN = getenv("HF_TOKEN")
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        response = requests.post(API_URL, headers=headers, json=text)
        result = json.loads(response.content.decode("utf-8"))
        result = result[0]["generated_text"]
        print("[!] Server logs: Title generation completed")

        data["title"] = result
    except:
        data["title"] = "Title Generation Failed"
    return data
