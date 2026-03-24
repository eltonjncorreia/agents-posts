import requests
from src.config import settings


def search_google(query):
    url = "https://serpapi.com/search"
    params = {"q": query, "api_key": settings.serpapi_key, "num": 10}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
