#!/usr/bin/python3
"""Module for secure API"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {

    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

