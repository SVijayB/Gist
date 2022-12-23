import smtplib
from os import getenv
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


def payloadPrep(email_address, file):
    load_dotenv()
    username = getenv("EMAIL_ADDRESS")
    password = getenv("EMAIL_PASSWORD")
    msg = MIMEMultipart("mixed")

    sender = "naveen.19BCN7185@vitap.ac.in"
    recipient = email_address

    msg["Subject"] = "Gist Gmail Summary Generated"
    msg["From"] = email_address
    msg["To"] = email_address

    text = "Attached is the gist summary generated from your emails."

    text_message = MIMEText(text, "plain")
    msg.attach(text_message)
    with open(file, "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header("Content-Disposition", "attachment", filename=str(file)[5:])
    msg.attach(attach)
    mailServer = smtplib.SMTP(
        "mail.smtp2go.com", 2525
    )  # 8025, 587 and 25 can also be used.
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(sender, recipient, msg.as_string())
    mailServer.close()
    return True
