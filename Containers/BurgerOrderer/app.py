from flask import Flask, render_template, request, redirect, url_for, session
import requests
from pymongo import MongoClient

# Starta Flask-appen
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Används för att hantera sessions

# Anslut till MongoDB
client = MongoClient('mongo', 27017)
db = client.burger_orderer  # Välj databasen för burger orderer
burgers_collection = db.burgers  # Referens till burgers-kollektionen
customizations_collection = db.customizations  # Referens till customizations-kollektionen

def fetch_burgers_from_db():
    """
    Hämtar alla hamburgare från databasen.

    Returns:
        list: En lista med hamburgare från databasen.
    """
    return list(db.burgers.find())

def fetch_customizations_from_db():
    """
    Hämtar alla anpassningar från databasen.

    Returns:
        list: En lista med anpassningar från databasen.
    """
    return list(db.customizations.find())

@app.route('/', methods=['GET', 'POST'])
def order():
    """
    Hanterar order-logik för att lägga till, ta bort och placera beställningar.

    GET-förfrågningar hämtar hamburgare och anpassningar från databasen
    och visar dem i webbläsaren. POST-förfrågningar hanterar användarens
    interaktioner för att lägga till, ta bort eller skicka beställningar.
    """
    # Initiera varukorgen i sessionen om den inte finns
    if 'cart' not in session:
        session['cart'] = []

    if request.method == 'POST':
        # Hantera lägg till i varukorg
        if request.form.get('action') == 'add':
            burger_choice = request.form.get('burger')  # Hämtar vald hamburgare
            customization_choice = request.form.getlist('customizations')  # Hämtar valda anpassningar

            # Skapar en order med burger och anpassningar
            order = {
                'burger': burger_choice,
                'customizations': customization_choice
            }
            session['cart'].append(order)  # Lägger till order i varukorgen
            session.modified = True  # Markerar sessionen som ändrad

        # Hantera ta bort från varukorg
        elif request.form.get('action') == 'remove':
            index_to_remove = int(request.form.get('index'))  # Hämtar index för att ta bort
            session['cart'].pop(index_to_remove)  # Tar bort order från varukorgen
            session.modified = True  # Markerar sessionen som ändrad

        elif request.form.get('action') == 'place_order':
            final_order = {
                'burgers': session['cart']
            }
            requests.post('http://kitchen:5001/new_order', json=final_order)
            order_confirmed = final_order 
            session['cart'] = []
            session.modified = True

            return redirect(url_for('order', order_confirmed=order_confirmed)) 

    # Hämta data för hamburgare och anpassningar
    burgers_from_db = fetch_burgers_from_db()
    customizations_from_db = fetch_customizations_from_db()

    # Skapa listor över hamburgare och anpassningar för att skicka till HTML-mallen
    BURGERS = [burger['name'] for burger in burgers_from_db]
    CUSTOMIZATIONS = [customization['name'] for customization in customizations_from_db]

    # Rendera HTML-mall med data
    return render_template('index.html', burgers=BURGERS, customizations=CUSTOMIZATIONS, cart=session['cart'], order_confirmed=request.args.get('order_confirmed', None))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Startar Flask-applikationen
