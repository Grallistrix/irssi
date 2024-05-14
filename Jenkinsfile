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
                echo 'Building the Irssi Image'
                //Usun poprzedni image
                sh 'docker rmi -f irssi-builder'
                dir('irssi/Building'){
                    st 'docker build -t irssi-builder .'
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