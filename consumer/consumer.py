import os
import json
import argparse
import requests
from urllib.parse import quote_plus

from kafka import KafkaConsumer
from pymongo import MongoClient


KAFKA_BROKER_CONNECT = os.getenv('KAFKA_BROKER_CONNECT')
MONGODB_CONNECT = os.getenv('MONGODB_CONNECT')
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

crystal_feel_url = 'https://socialanalyticsplus.net/crystalfeel/getEmotionScores.php'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    'Referer':      'https://socialanalyticsplus.net/crystalfeel/'
}


def get_sentiment(text):
    res = requests.post(crystal_feel_url, headers=headers, data=f'tweet={quote_plus(text)}')
    sentiment = res.json()['scores'].split('Sentiment: </b>')[1].split('</td>')[0].lower()
    if 'positive' in sentiment:
        return 1
    elif 'negative' in sentiment:
        return -1
    else:
        return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        default='sg',
        help='topic to consume from: "sg" or "hk"',
    )
    args = parser.parse_args()

    print(args)

    consumer = KafkaConsumer(
        args.t,
        bootstrap_servers=[KAFKA_BROKER_CONNECT],
        group_id=f'group-{args.t}',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    client = MongoClient(MONGODB_CONNECT, username=MONGODB_USERNAME, password=MONGODB_PASSWORD)
    if args.t == 'sg':
        collection = client.tweets.sg
    elif args.t == 'hk':
        collection = client.tweets.hk
    elif args.t == 'au':
        collection = client.tweets.au

    for message in consumer:
        print(message)
        message = message.value
        message['sentiment'] = get_sentiment(message['text'])
        collection.insert_one(message)
        print('{} added to {}'.format(message, collection))