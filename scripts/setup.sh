#!/bin/bash
set -e
echo '=== MediWatch Local Setup ==='

if ! docker info > /dev/null 2>&1; then
    echo 'ERROR: Docker is not running. Start Docker and try again.'
    exit 1
fi

echo 'Building Docker images...'
docker-compose build --no-cache

echo 'Starting services...'
docker-compose up -d

echo 'Waiting for services to start...'
sleep 15

for port in 5001 5002 5003; do
    if curl -s http://localhost:${port}/health | grep -q 'ok'; then
        echo "Service on port ${port}: HEALTHY"
    else
        echo "Service on port ${port}: FAILED"
    fi
done

echo 'Setup complete. Access services on ports 5001, 5002, 5003'
