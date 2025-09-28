#!/bin/bash

# DevSecOps Deployment Script
# This script demonstrates a secure deployment process

set -euo pipefail

# Configuration
APP_NAME="task-api"
VERSION=${1:-"latest"}
ENVIRONMENT=${2:-"staging"}

echo "🚀 Starting deployment of $APP_NAME:$VERSION to $ENVIRONMENT"

# Pre-deployment security checks
echo "🔒 Running pre-deployment security checks..."

# Check for secrets in code
echo "  - Scanning for secrets..."
if command -v trufflehog &> /dev/null; then
    trufflehog filesystem . --only-verified || {
        echo "❌ Secret scan failed! Deployment aborted."
        exit 1
    }
fi

# Run security linting
echo "  - Running security linting..."
if command -v bandit &> /dev/null; then
    bandit -r . -ll || {
        echo "❌ Security linting failed! Deployment aborted."
        exit 1
    }
fi

# Check dependencies for vulnerabilities
echo "  - Checking dependencies..."
if command -v safety &> /dev/null; then
    safety check || {
        echo "❌ Dependency check failed! Deployment aborted."
        exit 1
    }
fi

echo "✅ Security checks passed!"

# Build application
echo "📦 Building application..."
if [ -f "Dockerfile" ]; then
    docker build -t $APP_NAME:$VERSION .
    echo "✅ Docker image built successfully"
else
    echo "📁 Creating deployment package..."
    mkdir -p dist
    cp app.py requirements.txt dist/
    tar -czf ${APP_NAME}-${VERSION}.tar.gz dist/
    echo "✅ Deployment package created"
fi

# Run tests
echo "🧪 Running tests..."
if command -v pytest &> /dev/null; then
    pytest --cov=. --cov-fail-under=80 || {
        echo "❌ Tests failed! Deployment aborted."
        exit 1
    }
    echo "✅ All tests passed!"
fi

# Container security scan (if Docker is used)
if [ -f "Dockerfile" ]; then
    echo "🔍 Scanning container for vulnerabilities..."
    if command -v trivy &> /dev/null; then
        trivy image --exit-code 1 --severity HIGH,CRITICAL $APP_NAME:$VERSION || {
            echo "❌ Container security scan failed! Deployment aborted."
            exit 1
        }
        echo "✅ Container security scan passed!"
    fi
fi

# Deploy based on environment
echo "🌍 Deploying to $ENVIRONMENT environment..."

case $ENVIRONMENT in
    "staging")
        echo "  - Deploying to staging..."
        # Add staging deployment commands here
        # Example: kubectl apply -f k8s/staging/
        echo "  - Running smoke tests..."
        # Add smoke test commands here
        ;;
    "production")
        echo "  - Deploying to production..."
        # Add production deployment commands here
        # Example: kubectl apply -f k8s/production/
        echo "  - Running health checks..."
        # Add health check commands here
        ;;
    *)
        echo "❌ Unknown environment: $ENVIRONMENT"
        exit 1
        ;;
esac

echo "✅ Deployment completed successfully!"
echo "📊 Deployment Summary:"
echo "  - Application: $APP_NAME"
echo "  - Version: $VERSION"
echo "  - Environment: $ENVIRONMENT"
echo "  - Timestamp: $(date)"

# Post-deployment monitoring setup
echo "📈 Setting up monitoring..."
echo "  - Health check endpoint: /health"
echo "  - Logs location: /var/log/$APP_NAME"
echo "  - Metrics endpoint: /metrics (if available)"

echo "🎉 Deployment process completed!"
