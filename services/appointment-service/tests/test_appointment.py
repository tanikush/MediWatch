import pytest
import sys
sys.path.insert(0, '..')
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

def test_book_appointment(client):
    response = client.post('/appointment/book', json={
        'patient_id': 'test-patient-123',
        'doctor_name': 'Dr. Sharma',
        'appointment_time': '2024-12-20 10:00:00'
    })
    assert response.status_code == 201
    assert 'appointment_id' in response.get_json()
