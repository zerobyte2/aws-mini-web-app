#!/bin/bash
yum update -y
yum install -y docker aws-cli
systemctl enable docker
systemctl start docker

ACCOUNT_ID=<your_account_id>
REGION=eu-central-1
REPO=$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/miniapp:latest
BUCKET=miniapp-uploads-yourname
TABLE=visits

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
docker pull $REPO
docker run -d -p 5000:5000 -e AWS_REGION=$REGION -e DDB_TABLE=$TABLE -e S3_BUCKET=$BUCKET $REPO