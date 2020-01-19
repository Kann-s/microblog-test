import os

class Config(object):

    # SECRET_KEY is needed by flask-wtf extension to protect web forms
    # against a nasty attack called Cross-Site Request Forgery
    # or CSRF (pronounced "seasurf")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
