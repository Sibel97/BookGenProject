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
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    }

}