import requests
from src.config import settings


def search_tavily(query):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {settings.tavily_api_key}"}
    payload = {"query": query, "limit": 10}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()
