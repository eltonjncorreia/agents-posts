import requests
from src.config import settings


def search_newsapi(query):
    url = "https://newsapi.org/v2/everything"
    params = {"q": query, "apiKey": settings.newsapi_key, "pageSize": 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
