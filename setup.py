"""
Setup script for the DevSecOps Task Management API
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="devsecops-task-api",
    version="1.0.0",
    author="DevSecOps Team",
    author_email="devsecops@example.com",
    description="A comprehensive DevSecOps demonstration with Flask Task Management API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/devsecops-task-api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Security",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.2",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "black>=23.7.0",
            "bandit>=1.7.5",
            "safety>=2.3.4",
        ],
    },
    entry_points={
        "console_scripts": [
            "task-api=app:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/devsecops-task-api/issues",
        "Source": "https://github.com/yourusername/devsecops-task-api",
        "Documentation": "https://github.com/yourusername/devsecops-task-api/wiki",
    },
)
