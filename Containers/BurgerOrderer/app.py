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
    data = request.json
    index = data.get('index')
    if 0 <= index <len(cart):
    cart.pop(index) #Tar bort varan
    return jsonify({"status":"error","messege":"Ogiltigt index"
400
@app.route('/place_order', methods=['POST'])
def place_order():
    if not cart:
        return jsonify({"status": "error", "message": "Varukorgen är tom"}), 400
    receipt_number = random.randint(1000, 9999)  # Skapar ett slumpmässigt kvittonummer
    order = {

        'receiptNumber': receipt_number,

        'items': cart  # Beställningen innehåller varorna i varukorgen
    }
    orders.append(order)  # Lägger till beställningen i listan med beställningar
    
    try:

        conn = http.client.HTTPConnection('localhost', 5001)

        headers = {'Content-type': 'application/json'}

        conn.request('POST', '/kitchen/orders', body=json.dumps(order), headers=headers)

        response = conn.getresponse()

        if response.status != 200:

            print(f"Kunde inte skicka beställning till köket: {response.reason}")

        conn.close()

    except Exception as e:

        print(f"Kunde inte skicka beställning till köket: {e}") 


