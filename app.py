from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route to check if API is running
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Verify API is running!"})

@app.route("/predict_profile", methods=["POST"])
def predict_profile():
    try:
        data = request.json
        print("Received data:", data)  # Debugging print
        if not data or "features" not in data:
            return jsonify({"error": "No features provided"}), 400
        return jsonify({"fake_profile": 1})  # Dummy response
    except Exception as e:
        print("Error:", str(e))  # Debugging print
        return jsonify({"error": str(e)}), 500

@app.route("/predict_comment", methods=["POST"])
def predict_comment():
    try:
        data = request.json
        print("Received data:", data)  # Debugging print
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400
        return jsonify({"harmful_comment": 1})  # Dummy response
    except Exception as e:
        print("Error:", str(e))  # Debugging print
        return jsonify({"error": str(e)}), 500

@app.route("/predict_review", methods=["POST"])
def predict_review():
    try:
        data = request.json
        print("Received data:", data)  # Debugging print
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400
        return jsonify({"fake_review": 0})  # Dummy response
    except Exception as e:
        print("Error:", str(e))  # Debugging print
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
