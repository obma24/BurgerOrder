from pymongo import MongoClient

# Anslut till MongoDB
client = MongoClient('mongo', 27017)
db = client.burger_orderer  # Välj databasen för burger orderer

# Lista över hamburgare att införa i databasen
burgers = [
    {"name": "Cheeseburger"},
    {"name": "Bacon Burger"},
    {"name": "Vegan Burger"}
]

# Lista över anpassningar att införa i databasen
customizations = [
    {"name": "Extra Cheese"},
    {"name": "No Pickles"},
    {"name": "Lettuce Wrap"},
    {"name": "Double Patty"}
]

# Rensa tidigare data och inför ny data i databasen
db.burgers.drop()  # Tar bort tidigare hamburgare
db.burgers.insert_many(burgers)  # Lägger till hamburgare
db.customizations.drop()  # Tar bort tidigare anpassningar
db.customizations.insert_many(customizations)  # Lägger till anpassningar

print("Databasen är populär med hamburgare och anpassningar.") #test
