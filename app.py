from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
app.secret_key = "crochet-secret-key"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Crochet Buddy 🧶, a friendly and supportive crochet assistant. "
                    "You help beginners and intermediate crocheters with patterns, advice, "
                    "encouragement, and troubleshooting. You are kind, patient, positive, "
                    "and never judgmental."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Oops 💛 Something went wrong. Please try again."})

if __name__ == "__main__":
    print("🔥 Crochet Buddy with REAL AI is running!")
    app.run(host="0.0.0.0", port=10000)


