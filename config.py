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

    MAIL_SERVER = 'smtp-relay.brevo.com'

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')

    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')
