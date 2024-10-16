# Import necessary modules from Flask for creating the web application, 
# rendering templates, handling requests, redirects, URLs, and session management.
from flask import Flask, render_template, request, redirect, url_for, session

import requests # Import the 'requests' library for making HTTP requests.


# Import MongoClient from the pymongo library to interact with MongoDB.
from pymongo import MongoClient

app = Flask(__name__) # Initialize the Flask web application.

# Set the secret key for securely signing the session data. 
# This key should be kept confidential to protect the application's sessions.
app.secret_key = 'your_secret_key'

# Create a MongoDB client connected to the 'mongo' container on port 27017.
client = MongoClient('mongo', 27017)

db = client.burger_orderer # Access the 'burger_orderer' database in MongoDB.

# Access the 'burgers' collection in the 'burger_orderer' database, 
# which stores information about the burgers available in the system.
burgers_collection = db.burgers

# Access the 'customizations' collection in the 'burger_orderer' database, 
# which stores information about customizations available for the burgers.
customizations_collection = db.customizations

def fetch_burgers_from_db():
    """
    Fetches the list of burgers from the MongoDB database.

    Returns:
        list: A list of burgers retrieved from the database.
    """
    return list(db.burgers.find())

def fetch_customizations_from_db():
    """
    Fetches the list of customizations from the MongoDB database.

    Returns:
        list: A list of customizations retrieved from the database.
    """
    return list(db.customizations.find())

@app.route('/', methods=['GET', 'POST'])
def order():
    """
    Handles the order placement and cart management for the hamburger ordering system.

    This function manages the cart's session state, processes requests to add or remove items,
    and places orders by communicating with the kitchen service.

    Returns:
        Response: Redirects to the same page to show the order confirmation.
    """
    # Check if the cart exists in the session; if not, initialize it as an empty list.
    if 'cart' not in session:
        session['cart'] = []

    # Handle POST requests for cart and order actions.
    if request.method == 'POST':
        if request.form.get('action') == 'add':
            # Retrieve the selected burger and customizations from the form.
            burger_choice = request.form.get('burger')
            customization_choice = request.form.getlist('customizations')

            # Create an order dictionary to hold the burger and its customizations.
            order = {
                'burger': burger_choice,
                'customizations': customization_choice
            }
            # Add the order to the session cart.
            session['cart'].append(order)
            session.modified = True

        elif request.form.get('action') == 'remove':
            # Remove the order from the cart based on the index provided.
            index_to_remove = int(request.form.get('index'))
            session['cart'].pop(index_to_remove)
            session.modified = True

        elif request.form.get('action') == 'place_order':
            # Create a final order containing all items in the cart.
            final_order = {
                'burgers': session['cart']
            }
            # Send the order to the kitchen service via POST request.
            requests.post('http://kitchen:5001/new_order', json=final_order)

            # Store the confirmed order details in the session for display.
            order_confirmed = final_order  # Store the confirmed order details
            session['confirmed_order'] = order_confirmed  # Store the confirmed order in session

            # Clear the cart after placing the order.
            session['cart'] = []
            session.modified = True

            # Redirect to the same page to show the order confirmation.
            return redirect(url_for('order'))  # Redirect to the same page to show the order confirmation


    burgers_from_db = fetch_burgers_from_db()
    customizations_from_db = fetch_customizations_from_db()

    BURGERS = [burger['name'] for burger in burgers_from_db]
    CUSTOMIZATIONS = [customization['name'] for customization in customizations_from_db]

    return render_template('index.html', burgers=BURGERS, customizations=CUSTOMIZATIONS, cart=session['cart'], order_confirmed=session.get('confirmed_order', None))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
