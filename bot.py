from telegram.ext import Updater, CommandHandler
from news import fetch_news
from config import TELEGRAM_TOKEN

def news(update, context):
    kpop = fetch_news("kpop musique idols comeback")
    tech = fetch_news("technologie innovation")
    world = fetch_news("monde international actualités")

    message = (
        "📰 *Votre Brève Quotidienne*\n\n"
        "🎤 *K-POP :*\n" + kpop + "\n"
        "💻 *Tech :*\n" + tech + "\n"
        "🌍 *Monde :*\n" + world
    )

    update.message.reply_text(message, parse_mode="Markdown")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("news", news))

    print("Bot en ligne.")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
