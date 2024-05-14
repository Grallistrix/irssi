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
                sh 'docker rmi -f irssi-builder'
                dir('irssi/Building'){
                    sh 'docker build -t irssi-builder .'
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                dir('irssi/Testing'){
                    sh 'docker build -t irssi-tester .'
                }
            }
        }   
    }
}