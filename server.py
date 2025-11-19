from flask import Flask
import requests
from news import fetch_news, fetch_kpop_rss, fetch_blackpink_news
from config import TELEGRAM_TOKEN, CHAT_ID

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is ready."

@app.route("/send_morning_news")
def send_morning_news():

    kpop = fetch_kpop_rss()
    blackpink = fetch_blackpink_news()
    tech = fetch_news("technologie innovation")
    world = fetch_news("actualités monde")

    message = (
        "📰 *Résumé du jour – 06h40*\n\n"
        "🎤 *K-POP :*\n" + kpop + "\n"
        "💖 *BLACKPINK :*\n" + blackpink + "\n"
        "💻 *Tech :*\n" + tech + "\n"
        "🌍 *Monde :*\n" + world
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

    return "News sent!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
