import requests
from config import GNEWS_API_KEY

def summarize(text, limit=200):
    return text if len(text) <= limit else text[:limit] + "..."

def fetch_news(query):
    url = f"https://gnews.io/api/v4/search?q={query}&lang=fr&max=5&apikey={GNEWS_API_KEY}"
    data = requests.get(url).json()
    articles = data.get("articles", [])

    result = []
    for a in articles:
        title = summarize(a["title"])
        link = a["url"]
        result.append(f"• {title}\n{link}\n")

    return "\n".join(result) if result else "Aucune news trouvée."
