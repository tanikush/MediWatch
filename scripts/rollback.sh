#!/bin/bash
SERVICE=${1:-'all'}

echo "Rolling back ${SERVICE}..."

if [ "$SERVICE" = 'all' ]; then
    for svc in patient-service lab-service appointment-service; do
        kubectl rollout undo deployment/${svc}
        kubectl rollout status deployment/${svc} --timeout=60s
    done
else
    kubectl rollout undo deployment/${SERVICE}
    kubectl rollout status deployment/${SERVICE} --timeout=60s
fi

echo 'Rollback complete. Current pod status:'
kubectl get pods
