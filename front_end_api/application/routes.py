from application import app 
from flask import Flask, request, Response
import requests


@app.route('/', methods=['GET'])
def home(): 
    numbers_api = requests.get('http://numbers_api:5000/get_numbers')
    return Response(f"{numbers_api.text} ", mimetype="text/plain")