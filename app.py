from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

mood_quotes = {
    "happy": [
        "Happiness looks good on you 🌸",
        "Keep smiling, it suits you 😊",
        "Your joy is contagious ✨"
    ],
    "sad": [
        "This too shall pass 🌧️",
        "Be gentle with yourself 💙",
        "Even the darkest night ends 🌙"
    ],
    "motivated": [
        "Go conquer your goals 🚀",
        "Discipline beats motivation 💪",
        "Success starts with showing up 🔥"
    ],
    "stressed": [
        "Pause. Breathe. You’re okay 🌿",
        "One step at a time 🤍",
        "Peace begins with a deep breath 🧘‍♀️"
    ]
}

def time_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning ☀️"
    elif hour < 17:
        return "Good Afternoon 🌤️"
    else:
        return "Good Evening 🌙"

@app.route("/", methods=["GET", "POST"])
def home():
    quote = None
    greeting = time_greeting()

    if request.method == "POST":
        mood = request.form.get("mood")
        quote = random.choice(mood_quotes.get(mood, []))

    return render_template(
        "index.html",
        greeting=greeting,
        quote=quote
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

