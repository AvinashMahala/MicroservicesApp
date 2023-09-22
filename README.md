# Project Title

Microservices-Based Web Application with Django, Flask, and React

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Prerequisites](#prerequisites)
  - [Setting Up Django](#setting-up-django)
    - [Installing Django and Dependencies](#installing-django-and-dependencies)
  - [Connecting Django with MySQL and Docker](#connecting-django-with-mysql-and-docker)
  - [Setting Up Flask](#setting-up-flask)
    - [Installing Flask and Dependencies](#installing-flask-and-dependencies)
    - [Running Flask App](#running-flask-app)
  - [Connecting Flask with MySQL and Docker](#connecting-flask-with-mysql-and-docker)
  - [RabbitMQ Setup](#rabbitmq-setup)
  - [Django Producer and Consumer](#django-producer-and-consumer)
  - [Flask Producer and Consumer](#flask-producer-and-consumer)
  - [Queue Service](#queue-service)
  - [Data Consistency](#data-consistency)
  - [Internal HTTP Requests](#internal-http-requests)
  - [Finishing the Python Apps](#finishing-the-python-apps)
  - [React Setup](#react-setup)
  - [Products CRUD](#products-crud)
  - [Completing the Main App](#completing-the-main-app)
  - [Important Docker Commands](#important-docker-commands)

## Introduction

This project demonstrates the creation of a microservices-based web application using Django, Flask, and React. It involves setting up the backend services with Docker, connecting them to MySQL databases, implementing RabbitMQ for message queuing, and creating a React-based frontend for CRUD operations.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed:

- Docker
- Python 3.x
- Node.js
- MySQL
- RabbitMQ (AMQP URL)
- MySQL Workbench

## Setting Up Django

1. Create a GitHub repository for your Django project.
2. Publish the repository.

### Installing Django and Dependencies

3. Open a terminal and run the following commands to install Django and required packages:

```bash
pip install django
pip install djangorestframework
```

4. Initialize a Django project:

```bash
django-admin startproject admin
cd admin
python3 manage.py runserver
```

5. Once the server is running, open a web browser and ensure that everything works as expected.

## Connecting Django with MySQL and Docker

6. Create a Dockerfile and docker-compose.yml inside the "admin" directory.
7. Create a requirements.txt file inside the "admin" directory to list all dependencies.
8. Install Docker if not already present:

```bash
# For Windows using Chocolatey
choco install docker-for-windows
```

9. Run Docker Desktop with administrative privileges.
10. Ensure Docker is up and running, fixing any issues if encountered.
11. Open a terminal and run:

```bash
docker-compose up
```

12. Verify that your Django app is running inside a Docker container.

## Setting Up Flask

1. Create a directory for your Flask app.
2. Create a main.py file in the Flask app directory.

### Installing Flask and Dependencies

3. In the Flask app's requirements.txt file, add the following dependencies:

```
# requirements.txt
Flask==x.x
# Add any other dependencies here
```

4. Create a Dockerfile similar to the one in the "admin" directory with appropriate changes.

```Dockerfile
# Dockerfile for Flask
# ...
CMD python main.py
```

5. Build the Docker image:

```bash
docker build -t flask-app .
```

### Running Flask App

6. Run the Flask app outside of Docker to verify it works:

```bash
python main.py
```

7. Stop the app and start it with Docker:

```bash
docker-compose up
```

8. Verify that your Flask app is running inside a Docker container.

## Connecting Flask with MySQL and Docker

1. Update the Flask app's main.py to include MySQL database configuration.
2. Modify the Dockerfile and docker-compose.yml in the Flask app's directory with appropriate changes.
3. Run the Flask app inside a Docker container:

```bash
docker-compose up
```

4. Verify that the Flask app is connected to MySQL and running successfully.

## RabbitMQ Setup

1. Set up an instance of RabbitMQ using an AMQP service. Copy the AMQP URL from the service details page.

## Django Producer and Consumer

1. Create "producer.py" and "consumer.py" files in the Django app's "products" directory.
2. Implement the necessary code for producing and consuming messages.
3. Test the producer and consumer in the Docker container using the provided instructions.

## Flask Producer and Consumer

1. Copy the "consumer.py" file from the Django app to the Flask app's directory.
2. Update the queue name in the Flask "consumer.py" to "main."
3. Update the routing key in the Django "producer.py" to "main."
4. Modify the Docker Compose files to run the consumer as a service.

## Queue Service

1. Configure the Docker Compose files to run the message queue service (RabbitMQ) as a container.
2. Ensure that the producer and consumer services can communicate with the queue service.

## Data Consistency

Implement data consistency mechanisms between microservices using transactions, error handling, or eventual consistency as needed.

## Internal HTTP Requests

Set up internal HTTP requests between microservices using appropriate libraries or frameworks like Flask's HTTP client.

## Finishing the Python Apps

Complete the implementation of views, models, and URL routing for both Django and Flask apps as required by your project.

## React Setup

1. Create a React app in the root directory using Create React App:

```bash
npx create-react-app react-crud --template typescript
```

## Products CRUD

Implement CRUD operations in your React app for managing products. Ensure that it can communicate with both the Django and Flask microservices.

## Completing the Main App

Integrate the React frontend with the Django and Flask backend services to create a fully functional microservices-based web application.

## Important Docker Commands

Here are some important Docker commands for managing your containers:

- `docker-compose up`: Start all the containers defined in the docker-compose.yml file.
- `docker-compose down`: Stop and remove services. Use `--volumes` to also remove volumes.
- `docker-compose build`: Build all the images defined in the docker-compose.yml file.
- `docker-compose ps`: List services and their status.
- `docker-compose logs`: Display logs from services. Append service name for specific logs.
- `docker-compose restart`: Restart services.
- `docker-compose stop`: Stop services without removing them.
- `docker-compose start`: Start existing containers for services.
- `docker-compose run`: Run a one-time command against a service.
- `docker-compose exec`: Execute a command in a running container.
- `docker-compose rm`: Remove stopped service containers.
- `docker-compose pull`: Pull the latest images for services.
- `docker-compose top`: Display running processes in services.
- `docker-compose config`: Validate and display the Compose configuration.
- `docker-compose pause`: Pause services.
- `docker-compose unpause`: Unpause services.
- `docker-compose kill`: Kill services.
-

 `docker-compose images`: List images used by created containers.

Please refer to the specific service directories and Docker Compose files for more detailed instructions and configurations.

This comprehensive README file should help anyone understand and reproduce your microservices-based web application project successfully. Make sure to keep it updated as your project evolves or new features are added.