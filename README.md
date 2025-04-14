# Flask Monitoring App with Prometheus & cAdvisor

This project runs a Flask application integrated with **Prometheus** for metrics collection and **cAdvisor** for container resource monitoring, all orchestrated using **Docker Compose**.

---

## 🐳 Services

- **flask-app**: A Python Flask application exposing `/` and `/metrics` endpoints.
- **prometheus**: Scrapes metrics from the Flask app and cAdvisor.
- **cadvisor**: Monitors container resource usage.

---

## 🛠️ Project Structure

```bash
.
├── app.py                # Flask app with Prometheus metrics
├── requirements.txt      # Python dependencies
├── Dockerfile            # Flask app Docker image
├── docker-compose.yml    # All services defined here
├── prometheus.yml        # Prometheus configuration
└── templates/
    └── index.html        # Simple UI showing request count



---

## 📦 Tech Stack

- **Flask**: Lightweight web framework for Python.
- **Prometheus**: Time-series monitoring and alerting system.
- **cAdvisor**: Container resource usage and performance analysis.
- **Docker**: Containerization platform.
- **Docker Compose**: Tool for defining and running multi-container apps.

---

## 🐳 Services Overview

| Service       | Description                                | Port(s)      |
|---------------|--------------------------------------------|--------------|
| `flask-app`   | Flask app with web UI and metrics endpoint | 5000, 8000   |
| `prometheus`  | Metrics scraping from Flask and cAdvisor   | 9090         |
| `cadvisor`    | Docker container resource monitoring       | 8080         |

---

## 🚀 Getting Started

### Prerequisites

- [Docker]
- [Docker Compose]

### Clone and Run
```bash
git clone https://github.com/Lamaalmassry/flask-monitoring-app.git
cd flask-monitoring-app
docker-compose up --build
```

### 📊Metrics Explanation
- Counter: request_count_total
- Incremented each time the root / route is accessed.
- Exposed via /metrics endpoint on port 8000.
- Displayed on the home page (index.html).


### 🌐 Access the App
- Flask App: http://localhost:5000
- Metrics Endpoint: http://localhost:8000/metrics
- Prometheus Dashboard: http://localhost:9090
- cAdvisor Dashboard: http://localhost:8080