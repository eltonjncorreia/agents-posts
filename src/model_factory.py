from pydantic_ai import Agent
from src.config import settings


def create_model():
    """
    Factory function para criar o modelo correto baseado na variável de ambiente LLM_PROVIDER.

    Suporta:
    - 'google': Google Generative AI (Gemini)
    - 'openai': OpenAI GPT
    - 'anthropic': Anthropic Claude
    - 'xai': xAI Grok
    """
    provider = settings.llm_provider.lower()
    model_name = settings.llm_model

    if provider == "google":
        from pydantic_ai.models.google import GoogleModel
        from pydantic_ai.providers.google import GoogleProvider

        if not settings.google_api_key:
            raise ValueError("GOOGLE_API_KEY não configurada")

        return GoogleModel(
            model_name, provider=GoogleProvider(api_key=settings.google_api_key)
        )

    elif provider == "openai":
        from pydantic_ai.providers.openai import OpenAIProvider

        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY não configurada")

        return Agent(
            model_name, provider=OpenAIProvider(api_key=settings.openai_api_key)
        )

    elif provider == "anthropic":
        from pydantic_ai.models.anthropic import AnthropicModel
        from pydantic_ai.providers.anthropic import AnthropicProvider

        if not settings.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY não configurada")

        return AnthropicModel(
            model_name, provider=AnthropicProvider(api_key=settings.anthropic_api_key)
        )

    elif provider == "xai":
        from pydantic_ai.models.xai import XaiModel
        from pydantic_ai.providers.xai import XaiProvider

        if not settings.xai_api_key:
            raise ValueError("XAI_API_KEY não configurada")

        return XaiModel(
            model_name,
            provider=XaiProvider(api_key=settings.xai_api_key),
        )

    else:
        raise ValueError(
            f"Provedor desconhecido: {provider}. "
            f"Use 'google', 'openai', 'anthropic' ou 'xai'"
        )


def create_agent(system_prompt: str, tools=None, **kwargs):
    """
    Helper function para criar um Agent com o modelo correto.

    Args:
        system_prompt: Prompt do sistema
        tools: Lista de ferramentas (opcional)
        **kwargs: Argumentos adicionais para o Agent

    Returns:
        Agent configurado com o modelo correto
    """
    model = create_model()

    agent_kwargs = {"system_prompt": system_prompt, "model": model, **kwargs}

    if tools:
        agent_kwargs["tools"] = tools

    return Agent(**agent_kwargs)
