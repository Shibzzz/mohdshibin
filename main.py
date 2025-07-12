from feed_fetcher import fetch_articles
from summarizer import summarize_article
from publisher import post_to_medium

def main():
    articles = fetch_articles()
    for article in articles:
        summary = summarize_article(article['title'], article['summary'], article['link'])
        post_result = post_to_medium(article['title'], summary)
        print(f"Posted to Medium: {post_result.get('data', {}).get('url', 'Failed')}")

if __name__ == "__main__":
    main()
