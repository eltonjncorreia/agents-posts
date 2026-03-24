# Configuração de Provedores LLM

Este projeto suporta múltiplos provedores de modelos de linguagem. A seleção é feita dinamicamente através da variável de ambiente `LLM_PROVIDER`.

## Provedores Suportados

### 1. Google (Padrão)
**Provedor:** Google Generative AI (Gemini)

```env
LLM_PROVIDER=google
LLM_MODEL=gemini-2.0-flash
GOOGLE_API_KEY=sua_chave_aqui
```

**Modelos disponíveis:**
- `gemini-2.0-flash` (recomendado)
- `gemini-1.5-pro`
- `gemini-1.5-flash`

---

### 2. OpenAI
**Provedor:** OpenAI

```env
LLM_PROVIDER=openai
LLM_MODEL=gpt-4
OPENAI_API_KEY=sua_chave_aqui
```

**Modelos disponíveis:**
- `gpt-4` (recomendado)
- `gpt-4-turbo`
- `gpt-3.5-turbo`

---

### 3. Anthropic
**Provedor:** Anthropic (Claude)

```env
LLM_PROVIDER=anthropic
LLM_MODEL=claude-3-sonnet-20240229
ANTHROPIC_API_KEY=sua_chave_aqui
```

**Modelos disponíveis:**
- `claude-3-sonnet-20240229` (recomendado)
- `claude-3-opus-20240229`
- `claude-3-haiku-20240307`

---

### 4. xAI (Grok)
**Provedor:** xAI

```env
LLM_PROVIDER=xai
LLM_MODEL=grok-2
XAI_API_KEY=sua_chave_aqui
```

**Modelos disponíveis:**
- `grok-2` (recomendado)
- `grok-1`

---

## Como Mudar de Provedor

1. Edite o arquivo `.env.local`
2. Altere `LLM_PROVIDER` para o provedor desejado
3. Defina `LLM_MODEL` para um modelo suportado
4. Configure a API key correspondente
5. Reinicie a aplicação

### Exemplo: Trocar para OpenAI

```bash
# .env.local
LLM_PROVIDER=openai
LLM_MODEL=gpt-4-turbo
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx...
```

---

## Implementação Técnica

A seleção dinâmica é feita através do módulo `src/model_factory.py`:

```python
from src.model_factory import create_agent

# Cria automaticamente um agent com o provedor configurado
agent = create_agent(
    system_prompt="Seu prompt aqui",
    tools=[tool1, tool2]  # opcional
)
```

A factory detecta automaticamente qual provedor usar baseado em `LLM_PROVIDER` e instancia o modelo correto.

---

## Variáveis de Ambiente

```env
# Seleção do provedor (obrigatório)
LLM_PROVIDER=google|openai|anthropic|xai

# Modelo específico (obrigatório)
LLM_MODEL=nome_do_modelo

# API Keys (conforme provedor)
GOOGLE_API_KEY=xxxxx       # Para Google
OPENAI_API_KEY=xxxxx       # Para OpenAI
ANTHROPIC_API_KEY=xxxxx    # Para Anthropic
XAI_API_KEY=xxxxx          # Para xAI
```

---

## Tratamento de Erros

Se uma API key necessária não estiver configurada, o factory lançará um `ValueError` informando qual chave está faltando:

```
ValueError: GOOGLE_API_KEY não configurada
ValueError: OPENAI_API_KEY não configurada
ValueError: Provedor desconhecido: nome_invalido
```

---

## Recomendações

- **Para desenvolvimento:** Use Google Gemini (quota gratuita disponível)
- **Para produção:** Use OpenAI GPT-4 ou Anthropic Claude (mais estáveis)
- **Para custo:** Use Google Gemini ou xAI (mais baratos)
- **Para latência:** Use OpenAI (melhor performance)
