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
@app.route('/view_cart,methods=['GET']
def view_cart():
    return jsonify(cart),200
@app.route('/remove_from_cart,methods=['POST'])
def remove_from_cart(): 
