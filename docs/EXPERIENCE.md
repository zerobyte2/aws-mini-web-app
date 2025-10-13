# Project Experience & Learnings

## 🎯 Project Journey

### Challenges Faced
1. **Docker Installation on Amazon Linux 2023**
   - Learned that `amazon-linux-extras` doesn't work the same way in AL2023
   - Solution: Use `yum install docker` directly

2. **IAM Role Configuration**
   - Understanding the exact permissions needed for ECR, DynamoDB, and S3
   - Learned about least privilege principle

3. **Auto Scaling Group Issues**
   - Debugging why instances weren't registering with Target Groups
   - Learned to check CloudWatch logs and instance status

4. **Application Load Balancer Configuration**
   - Setting up proper health checks
   - Configuring security groups correctly

### Key Learnings
- **Infrastructure as Code**: Understanding how AWS services connect
- **Troubleshooting**: Debugging distributed systems
- **Security**: IAM roles and security groups configuration
- **Monitoring**: Using CloudWatch and ALB metrics

### Skills Demonstrated
- AWS Services: EC2, ECR, ALB, Auto Scaling, DynamoDB, S3, IAM
- Containerization: Docker, ECR
- Python: Flask application development
- DevOps: CI/CD concepts, infrastructure management