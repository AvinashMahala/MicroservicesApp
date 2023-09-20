 ```
# MicroservicesApp

This project is a microservices architecture involving Django, Flask, MySQL, RabbitMQ, and React.

## Introduction

This document provides a step-by-step guide to setting up a microservices architecture involving Django, Flask, MySQL, RabbitMQ, and React.

## Prerequisites

Before you begin, ensure you have the following installed:

- A GitHub account
- Docker Desktop with admin privileges
- Python 3
- Pip
- Django
- Django REST Framework
- Flask
- MySQL Workbench
- RabbitMQ
- React

## Step 1: Django with Docker Setup

### 1.1. Create a GitHub Repo and publish it.

### 1.2. Install Docker if not already installed:

```bash
choco install docker-for-windows
```

### 1.3. Install Django and Django REST Framework:

```bash
pip install django
pip install djangorestframework
```

### 1.4. Start a new Django project and move to its directory:

```bash
django-admin startproject admin
cd admin
```

### 1.5. Test if everything works:

```bash
python3 manage.py runserver
```

### 1.6. Dockerization

- Create a `Dockerfile`, `docker-compose.yml`, and `requirements.txt` for your application dependencies inside the `admin` directory.
- Run Docker Desktop with admin privileges.
- Confirm Docker is running:

```bash
docker-compose up
```

## Step 2: Connect Django with MySQL

### 2.1. Remove the existing SQLite DB if present.

### 2.2. Update `docker-compose.yml` with MySQL configurations.

### 2.3. Run the Docker Compose file:

```bash
docker-compose up
```

### 2.4. MySQL Workbench Configuration

- **Connection Name**: `admin@localhost`
- **Connection Method**: LDAP User/Password
- **HostName**: `localhost`
- **Port**: `33066`
- **UserName**: `root`
- **Password**: `root`
- **Default Schema**: `admin`

### 2.5. Create a New Django App

- Enter Docker Service Terminal:

```bash
docker-compose exec backend sh
```

- Start a new app called `products`:
