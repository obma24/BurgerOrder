"""
app.py: Application for the Kitchen for managing incoming orders in the KitchenView system.
This Flask application is designed for kitchen staff to manage orders. 
It displays current orders, allows new orders to be added, 
and enables the cancellation of existing orders.
"""
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# List to store all incoming orders
app.orders = []  # Moved orders to be an attribute of the app

@app.route('/')
def kitchen():
    """Render the kitchen page. This function displays the kitchen page along with the current list of orders.
    Returns a str: The rendered HTML template for the kitchen page, showing all the orders.
    """
    return render_template('kitchen.html', orders=app.orders)  # Reference app.orders

@app.route('/new_order', methods=['POST'])
def new_order():
    """Add a new order.
    This function receives a new order via a POST request and adds it to the orders list.
    Returns:
        str: An empty response with a status code of 200 if the order was added successfully.
    """
    full_order = request.get_json()  # Get the new order from the request
    app.orders.append(full_order)  # Add the new order to our list
    return '', 200  # Respond with a success message

@app.route('/get_orders', methods=['GET'])
def get_orders():
    """Retrieve all current orders.
    This function returns the list of current orders in JSON format.
    Returns:
        Response: A JSON response containing the list of orders.
    """
    return jsonify(app.orders)  # Send back app.orders as JSON

@app.route('/cancel_order/<int:index>', methods=['DELETE'])
def cancel_order(index):
    """Cancel an order by its index.
    This function allows you to cancel an order based on its position in the orders list.
    Args:
        index (int): The position of the order you'd like to cancel.
    Returns:
        str: An empty response with a status code of 200 if the order was found and canceled,
            or a friendly error message if the order doesn't exist (status 404).
    """
    if 0 <= index < len(app.orders):  # Reference app.orders
        app.orders.pop(index)  # Remove the order from the list
        return '', 200  # Confirm the cancellation
    return 'Order not found!', 404  # Let them know the order wasn't found

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Start the Flask application