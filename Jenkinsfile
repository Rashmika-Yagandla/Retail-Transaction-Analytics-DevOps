pipeline {
    agent any
    options { timestamps(); disableConcurrentBuilds() }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Install test dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r backend/requirements.txt
                    pip install -r frontend/requirements.txt
                '''
            }
        }
        stage('Unit tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    (cd backend && PYTHONPATH=. pytest -q)
                    (cd frontend && PYTHONPATH=. pytest -q)
                '''
            }
        }
        stage('Build Docker images') { steps { sh 'docker compose build' } }
        stage('Deploy') {
            when { branch 'main' }
            steps { sh 'docker compose up -d --remove-orphans' }
        }
        stage('Smoke tests') {
            when { branch 'main' }
            steps {
                sh '''
                    set -eu
                    for i in $(seq 1 20); do
                      if curl -fsS http://localhost:3000/health >/dev/null; then break; fi
                      sleep 3
                    done
                    curl -fsS http://localhost:3000/health
                    curl -fsS http://localhost:3000/api/metrics
                '''
            }
        }
    }
    post {
        always { sh 'docker compose ps || true' }
        failure { echo 'Pipeline failed. Review the stage logs above.' }
        success { echo 'Retail Transaction Analytics demo pipeline completed successfully.' }
    }
}
