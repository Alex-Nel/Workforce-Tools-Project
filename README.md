# Task Management API - Workforce Tools Project

## Architecture Overview

This project is a containerized REST API for task management, built with a CI/CD pipeline for automated building, testing, and deployment.


- **Flask API container** — Serves REST endpoints for creating, reading, and deleting tasks.
- **PostgreSQL container** — Stores task data persistently. Includes a healthcheck so the API only starts after the database is ready.
- **Docker Compose** — Orchestrates both containers on a shared bridge network with a named volume for database storage.
- **Jenkins** — Automates the full lifecycle: pulling code, building images, running integration tests, confirming deployment, and tearing down the environment.

## Tools Used

| Tool | Purpose |
|------|---------|
| **Python 3.9 / Flask** | REST API framework |
| **PostgreSQL 15** | Relational database for task storage |
| **psycopg2** | Python adapter for PostgreSQL |
| **Docker** | Containerization of the API and database |
| **Docker Compose** | Multi-container orchestration |
| **Jenkins** | CI/CD pipeline automation |
| **GitHub** | Source control and collaboration |

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/tasks` | Retrieve all tasks |
| `POST` | `/tasks` | Create a new task (body: `{"name": "..."}`) |
| `DELETE` | `/tasks/<id>` | Delete a task by its ID |

## Setup Steps

### Prerequisites

- Docker and Docker Compose installed
- Python 3.9+ (for running tests locally)
- Jenkins (for CI/CD pipeline)

### Running the Application

1. Clone the repository:
   ```bash
   git clone https://github.com/Alex-Nel/Workforce-Tools-Project.git
   cd Workforce-Tools-Project
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build -d
   ```

3. Verify the API is running:
   ```bash
   curl http://localhost:5000/tasks
   ```

4. Create a task:
   ```bash
   curl -X POST http://localhost:5000/tasks \
     -H "Content-Type: application/json" \
     -d '{"name": "My first task"}'
   ```

5. Delete a task:
   ```bash
   curl -X DELETE http://localhost:5000/tasks/1
   ```

6. Stop and clean up:
   ```bash
   docker-compose down -v
   ```

### Running Integration Tests

With the containers running:

```bash
pip install requests
python tests/test_api.py
```

The test suite performs all API tests in test_api: creates a task, reads it back, deletes it, and confirms deletion.

## Jenkins Pipeline Stages

| Stage | Description |
|-------|-------------|
| **Checkout** | Pulls the latest code from GitHub |
| **Build** | Builds Docker images using `docker-compose build` |
| **Verify** | Starts containers and runs the integration test suite |
| **Deploy** | Confirms the application is running and displays container status |
| **Teardown** (post) | Stops all containers and removes volumes regardless of pipeline outcome |

## Demo Screenshots

enter screenshots here

<!-- add screenshots here:
- Jenkins pipeline with all stages passing
- API responses (POST, GET, DELETE) using curl 
- docker-compose ps showing running containers
- integration test output showing all tests passed
-->
