pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Check out'
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '5681c726-2fd2-4243-8ec9-27fc02659592', url: 'https://github.com/bhavesh51/DevOps.git']]])
            }
        }
        stage('Build') {
            steps {
                echo 'Build'
                git branch: 'main', credentialsId: '5681c726-2fd2-4243-8ec9-27fc02659592', url: 'https://github.com/bhavesh51/DevOps.git'
                sh 'python3 Hello.py'
            }
        }
        
        
    }
}
