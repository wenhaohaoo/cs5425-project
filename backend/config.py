import os


class Config(object):
    APP_NAME = 'backend-api'
    MONGODB_CONNECT = os.getenv('MONGODB_CONNECT')
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
