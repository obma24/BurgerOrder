import pytest
from app import app 

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True  # Enabling testing mode
    with app.test_client() as client:
        yield client  # Provided the test client to the tests

@pytest.fixture(autouse=True)
def reset_orders():
    """Reset the orders list before each test."""
    app.orders = []  # Reset the orders list before each test

def test_kitchen_page(client):
    """Test that the kitchen page renders correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Kitchen' in response.data

def test_new_order(client):
    """Test adding a new order."""
    new_order = {'item': 'Burger', 'quantity': 2}
    response = client.post('/new_order', json=new_order)
    assert response.status_code == 200
    # Check if the order was added
    response = client.get('/get_orders')
    assert response.json == [new_order]

def test_get_orders(client):
    """Test retrieving current orders."""
    response = client.get('/get_orders')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # test that it ensures it's a list

def test_cancel_order(client):
    """Test canceling an order."""
    new_order = {'item': 'Burger', 'quantity': 2}
    client.post('/new_order', json=new_order)  # Add an order to cancel
    response = client.delete('/cancel_order/0')  # Cancel the first order
    assert response.status_code == 200

    # Debugging: Check the state of orders after cancellation
    response = client.get('/get_orders')
    print("Current orders after cancellation:", response.json)  # Debugging line
    assert response.json == []  # No orders should remain


if __name__ == '__main__':
    pytest.main()