pipeline {
    agent any

    environment {
        IMAGE_NAME = "task-management-api"
        DB_PASSWORD = credentials('db-secret-password')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Code pulled successfully."
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker images..."
                // Use --no-cache to ensure a clean build for the final submission
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Verify') {
            steps {
                echo "Launching containers for verification..."
                sh 'docker-compose up -d'
                
                sh 'sleep 10'
                
                echo "Containers are live. Ready for Part 3 tests."
            }
        }
    }

    post {
        always {
            echo "Cleaning up environment..."
            sh 'docker-compose down -v'
        }
    }
}