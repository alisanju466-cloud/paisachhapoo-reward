from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "bot": "PAISA CHHAPO"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})
