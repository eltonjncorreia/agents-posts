

=======
# Produzir Substack

Agents para criar conteudo para SubStack


Pipeline multi-agente para buscar, resumir e publicar conteúdo na Substack como rascunho. Este projeto utiliza PydanticAI, GitHub Models e integrações com fontes de conteúdo como Tavily, SerpAPI, NewsAPI e RSS feeds.

## Requisitos

- Python 3.12+
- `uv` para gerenciar dependências e rodar o projeto
- Conta na Substack com cookie `substack.sid`
- Chaves de API para Tavily, SerpAPI e NewsAPI (opcional)

## Configuração Local

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd produzir_substack
   ```

2. Instale as dependências:
   ```bash
   uv install
   ```

3. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edite o arquivo `.env` com suas credenciais e configurações.

4. Execute o pipeline localmente:
   ```bash
   uv run -m src.main
   ```

## Estrutura do Projeto

```
produzir_substack/
├── pyproject.toml          # Configuração do Poetry e dependências
├── Dockerfile              # Configuração para deploy no Fly.io
├── fly.toml                # Configuração do Fly.io Machines
├── .env.example            # Exemplo de variáveis de ambiente
├── src/                    # Código-fonte principal
│   ├── config.py           # Configuração via Pydantic Settings
│   ├── models.py           # Modelos de dados
│   ├── sources/            # Fontes de conteúdo (Tavily, Google, etc.)
│   ├── agents/             # Agentes PydanticAI (Pesquisador, Editor, Publicador)
│   └── substack/           # Cliente para integração com Substack
└── .github/workflows/      # Configuração do GitHub Actions
```

## Deploy no Fly.io

1. Instale o Fly.io CLI:
   ```bash
   curl -L https://fly.io/install.sh | sh
   fly auth login
   ```

2. Configure o app no Fly.io:
   ```bash
   fly launch
   ```

3. Faça o deploy:
   ```bash
   fly deploy
   ```

4. Agende o job diário via GitHub Actions (já configurado em `.github/workflows/daily-run.yml`).

## Testes

- **Unitários**: Teste cada fonte de conteúdo isoladamente com mocks.
- **Integração**: Execute o pipeline localmente e verifique os rascunhos na Substack.
- **Pipeline Completo**: Valide o deploy no Fly.io e o agendamento via GitHub Actions.

---

## Contribuindo

1. Crie uma branch para sua feature/bugfix:
   ```bash
   git checkout -b minha-feature
   ```

2. Faça commits claros e objetivos.
3. Abra um Pull Request para revisão.

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

