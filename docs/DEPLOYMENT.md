# Deployment Guide

## Overview

This guide covers deployment strategies, procedures, and best practices for the DevTechAI WebApp v2.0 across different environments and cloud providers.

## Deployment Environments

### Development
- **Purpose**: Local development and testing
- **Infrastructure**: Docker Compose
- **Database**: Local PostgreSQL
- **Storage**: Local file system
- **Monitoring**: Basic logging

### Staging
- **Purpose**: Pre-production testing
- **Infrastructure**: Kubernetes cluster
- **Database**: Managed PostgreSQL
- **Storage**: Cloud storage (S3/GCS)
- **Monitoring**: Full observability stack

### Production
- **Purpose**: Live application
- **Infrastructure**: Multi-region Kubernetes
- **Database**: High-availability PostgreSQL
- **Storage**: Multi-region cloud storage
- **Monitoring**: Enterprise monitoring

## Prerequisites

### Required Tools
- Docker 24.0.0+
- Docker Compose 2.0.0+
- Kubernetes CLI (kubectl) 1.28+
- Helm 3.12+
- Terraform 1.6+
- AWS CLI / GCP CLI / Azure CLI

### Required Access
- Cloud provider accounts
- Container registry access
- Kubernetes cluster access
- DNS management access
- SSL certificate management

## Deployment Strategies

### 1. Blue-Green Deployment
```bash
# Deploy to green environment
kubectl apply -f k8s/green/

# Switch traffic to green
kubectl patch service app-service -p '{"spec":{"selector":{"version":"green"}}}'

# Verify deployment
kubectl get pods -l version=green

# Clean up blue environment
kubectl delete -f k8s/blue/
```

### 2. Canary Deployment
```bash
# Deploy canary version
kubectl apply -f k8s/canary/

# Gradually increase traffic
kubectl patch service app-service -p '{"spec":{"selector":{"version":"canary","weight":"10"}}}'

# Monitor metrics
kubectl get hpa app-hpa

# Promote to full deployment
kubectl apply -f k8s/production/
```

### 3. Rolling Deployment
```bash
# Update deployment
kubectl set image deployment/app-deployment app=app:v2.0.0

# Monitor rollout
kubectl rollout status deployment/app-deployment

# Rollback if needed
kubectl rollout undo deployment/app-deployment
```

## Cloud Provider Deployments

### AWS Deployment

#### 1. Infrastructure Setup
```bash
# Initialize Terraform
cd infrastructure/terraform/aws
terraform init

# Plan infrastructure
terraform plan -var-file="environments/production.tfvars"

# Apply infrastructure
terraform apply -var-file="environments/production.tfvars"
```

#### 2. Kubernetes Deployment
```bash
# Configure kubectl
aws eks update-kubeconfig --region us-east-1 --name devtechai-cluster

# Deploy application
helm install devtechai-app ./helm-charts/app \
  --namespace production \
  --set image.tag=v2.0.0 \
  --set environment=production
```

#### 3. Database Setup
```bash
# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier devtechai-prod \
  --db-instance-class db.t3.medium \
  --engine postgres \
  --master-username admin \
  --master-user-password $DB_PASSWORD

# Run migrations
kubectl exec -it deployment/app-deployment -- npm run db:migrate
```

### Google Cloud Platform Deployment

#### 1. Infrastructure Setup
```bash
# Initialize Terraform
cd infrastructure/terraform/gcp
terraform init

# Plan infrastructure
terraform plan -var-file="environments/production.tfvars"

# Apply infrastructure
terraform apply -var-file="environments/production.tfvars"
```

#### 2. Kubernetes Deployment
```bash
# Configure kubectl
gcloud container clusters get-credentials devtechai-cluster --zone us-central1-a

# Deploy application
helm install devtechai-app ./helm-charts/app \
  --namespace production \
  --set image.tag=v2.0.0 \
  --set environment=production
```

### Oracle Cloud Infrastructure Deployment

#### 1. Infrastructure Setup
```bash
# Initialize Terraform
cd infrastructure/terraform/oci
terraform init

# Plan infrastructure
terraform plan -var-file="environments/production.tfvars"

# Apply infrastructure
terraform apply -var-file="environments/production.tfvars"
```

#### 2. Kubernetes Deployment
```bash
# Configure kubectl
oci ce cluster create-kubeconfig --cluster-id $CLUSTER_ID --file ~/.kube/config

# Deploy application
helm install devtechai-app ./helm-charts/app \
  --namespace production \
  --set image.tag=v2.0.0 \
  --set environment=production
```

## CI/CD Pipeline

### GitHub Actions Workflow

#### 1. Build and Test
```yaml
name: Build and Test
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run test
      - run: npm run build
```

#### 2. Deploy to Staging
```yaml
name: Deploy to Staging
on:
  push:
    branches: [develop]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Staging
        run: |
          kubectl apply -f k8s/staging/
          kubectl rollout status deployment/app-deployment
```

