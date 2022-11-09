import re

from pytz import unicode
from transformers import pipeline

from src.components.title_generation import title_generation


def summarize(data):
    print("[!] Server logs: Summarizer Engine has started")
    try:
        text = data["article"]
    except KeyError as k:
        text = data["text"]
    to_tokanize = text[:1024]
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summarized = summarizer(to_tokanize)
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
