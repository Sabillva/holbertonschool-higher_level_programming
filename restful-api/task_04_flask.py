from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))