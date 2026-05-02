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
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Verify') {
            steps {
                echo "setting up containers for verification..."
                sh 'docker-compose up -d'
                sh 'sleep 10'     // to give time for database to be ready
                echo "Running integration tests..."
                sh 'pip install requests'
                sh 'python tests/test_api.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Verification complete. Application is running."
                sh 'docker-compose ps'
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully. All tests passed."
        }
        failure {
            echo "Pipeline failed. Check the stage logs above for details."
        }
        always {
            echo "Cleaning up environment..."
            sh 'docker-compose down -v'
        }
    }
}