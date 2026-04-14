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
        database='appointmentdb',
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres')
    )

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'service': 'appointment-service'})

@app.route('/appointment/book', methods=['POST'])
def book():
    data = request.get_json()
    appointment_id = str(uuid.uuid4())
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO appointments (id, patient_id, doctor_name, appointment_time) VALUES (%s, %s, %s, %s)',
        (appointment_id, data['patient_id'], data['doctor_name'], data['appointment_time'])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'appointment_id': appointment_id, 'message': 'Appointment booked'}), 201

@app.route('/appointment/<appointment_id>', methods=['DELETE'])
def cancel(appointment_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM appointments WHERE id = %s', (appointment_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Appointment cancelled'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
