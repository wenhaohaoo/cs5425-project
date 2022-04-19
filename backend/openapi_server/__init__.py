import connexion
from pymongo import MongoClient

from config import Config
from openapi_server import encoder


db = MongoClient(Config.MONGODB_CONNECT, username=Config.MONGODB_USERNAME, password=Config.MONGODB_PASSWORD).tweets

def create_app(config_class=Config):
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'COVID-19 Tweets Sentiment Analysis API'},
                pythonic_params=True)

    return app