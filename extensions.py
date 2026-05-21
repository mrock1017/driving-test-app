from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer

mail = Mail()

serializer = URLSafeTimedSerializer(
    "secret123"
)