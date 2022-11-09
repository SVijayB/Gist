from __future__ import print_function

import base64
import json
import os
from bs4 import BeautifulSoup
from flask import request, Blueprint, redirect
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from src.components import summarizer
from .serialzer import HeaderParser


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

gmail_bp = Blueprint("gmail", __name__, url_prefix="/gist")
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
flow = InstalledAppFlow.from_client_secrets_file(
    CURR_DIR + "\\client_secret.json",
    SCOPES,
    redirect_uri="http://127.0.0.1:5000/api/gist/callback",
)


def decode_base64(data_base64):
    data = data_base64.replace("-", "+").replace("_", "/")
    decoded_data = base64.b64decode(data)
    soup = BeautifulSoup(decoded_data, "lxml")
    text = soup.text
    return text


@gmail_bp.route("/", methods=["GET"])
def get_mail():
    authorization_url, state = flow.authorization_url()
    return redirect(authorization_url)


@gmail_bp.route("/callback", methods=["GET", "POST"])
def user_redirect():
    flow.fetch_token(authorization_response=request.url)
    credentials = flow.credentials
    print(credentials)
    service = build("gmail", "v1", credentials=credentials)
    response = service.users().messages().list(maxResults=5, userId="me").execute()
    try:
        messages = response["messages"]
        responses = []
        for msg in messages:
            gmail = service.users().messages().get(userId="me", id=msg["id"]).execute()
            payload = gmail["payload"]
            gmail_text = {}
            try:
                meta_data = HeaderParser(payload["headers"])
                raw_data = ""
                if (
                    payload["mimeType"] == "text/html"
                    or payload["mimeType"] == "text/plain"
                ):
                    body = payload["body"]
                    data = body["data"]
                    raw_data = decode_base64(data)
                else:
                    parts = payload["parts"]
                    for part in parts:
                        body = part["body"]
                        data = body["data"]
                        raw_data += decode_base64(data)

                gmail_text["meta"] = meta_data
                gmail_text["text"] = raw_data
                user_summary = summarizer.summarize(gmail_text)
                print("==*" * 50)
                responses.append(user_summary)
            except Exception as e:
                print(e)
                pass

        # print(responses)

        return json.dumps(responses)
    except Exception as e:
        print(e)
        return "callback!!!!!!!!!!!!!!!!!"


"""

        for msg in messages:
            gmail = service.users().messages().get(userId='me', id=msg['id']).execute()
            payload = gmail['payload']
            try :
                part = payload.get("parts")[0]
                data = part['body']['data']
                data = data.replace("-", "+").replace("_", "/")
                decoded_data = base64.b64decode(data)
                soup = BeautifulSoup(decoded_data, "lxml")
                body = soup.body()
                responses[i] = str(body).replace('\n'," ").replace("\r"," ")
                result = summarizer.summarize(responses[i])
                print(result)
                i = i+1
            except Exception:
                pass

        #print(responses)

        return json.dumps(responses)
"""
