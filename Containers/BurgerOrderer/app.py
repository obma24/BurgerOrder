from flask import Flask, render_template, request, redirect, url_for, session
import requests
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'your_secret_key'

client = MongoClient('mongo', 27017)
db = client.burger_orderer
burgers_collection = db.burgers
customizations_collection = db.customizations

def fetch_burgers_from_db():
    return list(db.burgers.find()) 

def fetch_customizations_from_db():
    return list(db.customizations.find())


@app.route('/', methods=['GET', 'POST'])
def order():
    if 'cart' not in session:
        session['cart'] = []

    if request.method == 'POST':
        if request.form.get('action') == 'add':
            burger_choice = request.form.get('burger')
            customization_choice = request.form.getlist('customizations')

            order = {
                'burger': burger_choice,
                'customizations': customization_choice
            }
            session['cart'].append(order)
            session.modified = True

        elif request.form.get('action') == 'remove':
            index_to_remove = int(request.form.get('index'))
            session['cart'].pop(index_to_remove)
            session.modified = True

        elif request.form.get('action') == 'place_order':
            for order in session['cart']:
                requests.post('http://kitchen:5001/new_order', json=order)
            session['cart'] = []
            session.modified = True

        return redirect(url_for('order'))

    burgers_from_db = fetch_burgers_from_db()
    customizations_from_db = fetch_customizations_from_db()

    BURGERS = [burger['name'] for burger in burgers_from_db]
    CUSTOMIZATIONS = [customization['name'] for customization in customizations_from_db]

    return render_template('index.html', burgers=BURGERS, customizations=CUSTOMIZATIONS, cart=session['cart'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
