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

@app.route('/cancel_order/<int:index>', methods=['DELETE'])
def cancel_order(index):
    if 0 <= index < len(orders):
        orders.pop(index)
        return '', 200
    return 'Order not found!', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)