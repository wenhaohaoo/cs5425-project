from datetime import datetime, timedelta

import connexion
import six

from openapi_server.models.sentiment import Sentiment  # noqa: E501
from openapi_server import util, tweets_db, sentiments_db


AGGREGATE_TEMPLATE = [
    {'$match': { 
        'created_at': {'$gt': None}
    }},
    {'$group': {
        '_id': { '$dateToString': {'format': '%Y-%m-%d', 'date': "$created_at"} },
        'sentiment_sum': { '$sum': '$sentiment' }, 
        'count': { '$sum': 1 }
    }},
    {'$project': {
        'positive': { '$divide': ['$sentiment_sum', '$count'] },
        'negative': { '$subtract': [1, { '$divide': ['$sentiment_sum', '$count']}]},
        'tweet_count': '$count'
    }},
    {'$sort': { '_id': 1 }}
]

FIND_PRECOMPUTE_TEMPLATE = { 'date': {'$gt': None} }

def sentiment_country_get(country, start, end=None):  # noqa: E501
    """Returns a list of aggregated sentiments per day.

    Sentiments for COVID-19 related Tweets will be aggregated by day. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str
    :param start: Start date (inclusive) for sentiment aggregation
    :type start: str
    :param end: End date (exclusive) for sentiment aggregation
    :type end: str

    :rtype: List[Sentiment]
    """
    now = datetime.now()
    start = util.deserialize_datetime(start)
    end = util.deserialize_datetime(end)

    find = FIND_PRECOMPUTE_TEMPLATE.copy()
    find['date']['$gt'] = start
    if end:
        find['date']['$lt'] = end
    results = list(map(lambda x: Sentiment(x['date'].date(), x['positive'], x['negative'], x['tweet_count']), sentiments_db[country].find(find)))
    
    if start <= now <= end:
        aggregate = AGGREGATE_TEMPLATE.copy()
        aggregate[0]['$match']['created_at']['$gt'] = now
        results += list(map(lambda x: Sentiment(x['_id'], x['positive'], x['negative'], x['tweet_count']), tweets_db[country].aggregate(aggregate)))

    return results


def sentiment_country_past24hr_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 24 hours.

    Sentiments for COVID-19 related Tweets for past 24 hours. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    time = datetime.now() - timedelta(hours=24)
    aggregate = AGGREGATE_TEMPLATE.copy()
    aggregate[0]['$match']['created_at']['$gt'] = time
    aggregate[1]['$group']['_id'] = 'agg'
    result = list(tweets_db[country].aggregate(aggregate))
    if result:
        return Sentiment(time.strftime('%Y-%m-%d'), result['positive'], result['negative'], result['tweet_count'])
    else:
        return Sentiment(time.strftime('%Y-%m-%d'), 0, 0, 0)


def sentiment_country_past7_days_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 7 days.

    Sentiments for COVID-19 related Tweets for past 7 days. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    time = datetime.now() - timedelta(days=7)
    aggregate = AGGREGATE_TEMPLATE.copy()
    aggregate[0]['$match']['created_at']['$gt'] = time
    aggregate[1]['$group']['_id'] = 'agg'
    result = list(tweets_db[country].aggregate(aggregate))
    if result:
        return Sentiment(time.strftime('%Y-%m-%d'), result['positive'], result['negative'], result['tweet_count'])
    else:
        return Sentiment(time.strftime('%Y-%m-%d'), 0, 0, 0)


def sentiment_country_past30_days_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 30 days.

    Sentiments for COVID-19 related Tweets for past 30 days. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    time = datetime.now() - timedelta(days=30)
    aggregate = AGGREGATE_TEMPLATE.copy()
    aggregate[0]['$match']['created_at']['$gt'] = time
    aggregate[1]['$group']['_id'] = 'agg'
    result = list(tweets_db[country].aggregate(aggregate))
    if result:
        return Sentiment(time.strftime('%Y-%m-%d'), result['positive'], result['negative'], result['tweet_count'])
    else:
        return Sentiment(time.strftime('%Y-%m-%d'), 0, 0, 0)
