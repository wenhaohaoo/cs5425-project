import connexion
from pymongo import MongoClient

from config import Config
from openapi_server import encoder


mongo_client = MongoClient(Config.MONGODB_CONNECT, username=Config.MONGODB_USERNAME, password=Config.MONGODB_PASSWORD)
tweets_db = mongo_client.tweets
sentiments_db = mongo_client.sentiments

def set_cors_headers_on_response(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'X-Requested-With'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS'
    return response

def create_app(config_class=Config):
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'COVID-19 Tweets Sentiment Analysis API'},
                pythonic_params=True)
    app.app.after_request(set_cors_headers_on_response)

    return app
