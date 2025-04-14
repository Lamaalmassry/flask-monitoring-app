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
