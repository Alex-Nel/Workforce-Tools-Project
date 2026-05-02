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
            }
        }

        stage('Build') {
            steps {
                echo "Building Docker images..."
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Verify') {
            steps {
                echo "Setting up containers..."
                sh 'docker-compose up -d'
                
                // Use the app's retry logic instead of a long sleep
                echo "Waiting for Flask to initialize..."
                sh 'sleep 20'
                
                echo "Running integration tests..."
                sh 'docker-compose exec -T app python tests/test_api.py'
            }
        }

        stage('Deploy/Status') {
            steps {
                echo "Verification complete."
                sh 'docker-compose ps'
            }
        }
    }

    post {
        always {
            echo "Cleaning up environment..."
            sh 'docker-compose down -v || true'
        }
    }
}
