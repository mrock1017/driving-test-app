import os

class Config:

    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        'super-secret-key'
    )

    SQLALCHEMY_DATABASE_URI = (

        os.environ.get('DATABASE_URL')

        or

        'sqlite:///users.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = 'your_email@gmail.com'

    MAIL_PASSWORD = 'your_app_password'

    MAIL_DEFAULT_SENDER = 'your_email@gmail.com'