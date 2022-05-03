from application import app 
from flask import Flask, request, Response, jsonify 
import random

@app.route('/get_message', methods=['POST'])
def rollover():

    jackpot = {
        0: "Rollover",
        1: "No Rollover",
    }

    numbers = request.json['numbers_api']
    sum = 0
    for number in numbers:
        sum += number
    if sum < 150:
        return jsonify(f"{jackpot[0]}")
    else:
        return jsonify(f"{jackpot[1]}")