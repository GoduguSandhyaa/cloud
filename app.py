from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Cloud Computing Lab",
        "status": "Application Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy"
    })

@app.route("/student")
def student():
    return jsonify({
        "name": "Sandhya",
        "department": "CSE",
        "year": "Final Year"
    })

@app.route("/about")
def about():
    return jsonify({
        "application": "Cloud Deployment",
        "technology": "Python Flask"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)