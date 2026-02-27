from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# create app
app = Flask(__name__)
CORS(app)


# -----------------------------
# Load schemes database
# -----------------------------
with open("schemes.json") as f:
    schemes = json.load(f)


# -----------------------------
# Test route
# -----------------------------
@app.route("/")
def home():
    return "Python Backend Running 🚀"


# -----------------------------
# Helper function
# -----------------------------
def find_schemes(user_text):

    user_text = user_text.lower()
    matched = []

    for scheme in schemes:
        if scheme["category"] in user_text:
            matched.append(scheme["name"])

    return matched


# -----------------------------
# TEXT INPUT API
# -----------------------------
@app.route("/text", methods=["POST"])
def text():

    data = request.json["text"]
    result = find_schemes(data)

    if result:
        msg = "Eligible for: " + ", ".join(result)
    else:
        msg = "No matching scheme found"

    return jsonify({"message": msg})


# -----------------------------
# VOICE INPUT API
# -----------------------------
@app.route("/voice", methods=["POST"])
def voice():

    data = request.json["text"]
    result = find_schemes(data)

    if result:
        msg = "Eligible for: " + ", ".join(result)
    else:
        msg = "No matching scheme found"

    return jsonify({"message": msg})


# -----------------------------
# FILE UPLOAD API
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]
    filename = file.filename.lower()

    if "income" in filename:
        msg = "Income proof verified. You may apply for subsidy schemes."
    else:
        msg = "Upload income certificate for better eligibility."

    return jsonify({"message": msg})


# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)