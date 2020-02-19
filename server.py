from flask import Flask, jsonify

app = Flask(__name__)

# get data
@app.route('/')
def home():
    data = "Hello World"
    return jsonify(data)

