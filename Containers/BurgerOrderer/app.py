from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

BURGERS = ['Cheeseburger', 'Bacon Burger', 'Vegan Burger']
CUSTOMIZATIONS = CUSTOMIZATIONS = ['Extra Cheese', 'No Pickles', 'Lettuce Wrap', 'Double Patty']

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

    return render_template('index.html', burgers=BURGERS, customizations=CUSTOMIZATIONS, cart=session['cart'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
