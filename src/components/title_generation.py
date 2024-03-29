from dotenv import load_dotenv
import requests
import re
import json
from os import getenv


def title_generation(data):
    try:
        print("[!] Server logs: Title generation has started")
        text = data["content"]
        API_URL = "https://api-inference.huggingface.co/models/Michau/t5-base-en-generate-headline"
        text = {"inputs": f"{text}"}
        load_dotenv()
        HF_TOKEN = getenv("HF_TOKEN")
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        response = requests.post(API_URL, headers=headers, json=text)
        result = json.loads(response.content.decode("utf-8"))
        result = result[0]["generated_text"]
        print("[!] Server logs: Title generation completed")
    except:
        data["title"] = "Title Generation Failed! Please try again later."
        print("[!] Server logs: Title generation failed")
    data["title"] = result
    return data
