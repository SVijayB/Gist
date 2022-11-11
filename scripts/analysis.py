from rouge import Rouge
import requests
from pprint import pprint

"""
To perform analysis, a CSV file with following data is to be created.
- ID.
- Source URL.
- Content/Payload.
- Title Generated
- Summary by inShorts.
- Summary by our model.
- Time taken for execution.
- Rouge metric: f1, precision, recall.
"""


def analyse():
    data = requests.get("https://inshorts.me/news/top?offset=0&limit=3").json()
    # pprint(response)

    result = []
    ID = 1
    articles = data["data"]["articles"]
    for article in articles:
        gist_data = requests.get(
            f"http://127.0.0.1:5000/api/summarize?type=1&link={article['sourceUrl']}"
        ).json()

        curr_result = {}
        curr_result["Id"] = ID
        curr_result["sourceUrl"] = article["sourceUrl"]
        curr_result["content"] = gist_data["content"]
        curr_result["titleGenerated"] = gist_data["title"]
        curr_result["inShortsSummary"] = article["content"]
        curr_result["gistSummary"] = gist_data["summary"]
        curr_result["timeTaken"] = gist_data["summarizer_time"]

        rouge = Rouge()
        rouge_score = rouge.get_scores(
            curr_result["gistSummary"], curr_result["inShortsSummary"]
        )
        curr_result["rouge-1"] = rouge_score[0]["rouge-1"]
        curr_result["rouge-2"] = rouge_score[0]["rouge-2"]
        curr_result["rouge-l"] = rouge_score[0]["rouge-l"]
        ID += 1
        result.append(curr_result)
    return result


pprint(analyse())
