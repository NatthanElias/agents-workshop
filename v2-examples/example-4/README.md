# Example 4: Multi-Agent System

Este exemplo demonstra um sistema multi-agent usando Google ADK com **ParallelAgent** e **SequentialAgent**, simulando análise estratégica corporativa por C-Level executives.

## ▶️ Executar

### Modo CLI (linha de comando)

```bash
adk run .
```

Agora você pode fazer perguntas estratégicas no terminal!

### Modo Web UI (interface gráfica)

```bash
adk web .
```

Acesse http://localhost:8000 no navegador.

**Obs**: por padrão porta 8000, mas pode ser mudada com a flag `--port`. EX: `adk web --port 8001`

## 🧪 Testando

Exemplos de perguntas para fazer ao sistema:

- "Reduzir educadores em 30% para cortar custos. Qual análise?"
- "Expandir fisicamente ou investir em plataforma digital?"
- "Aumentar relação educador-aluno de 1:15 para 1:25. Avaliar."

O sistema executará **CSO e CMO em paralelo**, e depois o **CEO sintetizará** as análises.

## 📚 O que este exemplo demonstra

- **ParallelAgent**: Execução simultânea de agents (CSO + CMO rodam ao mesmo tempo)
- **SequentialAgent**: Orquestração determinística (paralelo → depois síntese)
- **Multi-agent coordination**: Comunicação entre agents via shared state
- **output_key**: Compartilhamento de resultados entre agents
- **google_search tool**: Ferramenta nativa do Google ADK para busca web
- **Knowledge Base inline**: Documentos passados direto no prompt


## 🔧 Modelo usado

- `gemini-2.5-flash`

Outros modelos Gemini disponíveis: https://ai.google.dev/gemini-api/docs/models/gemini

## 💡 Como funciona

1. `root_agent` orquestra tudo sequencialmente
2. `parallel_analysts` executa CSO + CMO simultaneamente:
   - **CSO**: Analisa impacto social usando Knowledge Base
   - **CMO**: Pesquisa mercado usando google_search
3. `ceo_agent` lê resultados de CSO/CMO e sintetiza decisão final
