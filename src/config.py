import os


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://postgres:P@ssw0rd!@postgres/elasticblog'
    ELASTICSEARCH_URL = os.environ.get('ELASTIC_URI') or \
        'http://elastic'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 10

    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
