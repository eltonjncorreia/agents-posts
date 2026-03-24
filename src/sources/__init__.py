from .tavily import search_tavily
from .google import search_google
from .newsapi import search_newsapi
from .rss import fetch_rss_feed
from src.config import settings


def fetch_all_sources(topic):
    results = []
    try:
        results.extend(search_tavily(topic))
        try:
            results.extend(search_google(topic))
        except Exception:
            pass
        try:
            results.extend(search_newsapi(topic))
        except Exception:
            pass
        try:
            for feed_url in settings.rss_feeds:
                results.extend(fetch_rss_feed(feed_url))
        except Exception:
            pass
    except Exception:
        # Se até o Tavily falhar, retorna vazio
        pass
    return results
