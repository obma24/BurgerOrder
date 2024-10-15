from pymongo import MongoClient

client = MongoClient('mongo', 27017)
db = client.burger_orderer 

burgers = [
    {"name": "Cheeseburger"},
    {"name": "Bacon Burger"},
    {"name": "Vegan Burger"}
]

customizations = [
    {"name": "Extra Cheese"},
    {"name": "No Pickles"},
    {"name": "Lettuce Wrap"},
    {"name": "Double Patty"}
]

db.burgers.drop()
db.burgers.insert_many(burgers)
db.customizations.drop()
db.customizations.insert_many(customizations)

print("Databasen är populär med hamburgare och anpassningar.") #test
