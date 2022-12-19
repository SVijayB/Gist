from src.components import summarizer
from celery import Celery
from celery.utils.log import get_task_logger
from EmailSender import send_email

logger = get_task_logger(__name__)
celery = Celery(__name__, backend="redis://127.0.0.1:6379", broker="redis://127.0.0.1:6379")


@celery.task(name="summarizer")
def GmailSummarizer(gmails, email_address):
    responses = []
    for gmail in gmails:
        gmail_summary = summarizer.summarize(gmail)
        responses.append(gmail_summary)
    send_email(responses, email_address)
    return True


"""
 run celery and also redis 
# celery -A flask_celery.celery worker -l info --pool=solo 
Compile Celery with --pool=solo argument. #IMP
# celery -A flask_celery.celery worker -l info --pool=solo
Example: celery -A your-application worker -l info --pool=solo
"""
