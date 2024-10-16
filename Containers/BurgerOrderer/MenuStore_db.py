"""
In this file, `MenuStore_db.py`, the script is responsible for populating the MongoDB database
for burger options and customizations for the BurgerOrderer application.
It connects to a MongoDB, clears existing data from the 'burgers' and 'customizations' collections,
and then inserts new data. This ensures that every time the application is started,
the database is refreshed with up-to-date burger and customization options.
"""
from pymongo import MongoClient

# Create a MongoClient to connect to the MongoDB instance
# 'mongo' refers to the hostname of the MongoDB service in Docker, and 27017 is the default MongoDB port
client = MongoClient('mongo', 27017)
db = client.burger_orderer  # Access the 'burger_orderer' database

# List of burgers to populate the database
burgers = [
    {"name": "Cheeseburger"},
    {"name": "Bacon Burger"},
    {"name": "Vegan Burger"}
]

# List of customizations to populate the database
customizations = [
    {"name": "Extra Cheese"},
    {"name": "No Pickles"},
    {"name": "Lettuce Wrap"},
    {"name": "Double Patty"}
]

# Clear existing burger data (if any) and insert new burgers
db.burgers.drop()  # Drop the collection to avoid duplicates or stale data
db.burgers.insert_many(burgers)  # Insert the new burger list

# Clear existing customization data (if any) and insert new customizations
db.customizations.drop()  # Drop the collection to avoid duplicates or stale data
db.customizations.insert_many(customizations)  # Insert the new customization list

# Test message to confirm that the database has been populated
print("The database has been populated with burgers and customizations.")  
