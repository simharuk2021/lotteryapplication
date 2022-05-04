from application import app 
from flask import Flask, request, Response, jsonify
import requests


@app.route('/', methods=['POST', 'GET'])
def home(): 
    numbers_api = requests.get('http://numbers_api:5000/get_numbers')
    day_api = requests.get('http://day_api:5000/get_days')

    result = {'numbers_api': numbers_api.text} 
    message = requests.post('http://rollover_api:5000/get_message', json = result)
    

    # return jsonify(f"{numbers_api} {day_api} {message}")
    return jsonify(numbers_api = numbers_api.text, message = message.text, day_api = day_api.text)