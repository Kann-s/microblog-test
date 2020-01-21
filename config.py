import os
import platform

basedir = os.path.abspath(os.path.dirname(__file__))

platform_name = platform.system()
if platform_name in ["Linux", "Darwin"]:
    db_protocol = 'sqlite:////'
elif platform_name == "Windows":
    db_protocol = 'sqlite:///'

class Config(object):

    # SECRET_KEY is needed by flask-wtf extension to protect web forms
    # against a nasty attack called Cross-Site Request Forgery
    # or CSRF (pronounced "seasurf")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        db_protocol + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
