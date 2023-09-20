
---

# Microservices Project with Django, Flask, MySQL, RabbitMQ, and React

## Table of Contents

- [Microservices Project with Django, Flask, MySQL, RabbitMQ, and React](#microservices-project-with-django-flask-mysql-rabbitmq-and-react)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
- [MicroservicesApp](#microservicesapp)
  - [MicroservicesApp From freeCodeCamp.org https://www.youtube.com/watch?v=0iB5IPoTDts](#microservicesapp-from-freecodecamporg-httpswwwyoutubecomwatchv0ib5ipotdts)
  - [Django with Docker Setup](#django-with-docker-setup)
    - [Pre-requisites](#pre-requisites)
    - [Installation](#installation)
    - [Dockerization](#dockerization)
  - [Connect Django with MySQL](#connect-django-with-mysql)
    - [MySQL Workbench Configuration](#mysql-workbench-configuration)
    - [Create a New Django App](#create-a-new-django-app)
      - [Setup for the New App](#setup-for-the-new-app)
  - [Flask with Docker Setup](#flask-with-docker-setup)
    - [Create Flask App](#create-flask-app)
    - [Run Flask App with Docker](#run-flask-app-with-docker)
  - [Connect Flask with MySQL](#connect-flask-with-mysql)
    - [Update `main.py` to Connect to MySQL](#update-mainpy-to-connect-to-mysql)
    - [Run Migrations](#run-migrations)
  - [RabbitMQ Setup](#rabbitmq-setup)
  - [Data Consistency](#data-consistency)
  - [React Setup](#react-setup)
  - [Completing the Main App](#completing-the-main-app)

## Introduction

This project is aimed at setting up a microservices architecture involving Django, Flask, MySQL, RabbitMQ, and React. The following steps will guide you through each aspect of the project.
# MicroservicesApp
 MicroservicesApp From freeCodeCamp.org https://www.youtube.com/watch?v=0iB5IPoTDts
---

## Django with Docker Setup

### Pre-requisites

1. Create a GitHub Repo and publish it.
2. Install Docker if not already installed:
    ```bash
    choco install docker-for-windows
    ```

### Installation

1. Install Django and Django REST Framework:
    ```bash
    pip install django
    pip install djangorestframework
    ```

2. Start a new Django project and move to its directory:
    ```bash
    django-admin startproject admin
    cd admin
    ```

3. Test if everything works:
    ```bash
    python3 manage.py runserver
    ```

### Dockerization

1. Inside the `admin` directory, create a `Dockerfile`, `docker-compose.yml`, and `requirements.txt` for your application dependencies.
2. Run Docker Desktop with admin privileges.
3. Confirm Docker is running:
    ```bash
    docker-compose up
    ```

---

## Connect Django with MySQL

1. Remove the existing SQLite DB if present.
2. Update `docker-compose.yml` with MySQL configurations.
3. Run the Docker Compose file:
    ```bash
    docker-compose up
    ```

### MySQL Workbench Configuration

- **Connection Name**: `admin@localhost`
- **Connection Method**: LDAP User/Password
- **HostName**: `localhost`
- **Port**: `33066`
- **UserName**: `root`
- **Password**: `root`
- **Default Schema**: `admin`

### Create a New Django App

1. Enter Docker Service Terminal:
    ```bash
    docker-compose exec backend sh
    ```

2. Start a new app called `products`:
    ```bash
    python manage.py startapp products
    ```

#### Setup for the New App

1. Update `INSTALLED_APPS`, `MIDDLEWARE`, and more in `settings.py`.
2. Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

---

## Flask with Docker Setup

### Create Flask App

1. Create main directory and `main.py` for Flask app.
2. Update `requirements.txt` and `Dockerfile`.

### Run Flask App with Docker

1. Run Flask app to verify:
    ```bash
    python main.py
    ```

2. Start running Docker Compose:
    ```bash
    docker-compose up
    ```

---

## Connect Flask with MySQL

### Update `main.py` to Connect to MySQL

### Run Migrations

1. Enter Docker Service Terminal:
    ```bash
    docker-compose exec backend sh
    ```

2. Run Flask Migrations:
    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

---

## RabbitMQ Setup

*Instructions for setting up RabbitMQ*

---

## Data Consistency

*Instructions for ensuring data consistency*

---

## React Setup

*Instructions for setting up the React frontend*

---

## Completing the Main App

*Steps to complete the main application*

---
