
from flask import Flask, jsonify, request

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

@app.route("/reward", methods=["GET"])
def reward():
    user_id = request.args.get("userId")

    if not user_id or not user_id.isdigit():
        return jsonify({
            "success": False,
            "message": "Invalid userId"
        }), 400

    # Callback received.
    # Do not credit points until the reward
    # has been authenticated and processed.

    return jsonify({
        "success": True,
        "userId": user_id,
        "message": "Reward callback received"
    })

