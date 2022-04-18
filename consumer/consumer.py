import os
import json
import argparse
from datetime import datetime

from kafka import KafkaConsumer
from pymongo import MongoClient
import sparknlp
import pyspark.sql.functions as F
from pyspark.ml.pipeline import PipelineModel


KAFKA_BROKER_CONNECT = os.getenv('KAFKA_BROKER_CONNECT')
MONGODB_CONNECT = os.getenv('MONGODB_CONNECT')
MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')

crystal_feel_url = 'https://socialanalyticsplus.net/crystalfeel/getEmotionScores.php'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 
    'Referer':      'https://socialanalyticsplus.net/crystalfeel/'
}

def predict(spark, model, tweet):
    sample_df = spark.createDataFrame([[str(tweet)]]).toDF('text')
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', r'http\S+',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '@\w+',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '#',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', 'RT',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '&amp;',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '&quot;',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '&gt',''))
    sample_df = sample_df.withColumn('text', F.regexp_replace('text', '&lt',''))

    result = model.transform(sample_df)
    sentiment = result.select("prediction").first()[0]
    return sentiment

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        default='sg',
        help='topic to consume from: "sg" or "hk"',
    )
    args = parser.parse_args()

    print(args)

    spark = spark = sparknlp.start(gpu=True)
    model = PipelineModel.load("model/Models/svm_sg")

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
        message['created_at'] = datetime.strptime(message['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        message['sentiment'] = predict(spark, model, message['text'])
        collection.insert_one(message)
        print('{} added to {}'.format(message, collection))
