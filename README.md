
## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Containerization**: Docker
- **AWS Services**:
  - ECR (Elastic Container Registry)
  - EC2 (Elastic Compute Cloud)
  - ALB (Application Load Balancer)
  - Auto Scaling Groups
  - DynamoDB (NoSQL Database)
  - S3 (Simple Storage Service)
  - IAM (Identity and Access Management)

## 📋 Prerequisites

- AWS Account
- AWS CLI configured
- Docker installed
- Python 3.11+

## 🚀 Deployment Steps

### 1. Build and Push Docker Image
```bash
docker build -t miniapp .
docker tag miniapp:latest <account-id>.dkr.ecr.eu-central-1.amazonaws.com/miniapp:latest
docker push <account-id>.dkr.ecr.eu-central-1.amazonaws.com/miniapp:latest ```

### 2. AWS Infrastructure Setup
    Create ECR repository
    Create DynamoDB table (visits)
    Create S3 bucket for uploads
    Create IAM roles and policies
    Configure security groups
    Set up Load Balancer and Auto Scaling

### 3. Application Endpoints
    GET /health - Health check
    GET /count - Visit counter (increments DynamoDB)
    POST /upload - File upload to S3

### 🔧 Configuration
Environment variables required:
    AWS_REGION: AWS region (default: eu-central-1)
    DDB_TABLE: DynamoDB table name
    S3_BUCKET: S3 bucket name for uploads

### 📊 Architecture Diagram
Internet → ALB → Auto Scaling Group → EC2 Instances → Docker Containers
                    ↓              ↓
               DynamoDB (count)  S3 (uploads)

### 🧪 Testing
    # Health check
    curl http://<alb-dns>/health

    # Test counter
    curl http://<alb-dns>/count

    # Test file upload
    curl -X POST -F "file=@test.txt" http://<alb-dns>/upload

### 📝 Lessons Learned
    Containerized application deployment on AWS
    Infrastructure as Code concepts
    Auto Scaling and Load Balancing configuration
    IAM roles and security best practices
    Multi-service integration on AWS