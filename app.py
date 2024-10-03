from flask import Flask, request, jsonify, render_template
import random
import http.client
import json

app = Flask(__name__)

cart = []
orders = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    cart.append(data)
    return jsonify({"status": "success"}), 200