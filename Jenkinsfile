pipeline {
    agent any

    environment {
        // Define your Docker Hub or local image name
        IMAGE_NAME = "my-task-api"
    }

    stages {
        stage('Checkout') {
            steps {
                // This pulls the code from the repo that triggered the build
                checkout scm
                echo "Successfully pulled code from GitHub."
            }
        }

        stage('Build') {
            steps {
                echo "Building application with Docker Compose..."
                // Build the services defined in docker-compose.yml
                sh 'docker-compose build'
            }
        }

        stage('Verify') {
            steps {
                echo "Running integration tests..."
                // We'll add actual test commands here in Part 2
                sh 'docker-compose up -d'
                // Add a health check or simple curl here
                sh 'docker-compose down'
            }
        }
    }
}
