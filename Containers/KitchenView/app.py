from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

orders = []

@app.route('/')
def kitchen():
    return render_template('kitchen.html', orders=orders)

@app.route('/new_order', methods=['POST'])
def new_order():
    full_order = request.get_json()
    orders.append(full_order)
    return '', 200

@app.route('/get_orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)