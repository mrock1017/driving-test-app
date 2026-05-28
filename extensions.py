from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

mail = Mail()

serializer = URLSafeTimedSerializer(
    "secret123"
)

from flask_mail import Message

import os
import requests

def send_email(subject, recipient, body):

    try:

        url = "https://api.brevo.com/v3/smtp/email"

        headers = {

            "accept": "application/json",

            "api-key": os.environ.get(
                "BREVO_API_KEY"
            ),

            "content-type": "application/json"
        }

        data = {

            "sender": {

                "name": "Japan Driving Test Master",

                "email": os.environ.get(
                    "MAIL_DEFAULT_SENDER"
                )
            },

            "to": [

                {
                    "email": recipient
                }
            ],

            "subject": subject,

            "textContent": body
        }

        response = requests.post(

            url,

            json=data,

            headers=headers,

            timeout=10
        )

        print(response.text)

        return response.status_code == 201

    except Exception as e:

        import traceback

        traceback.print_exc()

        print("EMAIL ERROR:", e)

        return False