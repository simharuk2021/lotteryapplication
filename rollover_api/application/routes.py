from application import app 
from flask import Flask, request, Response, jsonify 
import random

jackpot = {
    0: "Rollover",
    1: "No Rollover",
    }

@app.route('/get_message', methods=['POST'])
def rollover():

    result = request.json['result']

    sum = 0
    for number in numbers:
        sum += number
    if sum < 150:
        return jsonify(f"{jackpot[0]}")
    else:
        return jsonify(f"{jackpot[1]}")