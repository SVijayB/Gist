from __future__ import print_function

import base64
import json
import os
from bs4 import BeautifulSoup
from flask import request, Blueprint, redirect, Response
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from .serialzer import HeaderParser
from flask_celery import GmailSummarizer

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

gmail_bp = Blueprint("gmail", __name__, url_prefix="/gmail")
SCOPES = ["https://www.googleapis.com/auth/userinfo.email", "openid", "https://www.googleapis.com/auth/gmail.readonly",
          "https://www.googleapis.com/auth/userinfo.profile"]

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
flow = InstalledAppFlow.from_client_secrets_file(
    CURR_DIR + '\\client_secret.json', SCOPES,
    redirect_uri="http://localhost:3000"  # http
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
    code = request.get_json().get('code')
    No_of_Emails = request.args.get("NoEmails")
    if int(No_of_Emails) > 15:
        No_of_Emails = 15
    print(No_of_Emails)
    flow.fetch_token(code=code)
    credentials = flow.credentials
    print(credentials)
    service = build('gmail', 'v1', credentials=credentials)
    email_address = service.users().getProfile(userId='me').execute()['emailAddress']
    response = service.users().messages().list(maxResults=No_of_Emails, userId='me').execute()
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
                gmail_text['content'] = raw_data
                responses.append(gmail_text)
            except Exception as e:
                print(e)
                return "Extracting gmail failed ", 400

        # print(responses)
        print(f"Sending Mail to {email_address}")
        GmailSummarizer.delay(responses, email_address)

        return "Request successful", 200
    except Exception as e:
        print(e)
        return "Bad Request ", 400
