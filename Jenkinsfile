pipeline {
    agent any   // Jenkins node normal (pas Docker)

    stages {
        stage('Run tests in Docker') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u'
                }
            }

            stages {
                stage('Show Python version') {
                    steps {
                        sh 'python3 --version'
                    }
                }

                stage('Create virtualenv and install deps') {
                    steps {
                        sh '''
                            python3 -m venv .venv
                            . .venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }

                stage('Run pytest') {
                    steps {
                        sh '''
                            . .venv/bin/activate
                            pytest -v -s --alluredir=allure-results
                        '''
                    }
                }

                stage('Generate Allure HTML') {
                    steps {
                        sh '''
                            pip install allure-pytest
                            allure generate allure-results --clean -o allure-report || true
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true

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
