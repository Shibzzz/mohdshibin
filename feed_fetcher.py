import feedparser

FEEDS = [
    "https://thehackernews.com/rss.xml",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.darkreading.com/rss.xml"
]

def fetch_articles():
    articles = []
    for feed_url in FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary
            })
    return articles
