# Workshop de LLM Agents

Material para aprender teoria e prática de agentes baseados em LLMs (Large Language Models) usando Python e APIs gratuitas.

Este workshop foi desenvolvido para aulas ministradas na **Universidade Atitus** (5º semestre) e oficinas no **IFSUL**, ambos em Passo Fundo/RS.

## 👥 Público-alvo

- Estudantes de Ciência da Computação
- Desenvolvedores com conhecimento básico de Python
- Qualquer pessoa interessada em IA e Agents

## 🎓 Conteúdo Teórico

- Ver pasta `_slides/`

## 💻 Conteúdo Prático

### [Example 1: Hello World Agent](./v2-examples/example-1/)
Introdução ao Google ADK com um agent básico de saudação.

**O que aprende:**
- Criação básica de um agent
- Integração com Google Gemini
- Execução via CLI e Web UI

---

### [Example 2: Agent com RAG](./v2-examples/example-2/)
Agent que usa RAG (Retrieval Augmented Generation) para buscar informações em documentos.

**O que aprende:**
- RAG (busca em documentos)
- Vector stores com FAISS
- Embeddings locais
- Tool calling com LangChain

---

### [Example 3: Agent ReAct Data Scientist](./v2-examples/example-3/)
Agent que analisa dados usando o padrão ReAct (Reasoning + Acting).

**O que aprende:**
- Padrão ReAct
- Python REPL como tool
- Análise de dados com pandas
- Prompts customizados

---

### [Example 4: Multi-Agent System](./v2-examples/example-4/)
Sistema multi-agent com execução paralela e orquestração sequencial.

**O que aprende:**
- ParallelAgent (execução simultânea)
- SequentialAgent (orquestração)
- Comunicação entre agents
- Arquitetura hierárquica

## 🔧 Stack Tecnológica

| Tecnologia | Uso | Custo |
|------------|-----|-------|
| **Google Gemini API** | LLM principal | Gratuito (1.5k req/dia) |
| **Google ADK** | Framework de agents | Open-source |
| **LangChain** | Ferramentas e patterns | Open-source |
| **FAISS** | Vector store local | Open-source |
| **HuggingFace** | Embeddings locais | Open-source |

**Custo total:** R$ 0,00 (tudo gratuito!)

## 🤝 Contribuições

Este é um material educacional aberto. Sugestões e melhorias são bem-vindas!

## 📧 Contato

[Nathan Elias - AI Engineer](https://www.linkedin.com/in/natthan-elias/)

## 📚 Referências

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [LangChain Documentation](https://python.langchain.com/)

## 📄 Licença

Material educacional de uso livre para fins acadêmicos.

---

**Última atualização:** Outubro 2025  
**Versão:** 2.0 (v2-examples)
