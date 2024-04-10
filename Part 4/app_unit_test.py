import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_signin(client):
    response = client.get('/signin')
    assert response.status_code == 200

def test_addProduct(client):
    response = client.get('/admin/addProduct')
    assert response.status_code == 200

def test_signup(client):
    response = client.get('/signup')
    assert response.status_code == 200

def test_register(client):
    response = client.post('/register', json={
        'username': 'Ram',
        'email': 'ram@example.com',
        'phone': '1234567890',
        'password': '123',
        'address': 'Test Address'
    })
    assert response.status_code == 201

def test_login(client):
    response = client.post('/login', json={
        'email': 'pranaybhandekar8841@gmail.com',
        'password': '123'
    })
    assert response.status_code == 200

def test_logout(client):
    response = client.get('/logout')
    assert response.status_code == 302  # Redirects to index page

def test_add_to_cart(client):
    response = client.post('/add_to_cart', json={
        'user_id': '660eb666737ad2cce2ff63e0',  # Provided user ID
        'product_id': '66077b310ded56fa26194535'  # Provided product ID
    })
    assert response.status_code == 200

def test_search_products(client):
    response = client.get('/search_products?keyword=IPhone')
    assert response.status_code == 200

def test_cart(client):
    response = client.get('/cart?user_id=660eb666737ad2cce2ff63e0')  # Provided user ID
    assert response.status_code == 200

def test_carts(client):
    response = client.get('/carts?user_id=660eb666737ad2cce2ff63e0')  # Provided user ID
    assert response.status_code == 200

def test_checkout(client):
    response = client.post('/checkout', json={
        'user_id': '660b9fd644fe37ae4241c473',  # Provided user ID
        'products': ['66077b310ded56fa26194535']  # Provided product ID
    })
    assert response.status_code == 200

def test_transactions(client):
    response = client.get('/transactions?user_id=660eb666737ad2cce2ff63e0')  # Provided user ID
    assert response.status_code == 200

def test_transaction(client):
    response = client.get('/transaction?user_id=660eb666737ad2cce2ff63e0')  # Provided user ID
    assert response.status_code == 200

def test_aboutus(client):
    response = client.get('/aboutus')
    assert response.status_code == 200

def test_contact(client):
    response = client.get('/contact')
    assert response.status_code == 200

def test_profile(client):
    response = client.get('/profile')
    assert response.status_code == 200

def test_update_profile(client):
    response = client.post('/update_profile', json={
        'user_id': '660eb666737ad2cce2ff63e0',  # Provided user ID
        'username': 'newusername',
        'email': 'new@example.com',
        'phone': '9876543210',
        'address': 'New Address'
    })
    assert response.status_code == 200

def test_user_info(client):
    response = client.get('/user_info?user_id=660eb666737ad2cce2ff63e0')  # Provided user ID
    assert response.status_code == 200

def test_delete_from_cart(client):
    response = client.delete('/delete_from_cart?user_id=660eb666737ad2cce2ff63e0&product_id=66077b310ded56fa26194535')  # Provided user ID and product ID
    assert response.status_code == 200
