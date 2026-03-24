from src.model_factory import create_agent


def editor_agent():
    agent = create_agent(
        system_prompt="Você é um editor-chefe de newsletter tech. Seu trabalho é criar um resumo conciso e envolvente de 30-50 linhas...",
    )
    return agent
