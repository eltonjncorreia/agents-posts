from pydantic_ai import Agent
from src.models import EditedArticle, PublishResult
from src.substack.client import SubstackClient
from src.config import settings


def publisher_agent():
    def publish_draft(article: EditedArticle):
        client = SubstackClient()
        return client.create_draft(
            title=article.title,
            subtitle=article.subtitle,
            body_html=article.content_html,
        )

    agent = Agent(
        system_prompt="Você é responsável por publicar artigos na Substack como rascunhos...",
        tools=[publish_draft],
        model=settings.llm_model,
    )
    return agent
