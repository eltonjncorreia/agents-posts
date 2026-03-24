from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    github_token: str
    topics: List[str]
    substack_sid: str
    substack_publication: str
    tavily_api_key: str
    serpapi_key: str
    newsapi_key: str
    rss_feeds: List[str]
    llm_model: str  # Modelo LLM (ex: 'gpt-4', 'ollama')

    class Config:
        env_file = ".env"


settings = Settings()
