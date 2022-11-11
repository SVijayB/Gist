from __future__ import print_function

import base64
import json
import os
from bs4 import BeautifulSoup
from flask import request, Blueprint, redirect, Response
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from src.components import summarizer
from .serialzer import HeaderParser

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

gmail_bp = Blueprint("gmail", __name__, url_prefix="/gist")
SCOPES = ["https://www.googleapis.com/auth/userinfo.email","openid","https://www.googleapis.com/auth/gmail.readonly","https://www.googleapis.com/auth/userinfo.profile"]

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
flow = InstalledAppFlow.from_client_secrets_file(
    CURR_DIR + '\\client_secret.json', SCOPES,
    redirect_uri="http://localhost:3000" #http
)


def jsonResponseFactory(data):
    """Return a callable in top of Response"""

    def callable(response=None, *args, **kwargs):
        """Return a response with JSON data from factory context"""
        return Response(json.dumps(data), *args, **kwargs)

    return callable


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
    code = request.get_json().get('code')
    flow.fetch_token(code=code)
    credentials = flow.credentials
    print(credentials)
    with open('token.json', 'w') as token:
        token.write(credentials.to_json())
    print(credentials.to_json())
    service = build('gmail', 'v1', credentials=credentials)
    response = service.users().messages().list(maxResults=1, userId='me').execute()
    try:
        messages = response['messages']
        responses = []
        for msg in messages:
            gmail = service.users().messages().get(userId='me', id=msg['id']).execute()
            payload = gmail['payload']
            gmail_text = {}
            try:
                meta_data = HeaderParser(payload['headers'])
                raw_data = ''
                if payload["mimeType"] == 'text/html' or payload["mimeType"] == 'text/plain':
                    body = payload["body"]
                    data = body['data']
                    raw_data = decode_base64(data)
                else:
                    parts = payload["parts"]
                    for part in parts:
                        body = part["body"]
                        data = body['data']
                        raw_data += decode_base64(data)

                gmail_text['meta'] = meta_data
                gmail_text['text'] = raw_data
                #user_summary = summarizer.summarize(gmail_text)
                print("==*" * 50)
                #responses.append(user_summary)
            except Exception as e:
                print(e)
                pass

        # print(responses)

        return json.dumps(responses)
    except Exception as e:
        print(e)
        return "callback!!!!!!!!!!!!!!!!!"



