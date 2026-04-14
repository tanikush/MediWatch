import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'

def test_register_patient(client):
    response = client.post('/patient/register', json={
        'name': 'Test Patient',
        'age': 30,
        'blood_group': 'O+'
    })
    assert response.status_code == 201
    assert 'patient_id' in response.get_json()
