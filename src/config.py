from pydantic_settings import BaseSettings
from typing import List, Optional


class Settings(BaseSettings):
    github_token: str
    topics: List[str]
    substack_sid: str
    substack_publication: str
    tavily_api_key: str
    serpapi_key: str
    newsapi_key: str
    rss_feeds: List[str]
    
    # LLM Configuration
    llm_provider: str = "google"  # google, openai, anthropic, xai
    llm_model: str = "gemini-2.0-flash"
    
    # API Keys for different providers
    google_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    xai_api_key: Optional[str] = None

    class Config:
        env_file = ".env.local"


settings = Settings()
