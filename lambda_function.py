import os
import json
from flask import Flask
from flask_lambda import FlaskLambda

app = Flask(__name__)
lambda_handler = FlaskLambda(app)

@app.route('/')
def hello_world():
    return 'Hello, World! This is my Flask app on AWS Lambda.'

def lambda_handler(event, context):
    return lambda_handler.run(event, context)

if __name__ == '__main__':
    app.run(debug=True)
