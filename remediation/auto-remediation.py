import requests
import subprocess
import logging
import time
from datetime import datetime

logging.basicConfig(
    filename='/var/log/mediwatch-remediation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

PROMETHEUS_URL = 'http://localhost:9090'
ERROR_THRESHOLD = 0.05  # 5%
CHECK_INTERVAL = 30  # seconds

def query_prometheus(query):
    try:
        response = requests.get(
            f'{PROMETHEUS_URL}/api/v1/query',
            params={'query': query},
            timeout=10
        )
        data = response.json()
        if data['status'] == 'success':
            return data['data']['result']
    except Exception as e:
        logging.error(f'Prometheus query failed: {e}')
    return []

def trigger_rollback(service_name):
    logging.info(f'Triggering rollback for {service_name}')
    try:
        subprocess.run(
            ['bash', '/path/to/scripts/rollback.sh', service_name],
            check=True,
            timeout=120
        )
        logging.info(f'Rollback completed for {service_name}')
        return True
    except Exception as e:
        logging.error(f'Rollback failed: {e}')
    return False

def check_error_rates():
    query = """
        sum(rate(flask_http_request_total{status=~'5..'}[5m])) by (job)
        /
        sum(rate(flask_http_request_total[5m])) by (job)
    """
    results = query_prometheus(query)
    for result in results:
        service = result['metric'].get('job', 'unknown')
        error_rate = float(result['value'][1])
        if error_rate > ERROR_THRESHOLD:
            msg = (f'[AUTO-REMEDIATION] {datetime.now()} | '
                   f'Service: {service} | Error rate: {error_rate:.1%} | '
                   f'Threshold: {ERROR_THRESHOLD:.0%} | Action: Rollback triggered')
            logging.warning(msg)
            print(msg)
            trigger_rollback(service)

def check_service_health():
    services = [
        ('patient-service', 5001),
        ('lab-service', 5002),
        ('appointment-service', 5003)
    ]
    for service_name, port in services:
        try:
            response = requests.get(f'http://localhost:{port}/health', timeout=5)
            if response.status_code != 200:
                msg = f'[AUTO-REMEDIATION] {service_name} health check failed'
                logging.warning(msg)
                print(msg)
                trigger_rollback(service_name)
        except Exception as e:
            logging.error(f'{service_name} unreachable: {e}')

if __name__ == '__main__':
    logging.info('Auto-remediation script started')
    print('MediWatch Auto-Remediation Service Started')
    while True:
        check_error_rates()
        check_service_health()
        time.sleep(CHECK_INTERVAL)
