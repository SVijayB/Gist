from operator import mod
from transformers import pipeline
from src.components.title_generation import title_generation


def summarize(data):
    text = data["result"]
    to_tokanize = text
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    summarized = summarizer(to_tokanize, min_length=75, max_length=300)
    tmp = " ".join([str(i) for i in summarized])
    tmp = tmp.replace("{", "")
    tmp = tmp.replace("''", "")
    tmp = tmp.replace("\x92", "")
    data["summary"] = tmp
    data = title_generation(data)
    return data
