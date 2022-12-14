pipeline {
    agent any
    stages {

        stage('Run unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build and push images') {
            steps {
                sh "sudo docker-compose build --parallel"
                sh "sudo docker login -u sibel97 -p "
                sh "sudo docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                sh "scp -i ~/.ssh/id_rsa docker-compose.yaml node-m:/home/jenkins/docker-compose.yaml"
                sh "scp -i ~/.ssh/id_rsa nginx.conf node-m:/home/jenkins/nginx.conf"
                sh "ansible-playbook -i Configuration/inventory.yaml Configuration/playbook.yaml"
            }
        }
    }
    post {
        always {
            junit '**/*.xml'
            cobertura coberturaReportFile: 'Front-end/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'Genre-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'Author-api/coverage.xml', failNoReports: false
            cobertura coberturaReportFile: 'Book-api/coverage.xml', failNoReports: false
        }
    }

}
