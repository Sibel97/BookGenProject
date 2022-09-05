pipeline {
    agent any
    stages {

        stage('Build and push images') {
            steps {
                sh "sudo docker-compose build --parallel"
                sh "sudo docker login -u sibel97 -p password1234"
                sh "sudo docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "ansible-playbook -i configuration/inventory.yaml configuration/playbook.yaml"
            }
        }
    }

}