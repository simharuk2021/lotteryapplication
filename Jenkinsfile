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
                DOCKER_USERNAME = credentials('docker_username')
                DOCKER_PASSWORD = credentials('docker_password')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('ansible configuration') {
            steps {
                sh "bash ansible.sh"
            }
        }
    post {
        always {
            sh "docker logout"
            }
        }
    }
}