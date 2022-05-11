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
        stage('Deployment'){
            steps{
                // sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml swarm-master:/home/jenkins/docker-compose.yaml"
                // sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf swarm-master:/home/jenkins/nginx.conf"
                sh "scp -i ~/ansible docker-compose.yaml swarm-manager:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/ansible nginx.conf swarm-manager:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    }
    post {
        always {
            sh "docker logout"
            }
        }
}