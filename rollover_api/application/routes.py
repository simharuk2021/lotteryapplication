from application import app 
from flask import Flask, request, Response, jsonify 
import random

jackpot = {
    0: "Rollover",
    1: "No Rollover",
    }

@app.route('/get_message', methods=['POST'])
def rollover():

    results = eval(request.get_json()['numbers_api'])
    
    sum = 0
    for result in results:
        sum += result
    if sum < 150:
        return Response(f"{jackpot[0]}", mimetype = 'text/plain')
    else:
        return Response(f"{jackpot[1]}", mimetype = 'text/plain')