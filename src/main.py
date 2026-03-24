from src.config import settings
from src.agents.researcher import researcher_agent
from src.agents.editor import editor_agent
from src.agents.publisher import publisher_agent


def main():
    topics = settings.topics
    for topic in topics:
        print(f"Pesquisando sobre: {topic}")
        researcher = researcher_agent()
        research_result = researcher.run_sync(topic)
        breakpoint()  # Para depuração, pode ser removido depois

        print(f"Editando artigos para: {topic}")
        editor = editor_agent()
        edited_article = editor.run_sync(research_result)

        print(f"Publicando rascunho para: {topic}")
        publisher = publisher_agent()
        publish_result = publisher.run_sync(edited_article)

        print(f"Rascunho publicado: {publish_result['url']}")


if __name__ == "__main__":
    main()
