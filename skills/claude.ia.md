# Claude.IA Skill para Evolução do Projeto

## Objetivo

Este skill define padrões e práticas para evoluir o projeto **Produzir Substack** com base em workflows e melhores práticas do Claude.IA. Ele inclui guidelines para:

- Adicionar novas fontes de conteúdo
- Melhorar prompts e agentes
- Otimizar o pipeline para custo e desempenho
- Garantir qualidade e testes

---

## Estrutura

### 1. Adicionar Novas Fontes de Conteúdo

1. Crie um novo arquivo em `src/sources/` com o nome da fonte (ex: `medium.py`).
2. Implemente uma função que retorne uma lista de artigos no formato `SourceArticle`.
3. Atualize `src/sources/__init__.py` para incluir a nova fonte em `fetch_all_sources()`.
4. Teste a integração com mocks.

### 2. Melhorar Prompts e Agentes

- **Pesquisador**:
  - Ajuste o prompt para incluir contexto adicional (ex: "Foque em artigos recentes e relevantes para desenvolvedores").
  - Adicione ferramentas específicas para novas fontes.

- **Editor**:
  - Refine o prompt para melhorar a qualidade do resumo (ex: "Use um tom mais informal e envolvente").
  - Teste diferentes limites de caracteres para o resumo.

- **Publicador**:
  - Adicione validações antes de publicar (ex: verificar se o HTML está bem formatado).

### 3. Otimizar Pipeline

- **Custo**:
  - Use caching para evitar chamadas redundantes às APIs.
  - Reduza o número de artigos processados por execução.

- **Desempenho**:
  - Paralelize chamadas às fontes de conteúdo.
  - Use bibliotecas assíncronas como `httpx` para melhorar a eficiência.

### 4. Garantir Qualidade

- **Testes**:
  - Adicione testes unitários para cada fonte e agente.
  - Use mocks para simular respostas de APIs.

- **Logs**:
  - Adicione logs detalhados para cada etapa do pipeline.
  - Use uma biblioteca como `loguru` para facilitar o debug.

---

## Contribuindo

1. Siga os padrões definidos neste skill.
2. Documente todas as mudanças no `README.md`.
3. Abra um Pull Request para revisão antes de mergear.

---

## Licença

Este skill está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
