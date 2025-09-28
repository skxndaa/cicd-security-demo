# Contributing to DevSecOps Task API

Thank you for your interest in contributing to our DevSecOps demonstration project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Clone your fork
git clone https://github.com/YOUR_USERNAME/devsecops-task-api.git
cd devsecops-task-api
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest pytest-cov flake8 black bandit safety
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number
```

## 📋 Development Guidelines

### Code Style

- **Python Style**: Follow PEP 8 guidelines
- **Line Length**: Maximum 127 characters
- **Formatting**: Use Black for code formatting
- **Linting**: Code must pass Flake8 checks

```bash
# Format code
black .

# Check linting
flake8 .
```

### Security Requirements

All contributions must pass security checks:

```bash
# Security linting
bandit -r .

# Dependency security check
safety check

# Secret scanning (if available)
trufflehog filesystem . --only-verified
```

### Testing Requirements

- **Coverage**: Minimum 80% test coverage
- **Test Types**: Unit tests for all new functionality
- **Test Naming**: Use descriptive test names

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Documentation

- Update README.md for significant changes
- Add docstrings for new functions/classes
- Update API documentation for endpoint changes
- Include examples in docstrings

## 🔒 Security Considerations

### Secure Coding Practices

1. **Input Validation**: Always validate and sanitize user inputs
2. **Error Handling**: Don't expose sensitive information in error messages
3. **Logging**: Log security-relevant events appropriately
4. **Dependencies**: Keep dependencies updated and secure

### Security Review Process

1. All code changes undergo security review
2. Automated security scans must pass
3. No secrets or sensitive data in code
4. Follow OWASP security guidelines

## 🧪 Testing Guidelines

### Test Structure

```python
class TestFeatureName:
    """Test class for specific feature"""
    
    def setup_method(self):
        """Setup before each test"""
        pass
    
    def test_specific_functionality(self):
        """Test specific functionality with descriptive name"""
        # Arrange
        # Act
        # Assert
        pass
```

### Test Categories

- **Unit Tests**: Test individual functions/methods
- **Integration Tests**: Test component interactions
- **Security Tests**: Test security-related functionality
- **API Tests**: Test REST API endpoints

## 📝 Commit Guidelines

### Commit Message Format

```
type(scope): brief description

Detailed description of changes (if needed)

Fixes #issue-number
```

### Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `security`: Security-related changes
- `ci`: CI/CD pipeline changes

### Examples

```bash
feat(api): add task priority field to task model

Add priority field (high, medium, low) to task creation and updates.
Includes validation and API documentation updates.

Fixes #123
```

## 🔄 Pull Request Process

### Before Submitting

1. **Run all checks locally**:
   ```bash
   # Format code
   black .
   
   # Run linting
   flake8 .
   
   # Run security checks
   bandit -r .
   safety check
   
   # Run tests
   pytest --cov=. --cov-fail-under=80
   ```

2. **Update documentation** if needed
3. **Add tests** for new functionality
4. **Update CHANGELOG.md** if applicable

### PR Template

When creating a PR, include:

- **Description**: What changes were made and why
- **Testing**: How the changes were tested
- **Security**: Any security considerations
- **Breaking Changes**: Any breaking changes
- **Screenshots**: For UI changes (if applicable)

### Review Process

1. **Automated Checks**: All CI/CD checks must pass
2. **Security Review**: Security team review for security-related changes
3. **Code Review**: At least one maintainer review required
4. **Testing**: Verify tests pass and coverage is maintained

## 🐛 Bug Reports

### Before Reporting

1. Check existing issues
2. Verify it's reproducible
3. Test with latest version

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Ubuntu 20.04]
- Python: [e.g., 3.9.7]
- Version: [e.g., 1.0.0]

**Additional Context**
Any other relevant information
```

## 💡 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature

**Use Case**
Why is this feature needed?

**Proposed Solution**
How should this feature work?

**Alternatives Considered**
Other solutions you've considered

**Additional Context**
Any other relevant information
```

## 📞 Getting Help

- **Documentation**: Check the README and wiki
- **Issues**: Search existing issues
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Use security@example.com for security issues

## 🏆 Recognition

Contributors will be recognized in:

- CONTRIBUTORS.md file
- Release notes
- GitHub contributors section

Thank you for contributing to DevSecOps excellence! 🚀
