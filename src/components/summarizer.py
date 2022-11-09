import re
import json
import requests
from os import getenv
from dotenv import load_dotenv
from src.components.title_generation import title_generation


def summarize(data):
    print("[!] Server logs: Summarizer Engine has started")
    try:
        text = data["article"]
    except KeyError as k:
        text = data["text"]
    # to_tokanize = text[:1024]
    API_URL = (
        "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
    )
    load_dotenv()
    HF_TOKEN = getenv("HF_TOKEN")
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": text, "min_length": 100, "max_length": 300}
    response = requests.request("POST", API_URL, headers=headers, data=payload)
    summarized = json.loads(response.content.decode("utf-8"))

    tmp = " ".join([str(i) for i in summarized])
    tmp = tmp.replace("{", "")
    tmp = tmp.replace("''", "")
    tmp = tmp.replace(f"{chr(61623)}", "")
    tmp = tmp.replace("\x92", "")
    tmp = tmp.replace("\x0c", "")
    regex_pattern = r"(?<='summary_text': ' )(.*)(?='})"
    try:
        result = re.search(regex_pattern, tmp).group(0)
    except:
        result = tmp
    result = result.encode("ascii", "ignore")
    result = result.decode()
    data["summary"] = result
    print("[!] Server logs: Summarized article")
    data = title_generation(data)
    return data
