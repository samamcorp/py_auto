pipeline {
    agent any

    stages {
        stage('Show Python version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Create virtualenv and install deps') {
            steps {
                sh '''
                    /Library/Frameworks/Python.framework/Versions/3.14/bin/python3.14 -m venv .venv
                    source .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run pytest') {
            steps {
                sh '''
                    source .venv/bin/activate
                    pytest -v -s --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }

    }
}