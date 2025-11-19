from flask import Flask
import requests
from news import fetch_news
from config import TELEGRAM_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route("/send_morning_news")
def send_morning_news():
    kpop = fetch_news("kpop musique idols comeback")
    tech = fetch_news("technologie innovation")
    world = fetch_news("monde international actualités")

    message = (
        "📰 *Résumé du jour – 06h40*\n\n"
        "🎤 *K-POP :*\n" + kpop + "\n"
        "💻 *Tech :*\n" + tech + "\n"
        "🌍 *Monde :*\n" + world
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
