from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2
import os
import uuid

app = Flask(__name__)
metrics = PrometheusMetrics(app)

def get_db():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        database='patientdb',
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres')
    )

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'patient-service'})

@app.route('/patient/register', methods=['POST'])
def register():
    data = request.get_json()
    patient_id = str(uuid.uuid4())
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO patients (id, name, age, blood_group) VALUES (%s, %s, %s, %s)',
        (patient_id, data['name'], data['age'], data['blood_group'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'patient_id': patient_id, 'message': 'Patient registered'}), 201

@app.route('/patient/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM patients WHERE id = %s', (patient_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify({'id': row[0], 'name': row[1], 'age': row[2], 'blood_group': row[3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