#### 3. Deploy to Production
```yaml
name: Deploy to Production
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Production
        run: |
          kubectl apply -f k8s/production/
          kubectl rollout status deployment/app-deployment
```

## Database Deployment

### Migration Strategy
```bash
# Create migration
npm run db:migrate:create -- --name add-user-table

# Run migrations
npm run db:migrate

# Verify migration
npm run db:migrate:status
```

### Backup Strategy
```bash
# Create backup
pg_dump -h $DB_HOST -U $DB_USER -d $DB_NAME > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore backup
psql -h $DB_HOST -U $DB_USER -d $DB_NAME < backup_20240101_120000.sql
```

## Monitoring Deployment

### Prometheus Setup
```bash
# Deploy Prometheus
helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  --set server.persistentVolume.enabled=true
```

### Grafana Setup
```bash
# Deploy Grafana
helm install grafana grafana/grafana \
  --namespace monitoring \
  --set persistence.enabled=true \
  --set adminPassword=$GRAFANA_PASSWORD
```

### Alerting Setup
```bash
# Deploy AlertManager
helm install alertmanager prometheus-community/alertmanager \
  --namespace monitoring
```

## Security Deployment

### SSL Certificate Setup
```bash
# Create certificate
kubectl apply -f - <<EOF
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: devtechai-tls
spec:
  secretName: devtechai-tls
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  dnsNames:
  - devtechai.org
  - api.devtechai.org
EOF
```

### Security Policies
```bash
# Apply security policies
kubectl apply -f security/policies/

# Verify policies
kubectl get networkpolicies
kubectl get podsecuritypolicies
```

## Rollback Procedures

### Application Rollback
```bash
# Check rollout history
kubectl rollout history deployment/app-deployment

# Rollback to previous version
kubectl rollout undo deployment/app-deployment

# Rollback to specific revision
kubectl rollout undo deployment/app-deployment --to-revision=2
```

### Database Rollback
```bash
# Rollback migration
npm run db:migrate:rollback

# Rollback to specific migration
npm run db:migrate:rollback -- --to=20240101000000
```

## Health Checks

### Application Health
```bash
# Check pod status
kubectl get pods -l app=devtechai-app

# Check service status
kubectl get services

# Check ingress status
kubectl get ingress
```

### Database Health
```bash
# Check database connection
kubectl exec -it deployment/app-deployment -- npm run db:health

# Check database performance
kubectl exec -it deployment/app-deployment -- npm run db:stats
```

## Troubleshooting

### Common Issues

#### Pod Startup Issues
```bash
# Check pod logs
kubectl logs deployment/app-deployment

# Check pod events
kubectl describe pod <pod-name>

# Check resource usage
kubectl top pods
```

#### Database Connection Issues
```bash
# Check database status
kubectl get pods -l app=postgres

# Check database logs
kubectl logs deployment/postgres-deployment

# Test database connection
kubectl exec -it deployment/app-deployment -- npm run db:test
```

#### Service Discovery Issues
```bash
# Check service endpoints
kubectl get endpoints

# Check DNS resolution
kubectl exec -it deployment/app-deployment -- nslookup app-service

# Check network policies
kubectl get networkpolicies
```

## Performance Optimization

### Resource Optimization
```bash
# Set resource limits
kubectl patch deployment app-deployment -p '{"spec":{"template":{"spec":{"containers":[{"name":"app","resources":{"limits":{"cpu":"500m","memory":"512Mi"},"requests":{"cpu":"250m","memory":"256Mi"}}}]}}}}'

# Enable horizontal pod autoscaling
kubectl autoscale deployment app-deployment --cpu-percent=70 --min=2 --max=10
```

### Database Optimization
```bash
# Create database indexes
kubectl exec -it deployment/app-deployment -- npm run db:index

# Analyze query performance
kubectl exec -it deployment/app-deployment -- npm run db:analyze
```

## Disaster Recovery

### Backup Procedures
```bash
# Create application backup
kubectl create job backup-app-$(date +%Y%m%d) --from=cronjob/backup-app

# Create database backup
kubectl create job backup-db-$(date +%Y%m%d) --from=cronjob/backup-db
```

### Recovery Procedures
```bash
# Restore application
kubectl apply -f backup/app-backup.yaml

# Restore database
kubectl exec -it deployment/app-deployment -- npm run db:restore
```

## Maintenance

### Regular Maintenance Tasks
- Update dependencies
- Apply security patches
- Monitor resource usage
- Clean up old resources
- Review and update configurations

### Maintenance Windows
- Schedule maintenance during low-traffic periods
- Notify users in advance
- Have rollback plans ready
- Monitor during maintenance

## Support

For deployment support:
- Check deployment logs
- Review troubleshooting section
- Contact DevOps team
- Create incident ticket
