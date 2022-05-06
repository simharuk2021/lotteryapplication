pipeline {
    agent any
    stages {
        stage('unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            environment {
                DOCKERHUB_CREDENTIALS = credentials('docker_id')
                // DOCKER_PASSWORD = credentials('docker_password')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_CREDENTIALS_USR --password-stdin"
                sh "docker-compose push"
            }
        }
    }
    post {
        always {
            sh "docker logout"
        }
    }
}