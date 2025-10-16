# Example 2: Agent com RAG Tool

Este exemplo demonstra como criar um Agent usando LangChain que utiliza uma ferramenta de RAG (Retrieval Augmented Generation) para buscar informações em documentos antes de responder.

## ▶️ Executar
Na linha de comando:

```bash
python agent_rag.py
```

O agent iniciará em modo interativo no terminal. Digite suas perguntas e ele buscará informações na base de conhecimento quando necessário.

## 🧪 Testando

Exemplos de perguntas para fazer ao agent:

- "Quem fundou a TechCorp?"
- "Quais são os produtos da empresa?"
- "Quanto custa o CloudManager Pro?"

O agent decidirá automaticamente quando usar a ferramenta de busca e quando responder diretamente.

## 📚 O que este exemplo demonstra

- **RAG (Retrieval Augmented Generation)**: Busca informações em documentos antes de responder
- **Criação de ferramenta personalizada** usando `create_retriever_tool`
- **Vector Store com FAISS**: Armazenamento e busca vetorial eficiente
- **Agent com tool calling**: O LLM decide quando usar a ferramenta de busca
- **Processamento de documentos**: Carregamento, chunking e embeddings

## 🔧 Componentes

- **LLM**: `google/gemini-2.0-flash-exp:free` (gratuito no OpenRouter)
- **Embeddings**: `sentence-transformers/all-MiniLM-L6-v2` (modelo local, sem necessidade de API)
- **Vector Store**: FAISS (local, sem necessidade de configuração adicional)
- **Document Loader**: TextLoader para arquivos .txt

## 💡 Como funciona

1. **Carregamento**: O documento `knowledge_base.txt` é carregado
2. **Chunking**: O texto é dividido em pedaços menores para melhor busca
3. **Embeddings**: Cada chunk é convertido em vetores usando embeddings
4. **Vector Store**: Os vetores são armazenados no FAISS para busca rápida
5. **Retriever Tool**: Uma ferramenta de busca é criada a partir do retriever
6. **Agent**: O LLM recebe a ferramenta e decide quando usá-la
7. **Execução**: O agent responde perguntas, buscando informações quando necessário