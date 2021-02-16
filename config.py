import os

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_TLS = True
MAIL_USE_SSL = False

SECRET_KEY = os.environ.get("KEY")