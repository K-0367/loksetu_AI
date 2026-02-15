# Design Document
AI for Communities Access and Public Impact

---

## System Architecture Overview

Explanation of how your system works...
# 📌 How Our System Works

## 🔹 System Working Explanation

### 1️⃣ User Interaction Layer (Frontend)

Users access the platform through a simple and multilingual web interface built using HTML and integrated with AI-powered features.

* Citizens submit queries related to:

  * Government schemes
  * Public services
  * Local civic issues
* Users can type or speak their queries in their preferred language.
* The system ensures accessibility for rural and semi-urban users.

The frontend sends user input securely to the backend server.

---

### 2️⃣ Backend Processing Layer (Application Server)

The backend (app.py) acts as the core processing engine of the system.

When a user submits a query:

1. The system receives the input.
2. It preprocesses the text (cleaning, normalization).
3. The query is passed to the AI intelligence module.
4. The system searches:

   * Government scheme database
   * Policy knowledge base
   * Civic information datasets

The backend then generates a structured and simplified response.

---

### 3️⃣ AI Intelligence Layer

The AI module performs:

* 🔍 Intent Detection – Understands what the citizen is asking.
* 🌐 Language Translation – Converts regional languages to a processing language.
* 🧠 Context Understanding – Identifies eligibility, benefits, and relevant schemes.
* 📊 Recommendation Engine – Suggests the most suitable government schemes.

AI ensures:

* Simplified explanations
* Personalized responses
* Inclusive access to information

---

### 4️⃣ Data & Knowledge Layer

The system uses structured datasets (schemes.json) containing:

* Scheme name
* Eligibility criteria
* Required documents
* Application process
* Benefits

The AI matches user profiles with this data.

---

### 5️⃣ Response Generation

The final response is:

* Clear
* Easy to understand
* Multilingual
* Actionable (tells user what to do next)

The answer is then displayed back to the user interface.

---

## 🔄 End-to-End Flow Summary

1. User submits query
2. Frontend sends data to backend
3. Backend processes using AI
4. AI matches with scheme database
5. System generates response
6. User receives personalized guidance

---

# 🔥 Short Technical Architecture Summary 

```
User → Frontend → Backend (Flask) → AI Module → Scheme Database → Response → User
```
> Our system bridges the information gap between citizens and public services by using AI to transform complex policy data into simple, accessible, and actionable insights for every community member.
```


## Backend (app.py)
```
python
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
You are LokSetu
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
            {"role": "user", "content": user_message}]
    )

   reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(debug=True)
```
```
## frontend-index.html
HTML
<!DOCTYPE html>
<html>
<head>
    <title>LokSetu</title>
    <style>
        body { font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif; background: #f1bbdf; padding: 20px; }
        #chat { background: white; padding: 20px; border-radius: 10px; }
        input { width: 80%; padding: 10px; }
        button { padding: 10px; }
    </style>
</head>
<body>

<h2>Public Pal</h2>

<div id="chat">
    <p id="response">Ask about any government scheme.</p>
</div>

<br>
<input type="text" id="message" placeholder="Ask your query..." />
<button onclick="sendMessage()">Send</button>

<script>
function sendMessage() {
    let msg = document.getElementById("message").value;

    fetch("/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText = data.reply;
    });
}
</script>

</body>
</html>

##Data schema-schemaes.json
'''Json
{
  "PM Awas Yojana": {
    "description": "Provides affordable housing for low-income families.",
    "eligibility": "Family should not own a permanent house.",
    "documents": ["Aadhaar Card", "Income Certificate"]
  },
  "PM Ujjwala Yojana": {
    "description": "Free LPG connection for women from poor households.",
    "eligibility": "BPL family and adult woman applicant.",
    "documents": ["Aadhaar Card", "BPL Card"]
  },
  "Ayushman Bharat": {
    "description": "Health insurance up to 5 lakh per family.",
    "eligibility": "Low-income families listed in SECC.",
    "documents": ["Aadhaar Card"]
  }
}

    
