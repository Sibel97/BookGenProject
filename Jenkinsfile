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
                sh "scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml node-m:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/ansible_id_rsa nginx.conf node-m:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i Configuration/inventory.yaml Configuration/playbook.yaml"
            }
        }
    }

}
