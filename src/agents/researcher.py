from pydantic_ai import Agent
from src.sources import fetch_all_sources
from src.model_factory import create_agent


def researcher_agent():
    agent = create_agent(
        system_prompt="Você é um pesquisador especializado em curadoria de conteúdo tech...",
        tools=[fetch_all_sources],
    )
    return agent
