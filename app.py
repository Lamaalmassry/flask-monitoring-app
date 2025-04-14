from flask import Flask, render_template
from prometheus_client import start_http_server, Counter, generate_latest
import re

app = Flask(__name__)

# Initialize the Prometheus counter
REQUEST_COUNT = Counter('request_count_total', 'Total number of requests received')

# Route to display the home page with UI
@app.route('/')
def hello():
    # Increment the counter each time the endpoint is hit
    REQUEST_COUNT.inc()

    # Get the current value of the request count
    metrics_data = generate_latest(REQUEST_COUNT).decode('utf-8')

    # Extract the request_count_total value using regex
    match = re.search(r'request_count_total (\d+\.\d+)', metrics_data)
    request_count_value = match.group(1) if match else '0'

    return render_template('index.html', request_count=request_count_value)

# Route to expose Prometheus metrics (to scrape by Prometheus)
@app.route('/metrics')
def metrics():
    return generate_latest(REQUEST_COUNT)

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8000, addr='0.0.0.0')  # Allow external access
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)