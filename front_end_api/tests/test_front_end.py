from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask, request, Response, jsonify, url_for
from application import app 
import random
import requests_mock

class TestBase(TestCase):
    def create_app(self):
        return app

class TestData(TestBase):

    def get_data(self):
        return {'numbers_api': self.numbers_api, 'day_api': self.day_api, 'rollover_api': self.rollover_api, 'message': self.message}

    def test_day(self):
        number_api = '[1,2,3,4,5,6]'
        day_api = 'Saturday'
        rollover_api = 'Rollover'

        with requests_mock.Mocker() as p:
            p.get('http://numbers_api:5000/get_numbers', text = number_api)
            p.get('http://day_api:5000/get_days', text = day_api)
            p.post('http://rollover_api:5000/get_message', text = rollover_api)
            response = self.client.get(url_for('home'))
            self.assertEquals(response.status_code, 200)

