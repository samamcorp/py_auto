pipeline {
    agent any   // Jenkins node normal

    stages {

        stage('Run tests in Docker') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u'
                }
            }

            steps {
                script {
                    sh '''
                        echo "Python version:"
                        python3 --version

                        echo "Creating virtualenv..."
                        python3 -m venv .venv
                        . .venv/bin/activate

                        echo "Installing dependencies..."
                        pip install --upgrade pip
                        pip install -r requirements.txt

                        echo "Running pytest..."
                        pytest -v -s --alluredir=allure-results

                        echo "Generating Allure report..."
                        pip install allure-pytest
                        allure generate allure-results --clean -o allure-report || true
                    '''
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
