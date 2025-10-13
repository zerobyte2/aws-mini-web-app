# 🚀 AWS Mini Web App - Full Stack Cloud Deployment

A production-ready Flask web application deployed on AWS cloud infrastructure using Docker containers, ECR, EC2 instances, Auto Scaling, Application Load Balancer, DynamoDB, and S3.

![AWS Architecture](https://img.shields.io/badge/AWS-Cloud--Architecture-orange)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-lightblue)

## 📋 Project Overview

This project demonstrates a complete microservices deployment on AWS, featuring a Flask application that maintains a visit counter in DynamoDB and handles file uploads to S3. The infrastructure is designed for high availability and scalability using AWS best practices.

### ✨ Features
- **📊 Visit Counter**: Real-time counter stored in DynamoDB
- **📁 File Upload**: Secure file uploads to Amazon S3
- **🚦 Health Monitoring**: Application health checks
- **⚡ Auto Scaling**: Automatic scaling based on demand
- **🔀 Load Balancing**: Distributed traffic across instances
- **🐳 Containerized**: Docker-based deployment
- **🔒 Secure**: IAM roles with least privilege

## 🏗️ System Architecture
- Internet Users
- ↓
- Application Load Balancer (ALB)
- ↓
- Auto Scaling Group (ASG)
- ↓
- EC2 Instances (Docker Containers)
- ├── DynamoDB (Visit Counter)
- └── S3 Bucket (File Storage)


## 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| **Backend** | Python, Flask, Boto3 |
| **Container** | Docker, Amazon ECR |
| **Compute** | EC2, Auto Scaling Groups |
| **Network** | Application Load Balancer, Security Groups |
| **Storage** | DynamoDB, S3 |
| **Security** | IAM Roles, Security Groups |
| **Infrastructure** | Launch Templates, Target Groups |

## 📁 Project Structure
    aws-mini-web-app/
    ├── app/
    │ ├── app.py # Flask application
    │ └── requirements.txt # Python dependencies
    ├── infrastructure/
    │ └── user-data.sh # EC2 bootstrap script
    ├── docs/
    │ ├── architecture.md # Detailed architecture
    │ ├── setup-guide.md # Step-by-step setup
    │ └── troubleshooting.md # Common issues & solutions
    ├── Dockerfile # Container configuration
    ├── .gitignore # Git ignore rules
    └── README.md # Project documentation


## 🚀 Quick Start

### Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Docker installed
- Python 3.11+

### Local Development
```bash
# Clone the repository
git clone https://github.com/zDR34M/aws-mini-web-app.git
cd aws-mini-web-app

# Build Docker image
docker build -t miniapp .

# Run locally
docker run -p 5000:5000 -e DDB_TABLE=test -e S3_BUCKET=test miniapp

# Test endpoints
curl http://localhost:5000/health
# Output: ok

curl http://localhost:5000/count
# Output: {"count": 1}
```

## 📡 API Endpoints

| Method | Endpoint |	Description	| Response |
|--------|----------|-------------|----------|
| **GET** | /health | Health check |	ok |
| **GET** | /count | Increment & return visit counter |	{"count": N} |
| **POST** | /upload | Upload file to S3 |	{"uploaded": "filename"} |

## Example Usage

### Health check
    curl http://your-alb-dns/health

### Visit counter
    curl http://your-alb-dns/count

### File upload
    curl -X POST -F "file=@document.pdf" http://your-alb-dns/upload

## 🔧 AWS Deployment

## Infrastructure Setup

    ECR Repository: Create private repository for Docker images

    DynamoDB Table: visits table with pk as partition key

    S3 Bucket: miniapp-uploads-* for file storage

    IAM Role: MiniAppEC2Role with ECR, DynamoDB, and S3 permissions

    Security Groups: ALB-SG (HTTP) and EC2-SG (port 5000)

    Load Balancer: MiniApp-ALB with target group

    Auto Scaling: Launch template with user data script

## Deployment Commands
    # Build and push to ECR
    docker build -t miniapp .
    docker tag miniapp:latest <account-id>.dkr.ecr.eu-central-1.amazonaws.com/miniapp:latest
    docker push <account-id>.dkr.ecr.eu-central-1.amazonaws.com/miniapp:latest

## ⚙️ Configuration

| Variable | Description |	Default	|
|----------|-------------|----------|
| **AWS_REGION** | AWS region | eu-central-1 |
| **DDB_TABLE** | DynamoDB table name | Required |
| **S3_BUCKET** | S3 bucket for uploads | Required |

## Security Groups

  - ALB-SG: Inbound HTTP (80) from 0.0.0.0/0
  - EC2-SG: Inbound port 5000 from ALB-SG only

## 🧪 Testing

### Manual Testing
    # Health endpoint
    curl http://<ALB-DNS>/health
    
    # Count endpoint (increments on each call)
    curl http://<ALB-DNS>/count
    
    # File upload
    curl -X POST -F "file=@test.txt" http://<ALB-DNS>/upload

### Verification

    ✅ Check DynamoDB table for incrementing counter

    ✅ Verify uploaded files in S3 bucket

    ✅ Monitor EC2 instance health in Target Group

    ✅ Review CloudWatch logs for errors

## 🐛 Troubleshooting
### Common Issues

    503 Service Unavailable: Check Target Group health status
    Docker not starting: Verify user data script execution
    IAM permissions: Confirm EC2 instance role attachments
    Security groups: Validate inbound rules

### Debugging Commands
    # Check container status
    docker ps
    
    # View application logs
    docker logs <container_id>
    
    # Check health endpoint
    curl http://localhost:5000/health

## 📈 Monitoring & Logs

  - Application Load Balancer: Access logs and metrics

  - CloudWatch: Instance metrics and Docker logs

  - DynamoDB: Table metrics and capacity monitoring

  - S3: Access logs and storage metrics

## 🔒 Security Considerations

  - IAM roles with least privilege principles

  - Security groups restricting unnecessary access

  - Private ECR repository for container images

  - No sensitive data in user data scripts

  - Regular security updates on EC2 instances

## 🤝 Contributing

  - Fork the repository

  - Create a feature branch (git checkout -b feature/amazing-feature)

  - Commit your changes (git commit -m 'Add amazing feature')

  - Push to the branch (git push origin feature/amazing-feature)

  - Open a Pull Request

## 📄 License
### This project is licensed under the MIT License - see the LICENSE file for details.

- GitHub: @zDR34M
- Project: AWS Mini Web App

## 🙏 Acknowledgments

  - AWS Documentation and Services

  - Flask Framework

  - Docker Community

  - Cloud Computing Best Practices

<div align="center">

⭐ If you found this project helpful, please give it a star! ⭐
</div>

