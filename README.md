# 🚀 DevOps Deployment Tracker

A full-stack DevOps project built with Flask, Docker, AWS ECS Fargate, Terraform, and GitHub Actions CI/CD.

## 📌 Overview

DevOps Deployment Tracker is a web application that allows teams to manage and track application deployments across multiple environments.

Users can:

- Create deployments
- Edit deployments
- Delete deployments
- Track deployment status
- Monitor deployment history
- View deployment statistics

---

## 🛠 Technologies Used

### Backend
- Python
- Flask
- SQLAlchemy
- Gunicorn

### Frontend
- HTML
- Bootstrap 5
- Jinja2

### DevOps
- Docker
- GitHub Actions
- Terraform

### AWS Services
- Amazon ECS Fargate
- Amazon ECR
- Application Load Balancer
- IAM
- VPC
- Security Groups

---

## ✨ Features

### Deployment Dashboard

- Total Deployments
- Successful Deployments
- Failed Deployments

### Deployment Management

- Create Deployment
- Edit Deployment
- Delete Deployment

### Environment Support

- Development
- Staging
- Production

### Status Tracking

- Success
- Failed
- Rollback

---

## 🏗 Architecture

```text
Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions CI/CD
   │
   ▼
Amazon ECR
   │
   ▼
Amazon ECS Fargate
   │
   ▼
Application Load Balancer
   │
   ▼
Flask Application
   │
   ▼
SQLite Database
```

---

## 📂 Project Structure

```text
DevOps-Deployment-Tracker/
│
├── app.py
├── models.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── templates/
│   ├── dashboard.html
│   ├── new_deployment.html
│   └── edit_deployment.html
│
├── terraform/
│
└── screenshots/
```

---

## 🐳 Docker

Build Image

```bash
docker build -t devops-tracker .
```

Run Container

```bash
docker run -p 5000:5000 devops-tracker
```

---

## ☁️ Infrastructure Provisioned with Terraform

- VPC
- Public Subnets
- Internet Gateway
- Route Tables
- Security Groups
- ECS Cluster
- ECS Service
- ECS Task Definition
- Application Load Balancer
- Target Group
- ECR Repository

---

## 🔄 CI/CD Pipeline

GitHub Actions automatically:

1. Builds Docker image
2. Pushes image to Amazon ECR
3. Updates ECS service
4. Deploys latest application version

---

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### New Deployment
![New Deployment](screenshots/new%20deployment.png)

### Edit Deployment
![Edit Deployment](screenshots/edit%20deployment.png)

### ECS Deployment
![ECS](screenshots/ecs.png)

### ECR Repository
![ECR](screenshots/ecr.png)

### Project Structure
![VS Code](screenshots/vs%20code.png)

---

## 🎯 Skills Demonstrated

- Linux
- Git & GitHub
- Python
- Flask
- SQLAlchemy
- Docker
- AWS ECS
- AWS ECR
- AWS IAM
- Application Load Balancer
- Terraform
- Infrastructure as Code
- GitHub Actions
- CI/CD

---

## 👨‍💻 Author

Badal Senchury

GitHub:
https://github.com/Badal-sen

LinkedIn:
https://www.linkedin.com/in/badal-senchury-78858b3a4/

---

## 🚀 Future Improvements

- CloudWatch Monitoring
- RDS PostgreSQL
- HTTPS & Custom Domain
- Prometheus & Grafana
- Kubernetes (EKS)
- Auto Scaling

---

**Project Status:** Completed and deployed on AWS ECS Fargate with automated CI/CD.
