from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Locust load test app running"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200
