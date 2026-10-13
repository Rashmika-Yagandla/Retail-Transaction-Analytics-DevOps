# Retail Transaction Analytics — Jenkins + Docker Demo

A self-contained deployment test application with a retail dashboard, analytics API, Docker containers, automated tests, and Jenkins pipeline.

## Architecture
- **Frontend:** Flask dashboard on port 3000.
- **Backend:** Flask API on port 5000 with demo KPI, sales, product, and basket data.
- **Docker Compose:** Runs both services on a private network; only frontend port 3000 is exposed.
- **Jenkins:** Checkout, install test dependencies, run tests, build images, deploy from `main`, and smoke-test endpoints.

**Important:** The referenced GitHub project describes a Flask dashboard and a PySpark basket-analysis notebook run in Google Colab and exposed via ngrok. This test app replaces that external Colab/ngrok dependency with a local mock analytics API so CI/CD can be tested reliably. It is not a full port of the original Spark processing.

## Requirements
- Git
- Docker Desktop with Docker Compose v2 (Windows/macOS) or Docker Engine + Compose plugin (Linux)
- Python 3.10+ for running tests outside Docker
- Jenkins agent with Git, Python 3, Docker, Compose, and permission to run Docker commands

## Run locally
```bash
docker compose up --build -d
docker compose ps
```
Open **http://localhost:3000**.

Check endpoints:
```bash
curl http://localhost:3000/health
curl http://localhost:3000/api/metrics
curl http://localhost:3000/api/products
docker compose logs -f
```
Stop:
```bash
docker compose down
```

## Run tests manually
```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
cd backend && python -m pytest -q
cd ../frontend && python -m pytest -q
```

## Configure Jenkins
1. Install Jenkins and ensure the agent has Python 3, Git, Docker, and Docker Compose v2.
2. Create a **Pipeline** job.
3. Choose **Pipeline script from SCM**; SCM **Git**; enter your repository URL; branch `*/main`; script path `Jenkinsfile`.
4. Save and select **Build Now**.
5. Deploy and smoke-test stages run on `main`. Jenkins needs Docker permissions and port 3000 available on the deployment host.

If Jenkins runs in a container, Docker access must be configured for the agent; mounting the host Docker socket has security implications. Do not expose Jenkins or Docker daemon publicly.

## Pipeline stages
1. Checkout source.
2. Install Python dependencies.
3. Run frontend and backend unit tests.
4. Build Docker images.
5. Deploy on `main`.
6. Check frontend health and analytics API response.

## Acceptance checklist
- [ ] `docker compose build` succeeds.
- [ ] Both containers are running/healthy in `docker compose ps`.
- [ ] `http://localhost:3000` displays the dashboard.
- [ ] `/health` returns frontend healthy JSON.
- [ ] `/api/metrics` returns KPI JSON.
- [ ] Jenkins test, build, deploy, and smoke-test stages pass.

## Production follow-up
Replace sample data with transaction ingestion and Spark/FP-Growth processing, add authentication and validation, pin images, scan dependencies, and deploy to a managed environment. Never commit secrets.
