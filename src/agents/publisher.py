from src.models import EditedArticle
from src.substack.client import SubstackClient
from src.model_factory import create_agent


def publisher_agent():
    def publish_draft(article: EditedArticle):
        client = SubstackClient()
        return client.create_draft(
            title=article.title,
            subtitle=article.subtitle,
            body_html=article.content_html,
        )

    agent = create_agent(
        system_prompt="Você é responsável por publicar artigos na Substack como rascunhos...",
        tools=[publish_draft],
    )
    return agent
