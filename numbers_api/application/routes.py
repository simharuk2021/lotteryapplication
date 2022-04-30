from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_numbers',methods=['GET'])
def lotto():
    numbers = []

    for i in range(0, 6):
        number=random.randint(1,50)

        while number in numbers:
            number = random.randint(1,50)

        numbers.append(number)
    numbers.sort()

    return Response(f"{numbers}", mimetype="text/plain")