import requests
import feedparser
from config import GNEWS_API_KEY


def summarize(text: str, limit: int = 200) -> str:
    """Raccourcit un texte proprement."""
    return text if len(text) <= limit else text[:limit] + "..."


# ------------------------------------------------------
# 🔥 1) NEWS K-POP (RSS Soompi)
# ------------------------------------------------------
def fetch_kpop_rss() -> str:
    RSS_URL = "https://www.soompi.com/feed"
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return "Aucune news K-POP trouvée."

    results = []
    for entry in feed.entries[:5]:
        title = summarize(entry.title)
        link = entry.link
        results.append(f"• {title}\n{link}\n")

    return "\n".join(results)


# ------------------------------------------------------
# 💖 2) NEWS BLACKPINK (filtré depuis Soompi RSS)
# ------------------------------------------------------
def fetch_blackpink_rss() -> str:
    RSS_URL = "https://www.soompi.com/feed"
    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        return "Aucune news BLACKPINK trouvée."

    bp_articles = [
        entry for entry in feed.entries
        if "blackpink" in entry.title.lower()
        or "jisoo" in entry.title.lower()
        or "jennie" in entry.title.lower()
        or "lisa" in entry.title.lower()
        or "rose" in entry.title.lower()
    ]

    if not bp_articles:
        return "Aucune news BLACKPINK trouvée."

    results = []
    for entry in bp_articles[:5]:
        title = summarize(entry.title)
        link = entry.link
        results.append(f"• {title}\n{link}\n")

    return "\n".join(results)


# ------------------------------------------------------
# 🌍 3) NEWS via Google News (tech, monde…)
# ------------------------------------------------------
def fetch_google_news(query: str) -> str:
    url = (
        f"https://gnews.io/api/v4/search?"
        f"q={query}&lang=fr&max=5&apikey={GNEWS_API_KEY}"
    )

    try:
        data = requests.get(url, timeout=10).json()
    except Exception:
        return "Erreur lors de la récupération des news."

    articles = data.get("articles", [])
    if not articles:
        return "Aucune news trouvée."

    results = []
    for a in articles:
        title = summarize(a.get("title", "Sans titre"))
        link = a.get("url", "")
        results.append(f"• {title}\n{link}\n")

    return "\n".join(results)


# Alias utilisé pour tech / monde
def fetch_news(query: str) -> str:
    return fetch_google_news(query)
