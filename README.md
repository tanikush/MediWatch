# 🏥 MediWatch – Hospital Infrastructure Reliability Platform

[![GitHub](https://img.shields.io/badge/GitHub-MediWatch-blue?logo=github)](https://github.com/tanikush/MediWatch)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5?logo=kubernetes)](https://kubernetes.io/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)


> A production-grade DevOps project demonstrating automated infrastructure, CI/CD pipelines, monitoring, and self-healing systems for hospital applications.

---

## 📋 Table of Contents
- [Problem Statement](#-problem-statement)
- [Solution Overview](#-solution-overview)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Deployment](#-deployment)
- [Monitoring](#-monitoring)
- [Testing](#-testing)
- [Author](#-author)
- [License](#-license)

---

## 🎯 Problem Statement

Hospitals rely on critical systems like patient management, lab processing, and appointment scheduling. However:

- ⏱️ Average downtime: **45+ minutes**
- 🚨 Manual failure detection
- 🏥 Delays in patient care
- 📉 No automated recovery

---

## 💡 Solution Overview

**MediWatch** provides:

- ✅ Real-time failure detection  
- ✅ Auto rollback when error rate > **5%**  
- ✅ Recovery time reduced to **< 2 minutes**  
- ✅ Zero-downtime deployments  

---

## 📸 Screenshots

### 🏗️ Architecture Diagram
<img alt="Architecture" src="https://github.com/user-attachments/assets/3f98a81b-83a4-4016-9447-97330f600ea4" />

---

### 🐳 Docker Services Running
<img alt="Docker PS" src="https://github.com/user-attachments/assets/d1823447-2dbe-4fbe-b822-a8e55a404ad9" />

---

### 📜 Service Logs
<img alt="Docker Logs" src="https://github.com/user-attachments/assets/14377b1f-f2e2-4eed-96be-6e2b0babc052" />

---

### ❤️ Health Checks

**Service 1**
<img alt="Health Check 1" src="https://github.com/user-attachments/assets/fb6fe916-2135-47c9-84dc-d33468e126ca" />
---

**Service 2**
<img alt="Health Check 2" src="https://github.com/user-attachments/assets/fd2159fd-4ba3-45be-a8ce-669fc0f7f85c" />
---

**Service 3**
<img alt="Health Check 3" src="https://github.com/user-attachments/assets/9970caee-8c23-41c7-9581-7fe4634f7a80" />

---

### 🔗 API Testing
<img alt="API Test" src="https://github.com/user-attachments/assets/eef91d4a-2a16-4516-be10-e9c3ad31d442" />

---

### 📊 Prometheus Metrics
<img alt="Prometheus" src="https://github.com/user-attachments/assets/13c7353a-b8d3-472a-ac83-8a13c7281a7b" />

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| Backend | Python 3.11, Flask |
| Database | PostgreSQL 15 |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes (K3s) |
| CI/CD | Jenkins |
| IaC | Ansible |
| Monitoring | Prometheus, Grafana |
| Cloud | AWS (EC2, ECR, S3) |
| Version Control | Git, GitHub |
| Testing | pytest |

---

## ✨ Features

### 🔄 CI/CD Pipeline
- Linting with `flake8`
- Testing with `pytest`
- Docker image build & push to AWS ECR
- Kubernetes rolling deployment
- GitHub webhook integration

---

### 🎯 Microservices Architecture
- Patient Service  
- Lab Service  
- Appointment Service  

Each includes:
- `/health`
- `/metrics`

---

### 📊 Monitoring
- Prometheus (15s scrape interval)
- Grafana dashboards:
  - Uptime
  - Requests/sec
  - P95 latency
  - Pod restarts
- Real-time alerting

---

### 🔧 Self-Healing
- Auto-remediation script
- Rollback triggers:
  - Error rate > 5%
  - Health check failure
  - High pod restarts

---

### ⚡ High Availability
- Kubernetes HPA enabled
- CPU-based auto-scaling (70%)
- 1–4 replicas per service
- Zero-downtime rolling updates

---

## 📁 Project Structure

mediwatch/
├── services/
│ ├── patient-service/
│ │ ├── app.py
│ │ ├── requirements.txt
│ │ ├── Dockerfile
│ │ └── tests/
│ │ └── test_patient.py
│ │
│ ├── lab-service/
│ │ ├── app.py
│ │ ├── requirements.txt
│ │ ├── Dockerfile
│ │ └── tests/
│ │ └── test_lab.py
│ │
│ └── appointment-service/
│ ├── app.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── tests/
│ └── test_appointment.py
│
├── jenkins/
│ └── Jenkinsfile
│
├── ansible/
│ ├── provision.yml
│ └── inventory.ini
│
├── kubernetes/
│ ├── patient-deployment.yaml
│ ├── lab-deployment.yaml
│ ├── appointment-deployment.yaml
│ ├── postgres-deployment.yaml
│ ├── configmap.yaml
│ └── monitoring/
│ ├── prometheus-config.yaml
│ ├── prometheus-deployment.yaml
│ ├── grafana-deployment.yaml
│ └── alertmanager-config.yaml
│
├── remediation/
│ ├── auto-remediation.py
│ └── requirements.txt
│
├── scripts/
│ ├── setup.sh
│ ├── health-check.sh
│ ├── rollback.sh
│ └── cleanup.sh
│
├── docker-compose.yml
└── README.md



> This structure follows a microservices-based architecture with clear separation of services, infrastructure, CI/CD, and monitoring.

---

## 🚀 Quick Start

```bash
git clone https://github.com/tanikush/MediWatch
cd MediWatch
docker-compose up -d
cat scripts/init-db.sql | docker exec -i mediwatch-postgres-1 psql -U postgres
docker ps

🔍 Health Check
curl http://localhost:5001/health
curl http://localhost:5002/health
curl http://localhost:5003/health

🌐 Deployment (AWS + Kubernetes)

ansible-playbook ansible/provision.yml -i ansible/inventory.ini
ssh -i ~/.ssh/mediwatch-key.pem ubuntu@YOUR_EC2_IP

git clone https://github.com/tanikush/MediWatch.git
cd MediWatch

docker-compose build

kubectl apply -f kubernetes/
kubectl apply -f kubernetes/monitoring/

📊 Monitoring

Prometheus

http://localhost:9090
http://localhost:30090

Grafana

http://localhost:3000
http://localhost:30300

Login: admin / admin

🧪 Testing

pytest services/*/tests/ -v
docker exec -it mediwatch-patient-service-1 pytest tests/ -v

👩‍💻 Author

Tanisha Kushwah
DevOps Engineer | Cloud Enthusiast

GitHub: https://github.com/tanikush
LinkedIn: https://www.linkedin.com/in/tanisha-kushwah-280944284/

📄 License

This project is licensed under the MIT License.

---

## ✅ Project Complete - April 2026

- 3 Hospital Microservices ✅
- Docker & Docker Compose ✅
- Jenkins CI/CD Pipeline ✅
- Prometheus + Grafana Monitoring ✅
- GitHub Integration ✅

Built by Tanisha Kushwah


---


