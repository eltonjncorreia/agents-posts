from pydantic_ai import Agent
from src.models import ResearchResult, EditedArticle
from src.config import settings


def editor_agent():
    agent = Agent(
        system_prompt="Você é um editor-chefe de newsletter tech. Seu trabalho é criar um resumo conciso e envolvente de 30-50 linhas...",
        model=settings.llm_model,
    )
    return agent
