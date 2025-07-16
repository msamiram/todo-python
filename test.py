import pytest
from app import create_app, db
from models.user import User

@pytest.fixture
def client():
    app = create_app()  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_register_success(client):
    response = client.post('/register', json={
        'username': 'testuser',
        'password': 'password123',
        'first_name': 'Test',
        'last_name': 'User'
    })
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully'

def test_register_missing_fields(client):
    response = client.post('/register', json={
        'username': 'testuser',
    })
    assert response.status_code == 400
    assert 'Missing required fields' in response.json['error']

def test_register_existing_user(client):
    user = User(username='existinguser', first_name='Exist')
    user.set_password('pass')
    with client.application.app_context():
        db.session.add(user)
        db.session.commit()

    response = client.post('/register', json={
        'username': 'existinguser',
        'password': 'password123',
        'first_name': 'Exist'
    })
    assert response.status_code == 400
    assert 'Username already exists' in response.json['error']

def test_login_success(client):
    user = User(username='loginuser', first_name='Login')
    user.set_password('password123')
    with client.application.app_context():
        db.session.add(user)
        db.session.commit()

    response = client.post('/login', json={
        'username': 'loginuser',
        'password': 'password123'
    })
    assert response.status_code == 200
    assert 'token' in response.json
    assert response.json['username'] == 'loginuser'

def test_login_invalid_credentials(client):
    response = client.post('/login', json={
        'username': 'notexist',
        'password': 'wrongpass'
    })
    assert response.status_code == 401
    assert 'Invalid credentials' in response.json['error']
