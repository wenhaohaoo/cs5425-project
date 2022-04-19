import connexion
import six

from openapi_server.models.sentiment import Sentiment  # noqa: E501
from openapi_server import util


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
    start = util.deserialize_date(start)
    end = util.deserialize_date(end)
    return 'do some magic!'


def sentiment_country_past24hr_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 24 hours.

    Sentiments for COVID-19 related Tweets for past 24 hours. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    return 'do some magic!'


def sentiment_country_past30_days_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 30 days.

    Sentiments for COVID-19 related Tweets for past 30 days. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    return 'do some magic!'


def sentiment_country_past7_days_get(country):  # noqa: E501
    """Returns aggregated sentiments for the past 7 days.

    Sentiments for COVID-19 related Tweets for past 7 days. # noqa: E501

    :param country: Country to query; must be in [\&quot;sg\&quot;, \&quot;hk\&quot;, \&quot;au\&quot;]
    :type country: str

    :rtype: Sentiment
    """
    return 'do some magic!'
