from flask import Flask
import requests
from news import fetch_news, fetch_kpop_rss, fetch_blackpink_rss
from config import TELEGRAM_TOKEN, CHAT_ID

app = Flask(__name__)


# ------------------------------
# 🔵 Endpoint principal (home)
# ------------------------------
@app.route("/")
def home():
    return "Bot is ready.", 200


# ------------------------------
# 🔵 Endpoint keep-alive (ping)
# ------------------------------
@app.route("/ping")
def ping():
    return "pong", 200


# ------------------------------
# 🔴 Envoi des news du matin
# ------------------------------
@app.route("/send_morning_news")
def send_morning_news():

    # 🔥 Récupération des news
    try:
        kpop = fetch_kpop_rss()
        blackpink = fetch_blackpink_rss()
        tech = fetch_news("technologie innovation")
        world = fetch_news("monde actualités")
    except Exception as e:
        return f"Erreur lors de la récupération des news : {e}", 500

    # 📝 Message Telegram
    message = (
        "📰 *Résumé du jour – 06h40*\n\n"
        "🎤 *K-POP :*\n" + kpop + "\n"
        "💖 *BLACKPINK :*\n" + blackpink + "\n"
        "💻 *Tech :*\n" + tech + "\n"
        "🌍 *Monde :*\n" + world
    )

    # ------------------------------
    # 📩 Envoi Telegram sécurisé
    # ------------------------------
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(telegram_url, data=payload, timeout=10)
    except Exception as e:
        return f"Erreur lors de l'envoi Telegram : {e}", 500

    return "News sent!", 200


# ------------------------------
# 🚀 Lancement serveur Render
# ------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
