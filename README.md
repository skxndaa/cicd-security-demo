# DevSecOps Task Management API

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=YOUR_PROJECT_KEY&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=YOUR_PROJECT_KEY)
[![Coverage](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO/branch/main/graph/badge.svg)](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=YOUR_PROJECT_KEY&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=YOUR_PROJECT_KEY)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive DevSecOps demonstration project featuring a Flask-based Task Management API with integrated CI/CD pipeline, security scanning, and quality gates.

## 🚀 Features

- **RESTful API** for task management (CRUD operations)
- **Comprehensive Security Scanning** with multiple tools
- **Automated CI/CD Pipeline** with GitHub Actions
- **Code Quality Gates** with linting and formatting
- **Test Coverage** with pytest and coverage reporting
- **Container Security** with Trivy scanning
- **Secret Detection** with TruffleHog
- **Dependency Security** with Safety checks
- **Static Code Analysis** with Bandit and CodeQL

## 🛡️ Security Features

### Implemented Security Measures

- **Secret Scanning**: TruffleHog OSS for detecting exposed secrets
- **Static Application Security Testing (SAST)**: Bandit for Python security issues
- **Dependency Scanning**: Safety for known vulnerabilities in dependencies
- **Container Security**: Trivy for container image vulnerabilities
- **Code Quality Analysis**: CodeQL for advanced security and quality analysis
- **Security Gates**: Pipeline fails if critical security issues are found

### Security Tools Integration

| Tool | Purpose | Status |
|------|---------|--------|
| TruffleHog | Secret Detection | ✅ Integrated |
| Bandit | Python Security Linting | ✅ Integrated |
| Safety | Dependency Vulnerability Scanning | ✅ Integrated |
| CodeQL | Advanced Security Analysis | ✅ Integrated |
| Trivy | Container Security Scanning | ✅ Integrated |

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check endpoint |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get a specific task |
| PUT | `/tasks/{id}` | Update a specific task |
| DELETE | `/tasks/{id}` | Delete a specific task |

## 🏗️ CI/CD Pipeline

The pipeline includes the following stages:

### 1. Security & Quality Analysis
- **Secret Scanning** with TruffleHog
- **Security Linting** with Bandit
- **Dependency Security** with Safety
- **Code Formatting** with Black
- **Code Linting** with Flake8

### 2. Testing
- **Unit Tests** with pytest
- **Coverage Reporting** with codecov
- **Multi-version Testing** (Python 3.8, 3.9, 3.10)

### 3. Advanced Security Analysis
- **CodeQL Analysis** for security and quality
- **SARIF Report Generation**

### 4. Build & Package
- **Application Packaging**
- **Artifact Generation**

### 5. Container Security
- **Docker Image Building**
- **Trivy Vulnerability Scanning**

### 6. Deployment (Optional)
- **Staging Deployment**
- **Smoke Testing**

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip
- Docker (optional)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cicd
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Test the API**
   ```bash
   curl http://localhost:5000/health
   ```

### Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=html

# Run security scan
bandit -r .

# Run linting
flake8 .

# Format code
black .
```

### Docker Deployment

```bash
# Build image
docker build -t task-api .

# Run container
docker run -p 5000:5000 task-api

# Health check
curl http://localhost:5000/health
```

## 📊 Code Quality Metrics

- **Test Coverage**: Target >90%
- **Code Quality**: Flake8 compliant
- **Security**: No high/critical vulnerabilities
- **Dependencies**: All dependencies up-to-date and secure

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_ENV` | Flask environment | `development` |
| `FLASK_APP` | Flask application entry point | `app.py` |
| `PORT` | Application port | `5000` |

### Security Configuration

- **Bandit**: Configured in `.bandit` file
- **Flake8**: Configured in `.flake8` file
- **Black**: Configured in `pyproject.toml`
- **Pytest**: Configured in `pyproject.toml`

## 📈 Monitoring & Observability

- **Health Check Endpoint**: `/health`
- **Application Logging**: Structured logging with Python logging
- **Error Handling**: Comprehensive error responses
- **Status Codes**: RESTful HTTP status codes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Ensure all security scans pass
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [GitHub Repository](https://github.com/YOUR_USERNAME/YOUR_REPO)
- [CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions)
- [Security Dashboard](https://github.com/YOUR_USERNAME/YOUR_REPO/security)
- [Code Coverage](https://codecov.io/gh/YOUR_USERNAME/YOUR_REPO)

## 📞 Support

For support and questions:

- Create an [Issue](https://github.com/YOUR_USERNAME/YOUR_REPO/issues)
- Check the [Documentation](https://github.com/YOUR_USERNAME/YOUR_REPO/wiki)
- Review [Security Guidelines](SECURITY.md)

---

**Built with ❤️ for DevSecOps Excellence**
