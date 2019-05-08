import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temp'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # set the uri for the database location, this db will be totally stored through a sqlite database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASEDIR, 'app.db')

    # use this when setting up postgres
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or '<db_type>://<username>:<password>@<host_address>:<post>/<database_name>'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'postgresql://postgres:ResidentEvil4@localhost:5432/twitter'
