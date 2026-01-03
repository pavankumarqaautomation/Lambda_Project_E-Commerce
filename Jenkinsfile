pipeline {
    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/pavankumarqaautomation/Lambda_Project_E-Commerce.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run PyTest Suite') {
            steps {
                bat '''
                pytest
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests executed successfully'
        }
        failure {
            echo 'Tests failed'
        }
    }
}
