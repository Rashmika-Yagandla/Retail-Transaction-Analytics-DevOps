import os
import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:5000")

@app.get("/")
def dashboard():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="healthy", service="frontend")

@app.get("/api/<path:path>")
def api_proxy(path):
    try:
        response = requests.get(f"{BACKEND_URL}/{path}", timeout=5)
        return (response.content, response.status_code, {"Content-Type": response.headers.get("Content-Type", "application/json")})
    except requests.RequestException:
        return jsonify(error="Analytics backend is unavailable"), 503

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
