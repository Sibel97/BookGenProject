pipeline {
    agent any
    stages {

        stage('Build and push images') {
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u sibel97 -p password1234"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/id_rsa docker-compose.yaml node-m:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/id_rsa nginx.conf node-m:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    }

}