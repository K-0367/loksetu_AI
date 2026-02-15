from flask import Flask, render_template, request, jsonify
import json
import openai

app = Flask(__name__)

# 🔑 Add your API key
openai.api_key = "YOUR_API_KEY_HERE"

# Load schemes data
with open("schemes.json", "r") as f:
    schemes = json.load(f)

SYSTEM_PROMPT = """
You are Public Pal.
Explain government schemes in very simple language.
Ask basic questions to check eligibility.
Avoid complex or legal terms.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
