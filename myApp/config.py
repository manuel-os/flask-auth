import os

class Config:
    #move to env vars
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'e153b5cf68f0ce85f684ced65453066a'
    #move to env vars
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')