from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_days',methods=['GET'])
def name(): 
    day_choice = ["Wednesday", "Saturday"]
    actual_day = random.choice(day_choice)
    return Response(f"{actual_day}", mimetype="text/plain")