import os
import json

from tweepy import OAuthHandler, Stream
from kafka import KafkaProducer


# Environemnt Vars
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
KAFKA_BROKER_CONNECT = os.getenv('KAFKA_BROKER_CONNECT')

# Bounding Boxes
SG = [103.566667,1.202857,104.094369,1.483382]
HK = [113.817111,22.136722,114.502444,22.568333]
AUS = [72.25,-55.32,168.23,-9.09]


class TweetListener(Stream):
    def on_data(self, data):
        json_ = json.loads(data) 
        print(json.dumps(json_, indent=2) + '\n')
        if json_['place']['country_code']  == 'SG':
            producer.send('sg', json.dumps({'id': json_['id_str'], 'created_at': json_['created_at'], 'text': json_['text']}).encode('utf-8'))
        elif json_['place']['country_code'] == 'HK':
            producer.send('hk', json.dumps({'id': json_['id_str'], 'created_at': json_['created_at'], 'text': json_['text']}).encode('utf-8'))
        return True
    
    def on_error(self, status):
        print (status)

print(f'{KAFKA_BROKER_CONNECT}')
producer = KafkaProducer(bootstrap_servers=f'{KAFKA_BROKER_CONNECT}')
tweet_stream = TweetListener(f'{CONSUMER_KEY}', f'{CONSUMER_SECRET}', f'{ACCESS_TOKEN}', f'{ACCESS_TOKEN_SECRET}')
tweet_stream.filter(locations=SG+HK)
