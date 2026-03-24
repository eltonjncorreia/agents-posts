from pydantic_ai import Agent
from src.sources import fetch_all_sources
from src.config import settings


def researcher_agent():
    agent = Agent(
        system_prompt="Você é um pesquisador especializado em curadoria de conteúdo tech...",
        tools=[fetch_all_sources],
        model=settings.llm_model,
    )
    return agent
