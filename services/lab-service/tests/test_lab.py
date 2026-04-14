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

def test_submit_lab_result(client):
    response = client.post('/lab/submit', json={
        'patient_id': 'test-patient-123',
        'test_name': 'Blood Test',
        'result': 'Normal'
    })
    assert response.status_code == 201
    assert 'result_id' in response.get_json()
