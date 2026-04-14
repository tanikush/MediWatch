#!/bin/bash
echo "Cleaning up MediWatch resources..."

docker-compose down -v
docker system prune -af

echo "Cleanup complete!"
