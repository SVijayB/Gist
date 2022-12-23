import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(list_resp, EmailAddress):
    username = os.environ.get("EMAIL_ADDRESS")  # naveen.19BCN7185@vitap.ac.in
    password = os.environ.get('EMAIL_PASSWORD')
    msg = MIMEMultipart('mixed')

    sender = 'naveen.19BCN7185@vitap.ac.in'
    recipient = 'naveennoob95@gmail.com'

    msg['Subject'] = 'Gist Email'
    msg['From'] = EmailAddress
    msg['To'] = recipient

    text = ""

    for i in list_resp:
        text += json.dumps(i)

    text_message = MIMEText(text, 'plain')
    msg.attach(text_message)

    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525)  # 8025, 587 and 25 can also be used.
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(sender, recipient, msg.as_string())
    mailServer.close()
