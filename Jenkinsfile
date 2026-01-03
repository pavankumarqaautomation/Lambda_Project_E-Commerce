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
                "C:\Soft\python.exe"  -m pip install --upgrade pip
                "C:\Soft\python.exe"  -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run PyTest Suite') {
            steps {
                bat '''
                "C:\Soft\python.exe" -m pytest
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


