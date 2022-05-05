from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from flask import Flask
from application import app 

class TestBase(TestCase):
    def create_app(self):
        return app

class TestData(TestBase):
    
    def get_data(self):
        return {'numbers_api': self.numbers_api, 'day_api': self.day_api, 'rollover_api': self.rollover_api, 'message': self.message}

    def test_rollover(self):
        results = '[1,2,3,4,5,6]'
        days = 'Saturday'
        response = self.client.post(url_for('rollover'), json = {'numbers_api': results, 'day_api': days})
        assert response.status_code == 200
        self.assertEquals(b'Rollover', response.data)

    def test_rollover_day(self):
        results = '[10,20.30,40,45,50]'
        days = 'Wednesday'
        response = self.client.post(url_for('rollover'), json = {'numbers_api': results, 'day_api': days})
        assert response.status_code == 200
        self.assertEquals(b'No Rollover', response.data)

    def test_rollover_day_weds(self):
        results = '[1,2,3,4,5,6]'
        days = 'Wednesday'
        response = self.client.post(url_for('rollover'), json = {'numbers_api': results, 'day_api': days})
        assert response.status_code == 200
        self.assertEquals(b'No Rollover', response.data)

    def test_no_rollover(self):
        results = '[10,20,30,40,45,50]'
        days = 'Saturday'
        response = self.client.post(url_for('rollover'), json = {'numbers_api': results, 'day_api': days})
        assert response.status_code == 200
        self.assertEquals(b'No Rollover', response.data)
    


