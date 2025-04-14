# Flask Monitoring App with Prometheus & cAdvisor

This project runs a Flask app with Prometheus metrics collection and visualization using cAdvisor and Prometheus.

## 🐳 Services

- **flask-app**: Python Flask app exposing `/` and `/metrics`
- **prometheus**: Scrapes metrics from flask and cAdvisor
- **cAdvisor**: Monitors container resource usage

## 🛠 Project Structure

```bash
.
├── app.py                # Flask app with Prometheus metrics
├── requirements.txt      # Python dependencies
├── Dockerfile            # Flask app Docker image
├── docker-compose.yml    # All services
├── prometheus.yml        # Prometheus config file
└── templates/
    └── index.html        # Simple UI showing request count

## 📦 Tech Stack

- **Flask** – Web application framework
- **Prometheus** – Monitoring and alerting
- **cAdvisor** – Container-level metrics
- **Docker** – Containerization
- **Docker Compose** – Multi-service orchestration

---

## 🐳 Services Overview

| Service      | Description                                 | Port(s)     |
|--------------|---------------------------------------------|-------------|
| `flask-app`  | Flask app exposing web UI and metrics       | 5000, 8000  |
| `prometheus` | Scrapes metrics from Flask and cAdvisor     | 9090        |
| `cadvisor`   | Monitors Docker container resource usage    | 8080        |

---
## 🚀 Getting Started

### Prerequisites

- Docker
- Docker Compose

### Clone and Run

```bash
git clone https://github.com/Lamaalmassry/flask-monitoring-app.git
cd flask-monitoring-app
docker-compose up --build


📊 Metrics Explanation
Counter: request_count_total

Incremented each time the root / route is hit.

Prometheus scrape: Accessed via /metrics on port 8000.

Displayed on the home page via index.html.



🌐 Access the App
Flask App: http://localhost:5000

Metrics Endpoint: http://localhost:8000/metrics

Prometheus Dashboard: http://localhost:9090

cAdvisor Dashboard: http://localhost:8080

