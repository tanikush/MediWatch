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
        database='labdb',
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres')
    )

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'lab-service'})

@app.route('/lab/submit', methods=['POST'])
def submit():
    data = request.get_json()
    result_id = str(uuid.uuid4())
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO lab_results (id, patient_id, test_name, result) VALUES (%s, %s, %s, %s)',
        (result_id, data['patient_id'], data['test_name'], data['result'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'result_id': result_id, 'message': 'Lab result submitted'}), 201

@app.route('/lab/<patient_id>', methods=['GET'])
def get_results(patient_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM lab_results WHERE patient_id = %s', (patient_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    results = [{'id': r[0], 'patient_id': r[1], 'test_name': r[2], 'result': r[3]} for r in rows]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
