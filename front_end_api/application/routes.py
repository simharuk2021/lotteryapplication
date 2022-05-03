from application import app 
from flask import Flask, request, Response, jsonify
import requests


@app.route('/', methods=['GET'])
def home(): 
    numbers_api = requests.get('http://numbers_api:5000/get_numbers')
    day_api = requests.get('http://day_api:5000/get_days')


    message = requests.post('http://rollover:5000/get_message', json = {'result': numbers_api})
    result = Results (numbers_api = numbers_api.json()) 

    return jsonify(f"{numbers_api.text} {day_api.text} {message.text}", mimetype="text/plain")