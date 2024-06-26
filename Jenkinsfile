pipeline {
    agent any

    stages {
        stage('Prepare') {
            steps {
                sh 'rm -rf irssi'
                sh 'git clone https://github.com/Grallistrix/irssi'

            }
        }
        stage('Build') {
            steps {
                echo 'Building'
                sh 'docker images'
                sh 'docker rmi -f irssi-builder'
                sh 'docker images'
                dir('irssi/Dockerfiles'){
                    sh 'docker build -t irssi-builder -f irssi-builder.Dockerfile .'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                dir('irssi/Dockerfiles'){
                    sh 'docker build -f irssi-test.Dockerfile .'
                }
            }
        }
        stage('Publish') {
            steps {
                echo 'Publishing'
                dir('irssi/Dockerfiles'){
                    echo 'RPM'
                    sh 'docker build -t irssi-publisher -f irssi-publish.Dockerfile .'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                dir('irssi/Dockerfiles'){
                    sh "docker stop irssi-deployed"
                    sh "docker rm -f irssi-deployed"
                    sh 'docker build -t irssi-deployer -f irssi-deploy.Dockerfile .'
                    sh "docker run -it -d --name irssi-deployed irssi-deployer"
                    sh "docker exec irssi-deployed irssi --version"
                    sh "docker logs irssi-deployed"
                }
            }
        }
        
    }
}
