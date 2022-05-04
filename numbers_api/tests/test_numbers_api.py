from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask, request, Response, jsonify
from application import app 
import random

class TestBase(TestCase):
    def create_app(self):
        return app

class TestData(TestBase):
    
    def get_data(self):
        return {'numbers_api': self.numbers_api}

    def test_numbers(self):
        self.numbers_api = []
        for i in range(0, 6):
            number=random.randint(1,50)
            self.numbers_api.append(number)
        response = self.client.get(url_for('lotto'))
        self.numbers_api.sort()
        self.assertEqual(self.numbers_api, self.get_data()['numbers_api'])
        assert response.status_code == 200  
    
    


    # def test_get_days(self):
    #     self.assertEqual(self.get_day_api(), 'Saturday')
    


