pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                sh 'rm -rf irssi'
                sh 'git clone https://github.com/Grallistrix/irssi.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker rmi -f irssi-builder'
                dir('irssi/Dockerfiles'){
                    sh 'docker build -t irssi-builder -f irssi-builder.Dockerfile .'
                }
            }
        }
        stage('Test') {
            steps {
                dir('irssi/Dockerfiles'){
                    sh 'docker build -f irssi-test.Dockerfile .'
                }
            }
        }
        stage('Publish') {
            steps {
                dir('irssi/Dockerfiles'){
                    echo 'RPM'
                    sh 'docker build -t irssi-publisher -f irssi-publish.Dockerfile .'
                }
            }
        }
        stage('Deploy') {
            steps {
                dir('irssi/Dockerfiles'){
                    sh "docker stop irssi-1"
                    sh "docker rm -f irssi-1"
                    sh 'docker build -t irssi-deployer -f irssi-deploy.Dockerfile .'
                    sh "docker run -it -d --name irssi-1 irssi-deployer"
                    sh "docker exec irssi-1 irssi --version"
                    sh "docker logs irssi-1"
                }
            }
        }
        
    }
}
