pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                //Usuń poprzednie repo
                sh 'rm -rf irssi'
                sh 'git clone https://github.com/Grallistrix/irssi'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Irssi Image'
                //Usun poprzedni image
                //sh 'docker rmi -f irssi-builder'
                dir('irssi/Building'){
                    sh 'docker build -t irssi-builder .'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                dir('irssi/Testing'){
                    sh 'docker rmi -f irssi-tester'
                    sh 'docker build -t irssi-tester .'
                }
            }
        } 
        stage('Publish') {
            steps {
                echo 'Publishing'
                dir('irssi/Publishing'){
                    echo 'RPM'
                    sh 'docker build -t irssi-publisher -f irssi-publish.Dockerfile .'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                dir('irssi/Deploy'){
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