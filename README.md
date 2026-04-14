
---

```markdown
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
- [Architecture](#-architecture)
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

Hospitals rely on critical software systems such as patient management, lab processing, and appointment scheduling. However:

- ⏱️ Average downtime: **45+ minutes**
- 🚨 Failures detected manually
- 🏥 Delays in patient care
- 📉 No automated alerting or recovery

---

## 💡 Solution Overview

**MediWatch** is a DevOps-driven platform that:

- ✅ Detects failures in real-time  
- ✅ Automatically triggers rollback when error rate exceeds **5%**  
- ✅ Reduces recovery time from **45 minutes → < 2 minutes**  
- ✅ Enables zero-downtime deployments  

---

## 📸 Screenshots

### 🏗️ Architecture Diagram
![Architecture](MediWatch%20hospital%20platform%20architecture.png)

---

### 🐳 Docker Services Running
![Docker PS](docker-ps.png)

---

### 📜 Service Logs
![Docker Logs](docker-logs.png)

---

### ❤️ Health Checks

**Service 1**
![Health Check 1](Health%20Check%202.png)

**Service 2**
![Health Check 2](Health%20Check%203.png)

---

### 🔗 API Testing
![API Test](api-test.png)

---

### 📊 Prometheus Metrics
![Prometheus](prometheus-metrics.png)



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
- Linting using `flake8`
- Unit testing with `pytest`
- Docker image build & push to AWS ECR
- Kubernetes rolling deployment
- GitHub webhook integration

### 🎯 Microservices Architecture
- **Patient Service**
- **Lab Service**
- **Appointment Service**

Each service includes:
- `/health` endpoint  
- `/metrics` endpoint  

---

### 📊 Monitoring & Observability
- Prometheus scraping every **15 seconds**
- Grafana dashboards:
  - Uptime %
  - Requests/sec
  - P95 latency
  - Pod restarts
- Real-time alerting

---

### 🔧 Self-Healing System
- Auto-remediation script (Python)
- Rollback triggered when:
  - Error rate > 5%
  - Health check fails
  - Pod restarts exceed threshold
- Incident logging enabled

---

### ⚡ High Availability
- Kubernetes HPA enabled
- Auto-scaling (CPU threshold: 70%)
- 1–4 replicas per service
- Rolling updates (zero downtime)

---

## 📁 Project Structure

```

mediwatch/
├── services/
│   ├── patient-service/
│   ├── lab-service/
│   └── appointment-service/
├── kubernetes/
├── jenkins/
├── ansible/
├── remediation/
├── scripts/
├── docker-compose.yml
└── README.md

````

---

## 🚀 Quick Start

### Prerequisites
- Docker installed
- Git installed
- Minimum 8GB RAM
- Ports: 5001–5003, 5432, 9090, 3000

---

### ▶️ Run Locally

```bash
# Clone repo
git clone https://github.com/tanikush/MediWatch
cd MediWatch

# Start services
docker-compose up -d

# Initialize database
cat scripts/init-db.sql | docker exec -i mediwatch-postgres-1 psql -U postgres

# Verify
docker ps
````

---

### 🔍 Health Check

```bash
curl http://localhost:5001/health
curl http://localhost:5002/health
curl http://localhost:5003/health
```

---

## 🌐 Deployment

### AWS + Kubernetes

```bash
# Provision infra
ansible-playbook ansible/provision.yml -i ansible/inventory.ini

# SSH into EC2
ssh -i ~/.ssh/mediwatch-key.pem ubuntu@YOUR_EC2_IP

# Deploy
git clone https://github.com/tanikush/MediWatch.git
cd MediWatch

docker-compose build

kubectl apply -f kubernetes/
kubectl apply -f kubernetes/monitoring/

kubectl get pods
kubectl get services
```

---

## 📊 Monitoring

### Prometheus

* [http://localhost:9090](http://localhost:9090) (Docker)
* [http://localhost:30090](http://localhost:30090) (K8s)

### Grafana

* [http://localhost:3000](http://localhost:3000) (Docker)
* [http://localhost:30300](http://localhost:30300) (K8s)

**Default Login:**
`admin / admin`

---

## 🧪 Testing

```bash
# Run all tests
pytest services/*/tests/ -v

# Test via Docker
docker exec -it mediwatch-patient-service-1 pytest tests/ -v
```

---

### 🔧 Utility Scripts

```bash
# Health check
bash scripts/health-check.sh

# Rollback
bash scripts/rollback.sh patient-service
bash scripts/rollback.sh all
```

---

## 👩‍💻 Author

**Tanisha Kushwah**
DevOps Engineer | Cloud Enthusiast

* GitHub: [https://github.com/tanikush](https://github.com/tanikush)
* LinkedIn: [https://www.linkedin.com/in/tanisha-kushwah-280944284/](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is licensed under the **MIT License**.

```

---

## 🔥 What I improved (important for you)
- Clean **professional formatting (industry standard)**
- Fixed **headings consistency**
- Removed clutter + improved readability
- Proper **code blocks & spacing**
- Better **flow (Problem → Solution → Architecture → Deploy)**
- Resume-ready 💯

---

If you want next level 🚀  
I can:
- Add **architecture diagram (like you showed earlier)**
- Add **GIF demo / screenshots section**
- Make it **top-tier GitHub portfolio (recruiter ready)**
```
