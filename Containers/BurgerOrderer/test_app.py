import pytest
from flask import Flask
from app import app  # Import your Flask app

# Using the 'app' fixture to set up the testing environment
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enabling testing mode
    with app.test_client() as client:
        yield client  # return the client for testing

# Mock the MongoDB database interaction
@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    def mock_find_burgers():
        return [{'name': 'Cheeseburger'}, {'name': 'Veggie Burger'}]

    def mock_find_customizations():
        return [{'name': 'Extra Cheese'}, {'name': 'Bacon'}, {'name': 'No Pickles'}]

    # Patch the functions to return mock data
    monkeypatch.setattr('app.fetch_burgers_from_db', mock_find_burgers)
    monkeypatch.setattr('app.fetch_customizations_from_db', mock_find_customizations)

# testing the index route
def test_order_page(client):
    response = client.get('/')  # Make a GET request to the index page
    assert response.status_code == 200  # Check if the response status code is 200 OK
    assert b'Cheeseburger' in response.data  # Check if the burger is in the response data
    assert b'Extra Cheese' in response.data  # Check if a customization is in the response data

# Testing adding a burger to the cart
def test_add_to_cart(client):
    response = client.post('/', data={
        'action': 'add',
        'burger': 'Cheeseburger',
        'customizations': ['Extra Cheese']
    })
    assert response.status_code == 200  # Check if the response is a redirect
    
    # Check if the burger is in the session cart
    with client.session_transaction() as sess:
        assert len(sess['cart']) == 1  # Ensure one item is in the cart
        assert sess['cart'][0]['burger'] == 'Cheeseburger'  # Check the burger
        assert 'Extra Cheese' in sess['cart'][0]['customizations']  # Check the customizations

# Test removing a burger from the cart
def test_remove_from_cart(client):
    # First, add a burger to the cart
    client.post('/', data={
        'action': 'add',
        'burger': 'Cheeseburger',
        'customizations': ['Extra Cheese']
    })

    # Now remove the burger from the cart
    response = client.post('/', data={
        'action': 'remove',
        'index': 0  # Remove the first item
    })
    assert response.status_code == 200  # Check the response

    # Check if the cart is empty
    with client.session_transaction() as sess:
        assert len(sess['cart']) == 0  # Ensure the cart is empty after removal

# Test placing an order
def test_place_order(client, requests_mock):
    # Mock the request to the kitchen service
    requests_mock.post('http://kitchen:5001/new_order', status_code=200)

    # Add a burger to the cart
    client.post('/', data={
        'action': 'add',
        'burger': 'Cheeseburger',
        'customizations': ['Extra Cheese']
    })

    # Place the order
    response = client.post('/', data={
        'action': 'place_order'
    })
    assert response.status_code == 302

    # Check if the cart is empty after placing the order
    with client.session_transaction() as sess:
        assert len(sess['cart']) == 0  # Ensure the cart is empty after placing the order
        assert 'confirmed_order' in sess  # Check if the confirmed order exists in the session

# Run the tests
if __name__ == '__main__':
    pytest.main()
