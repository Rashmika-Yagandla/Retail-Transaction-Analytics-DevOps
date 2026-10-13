from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(service="retail-analytics-api", status="ready")

@app.get("/health")
def health():
    return jsonify(status="healthy", service="analytics-backend")

@app.get("/metrics")
def metrics():
    return jsonify(revenue=184250, orders=1264, customers=842, units=3920)

@app.get("/sales")
def sales():
    return jsonify([
        {"date":"2026-10-06","revenue":18200},{"date":"2026-10-07","revenue":22400},
        {"date":"2026-10-08","revenue":19800},{"date":"2026-10-09","revenue":26750},
        {"date":"2026-10-10","revenue":31500},{"date":"2026-10-11","revenue":28900},
        {"date":"2026-10-12","revenue":36700}
    ])

@app.get("/products")
def products():
    return jsonify([
        {"name":"Coffee","units":840,"revenue":42000},{"name":"Ground Tea","units":720,"revenue":28800},
        {"name":"Biscuits","units":690,"revenue":20700},{"name":"Rice","units":510,"revenue":30600},
        {"name":"Cooking Oil","units":430,"revenue":25800}
    ])

@app.get("/basket")
def basket():
    return jsonify([
        {"item_a":"Coffee","item_b":"Biscuits","confidence":0.72},
        {"item_a":"Rice","item_b":"Cooking Oil","confidence":0.64},
        {"item_a":"Ground Tea","item_b":"Biscuits","confidence":0.58}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
