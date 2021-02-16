import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_TLS = False
MAIL_USE_SSL = True

SECRET_KEY = os.environ.get("MAIL_PASSWORD")