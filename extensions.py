from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

mail = Mail()

from flask_mail import Message

def send_email(subject, recipient, body):

    try:

        msg = Message(

            subject,

            recipients=[recipient]
        )

        msg.body = body

        mail.send(msg)

        return True

    except Exception as e:

        print(e)

        return False

serializer = URLSafeTimedSerializer(
    "secret123"
)