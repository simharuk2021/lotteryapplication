from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask, request, Response, jsonify
from application import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestData(TestBase):
    # def test_data(self):
        # self.numbers_api = '1,2,3,4,5,6'
        # self.day_api = 'Saturday'
        # self.rollover_api = 'Rollover'
        # self.no_rollover_api = 'No Rollover'
        # self.message = 'Rollover'
    
    # def get_numbers_api(self):
    #     return self.numbers_api
        
    # def get_day_api(self):
    #     return self.day_api
    
    # def get_rollover_api(self): 
    #     return self.rollover_api
    
    # def get_no_rollover_api(self):
    #     return self.no_rollover_api

    # def get_message(self):
    #     return self.message
    
    # def set_message(self, message):
    #     self.message = message
    
    def get_data(self):
        return {'numbers_api': self.numbers_api, 'day_api': self.day_api, 'rollover_api': self.rollover_api, 'no_rollover_api': self.no_rollover_api, 'message': self.message}

    def test_day(self):
        with patch('random.choice') as p:
            p.return_value = 'Saturday'
            response = self.client.get(url_for('name'))
            assert response.status_code == 200
            self.assertIn(b'Saturday', response.data)

    # def test_get_days(self):
    #     self.assertEqual(self.get_day_api(), 'Saturday')
    


