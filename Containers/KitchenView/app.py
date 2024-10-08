from flask import Flask, render_template, request

app = Flask(__name__)

orders = []

@app.route('/')
def kitchen():
    return render_template('kitchen.html', orders=orders)

@app.route('/new_order', methods=['POST'])
def new_order():
    order = request.get_json()
    orders.append(order)
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
