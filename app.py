import os
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Print files in the directory to check if models exist
print("Files in the current directory:", os.listdir(os.getcwd()))

# Load trained models
fake_profile_model = joblib.load("fake_profile_model.pkl")
harmful_comment_model = joblib.load("harmful_comment_rf_model.pkl")
fake_review_model = joblib.load("fake_review_model.pkl")

@app.route("/predict_profile", methods=["POST"])
def predict_profile():
    data = request.json["features"]
    prediction = fake_profile_model.predict([data])
    return jsonify({"fake_profile": int(prediction[0])})

@app.route("/predict_comment", methods=["POST"])
def predict_comment():
    data = request.json["text"]
    prediction = harmful_comment_model.predict([data])
    return jsonify({"harmful_comment": int(prediction[0])})

@app.route("/predict_review", methods=["POST"])
def predict_review():
    data = request.json["text"]
    prediction = fake_review_model.predict([data])
    return jsonify({"fake_review": int(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)

