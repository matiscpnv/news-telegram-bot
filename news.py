import requests
import feedparser
from config import GNEWS_API_KEY


def summarize(text, limit=200):
    return text if len(text) <= limit else text[:limit] + "..."


# 🔥 1) KPOP RSS (AllKpop)
def fetch_kpop_rss():
    feed = feedparser.parse("https://www.allkpop.com/rss")

    if not feed.entries:
        return "Aucune news K-POP trouvée."

    results = []
    for entry in feed.entries[:5]:
        title = summarize(entry.title)
        link = entry.link
        results.append(f"• {title}\n{link}\n")

    return "\n".join(results)


# 💖 2) BLACKPINK via GNews
def fetch_blackpink_news():
    url = (
        f"https://gnews.io/api/v4/search?"
        f"q=blackpink&lang=fr&max=5&apikey={GNEWS_API_KEY}"
    )

    data = requests.get(url).json()
    articles = data.get("articles", [])

    if not articles:
        return "Aucune news BLACKPINK trouvée."

    results = []
    for a in articles:
        title = summarize(a["title"])
        link = a["url"]
        results.append(f"• {title}\n{link}\n")

    return "\n".join(results)
