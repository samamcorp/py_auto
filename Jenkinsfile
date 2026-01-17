pipeline {
    agent any

    stages {


        stage('Check Java in Jenkins') {
    steps {
        sh 'echo PATH=$PATH'
        sh 'which java || true'
        sh 'java -version || true'
    }
}
        stage('Run tests in Docker') {
            steps {
                sh '''
                    docker run --rm \
                        -v "$PWD":/app \
                        -w /app \
                        python:3.11 bash -c "
                            pip install --upgrade pip &&
                            pip install -r requirements.txt &&
                            pytest -v -s --alluredir=allure-results
                        "
                '''
            }
        }

        stage('Generate Allure report') {
            steps {
                sh '''
                    allure generate allure-results --clean -o allure-report || true
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true

            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']], commandline: 'allure'

            emailext(
                subject: "Rapport Allure - Build #${env.BUILD_NUMBER}",
                body: """
                    Hello everyone,

                    Test #${env.BUILD_NUMBER} has run.

                    Allure report :
                    ${env.BUILD_URL}artifact/allure-report/index.html

                    Artifacts :
                    ${env.BUILD_URL}artifact/

                    Best,
                    Q.A-TEAM
                """,
                to: "sam@borekas.net"
            )
        }
    }
}
