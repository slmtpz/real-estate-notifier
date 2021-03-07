from typing import List
import os
import smtplib
import ssl
from email.mime.text import MIMEText

import pandas as pd

from .models import Post


def notify(posts: List[Post]):
    """Notify the recipient with the new posts."""
    if len(posts) == 0:
        return

    posts_in_dict = [post.dict() for post in posts]
    html = pd.DataFrame(posts_in_dict).to_html(
        escape=False,
        formatters={
            "post_url": _path_to_href_html,
            "image_url": _path_to_image_html
        })
    send_email(html)


def send_email(html):
    """Send an HTML email to the recipient."""
    sender_email = os.environ["SENDER_EMAIL"]
    receiver_email = os.environ["RECEIVER_EMAIL"]
    password = os.environ["SENDER_EMAIL_PASSWORD"]

    message = MIMEText(html, "html")
    message["Subject"] = "Real Estate Notifier Updates"
    message["From"] = sender_email
    message["To"] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def _path_to_image_html(path):
    return '<img src="' + path + '" width="240" >'


def _path_to_href_html(path):
    return '<a href="' + path + '">Click</a>'
