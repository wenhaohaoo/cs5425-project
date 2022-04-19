# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sentiment import Sentiment  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSentimentController(BaseTestCase):
    """SentimentController integration test stubs"""

    def test_sentiment_country_get(self):
        """Test case for sentiment_country_get

        Returns a list of aggregated sentiments per day.
        """
        query_string = [('start', 'Sat Jan 30 08:00:00 SGT 2021'),
                        ('end', 'Sun Jan 30 08:00:00 SGT 2022')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/sentiment/{country}'.format(country='country_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sentiment_country_past24hr_get(self):
        """Test case for sentiment_country_past24hr_get

        Returns aggregated sentiments for the past 24 hours.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/sentiment/{country}/past-24hr'.format(country='country_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sentiment_country_past30_days_get(self):
        """Test case for sentiment_country_past30_days_get

        Returns aggregated sentiments for the past 30 days.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/sentiment/{country}/past-30-days'.format(country='country_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sentiment_country_past7_days_get(self):
        """Test case for sentiment_country_past7_days_get

        Returns aggregated sentiments for the past 7 days.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/sentiment/{country}/past-7-days'.format(country='country_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
