#!/bin/bash
SERVICES=('patient-service:5001' 'lab-service:5002' 'appointment-service:5003')
ALL_OK=true

echo "=== MediWatch Health Check at $(date) ==="
for service in "${SERVICES[@]}"; do
    name="${service%%:*}"
    port="${service##*:}"
    response=$(curl -s -o /dev/null -w '%{http_code}' http://localhost:${port}/health)
    if [ "$response" -eq 200 ]; then
        echo "[OK]   ${name} (port ${port})"
    else
        echo "[FAIL] ${name} (port ${port}) - HTTP ${response}"
        ALL_OK=false
    fi
done

if [ "$ALL_OK" = false ]; then
    echo 'ALERT: One or more services are unhealthy!'
    exit 1
fi
echo 'All services healthy.'
