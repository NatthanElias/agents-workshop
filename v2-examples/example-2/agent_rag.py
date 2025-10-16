import os
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain import hub

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a API key do OpenRouter
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY não encontrada no arquivo .env")

# 1. Carregar documentos
loader = TextLoader("knowledge_base.txt")
docs = loader.load()

# 2. Dividir documentos em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
splits = text_splitter.split_documents(docs)

# 3. Criar embeddings e vector store (tudo Local neste exemplo)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.from_documents(splits, embeddings)

# 4. Criar retriever (metodo usado para buscar na Vector Store)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 5. Criar ferramenta de recuperação para o agent
retriever_tool = create_retriever_tool(
    retriever,
    name="knowledge_base_search",
    description="""Busca informações na base de conhecimento sobre a empresa TechCorp. 
    Use esta ferramenta quando precisar responder perguntas sobre produtos, serviços ou história da 
    empresa."""
)

# 6. Criar o wrapper do modelo a ser usado
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0,
    google_api_key=google_api_key
)

# 7. Criar o agent com a ferramenta
tools = [retriever_tool]
prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 8. Interface de CLI interativa
print("\n✅ Agent com RAG pronto!")
print("💬 Digite 'sair' para encerrar\n")

while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("👋 Até logo!")
        break
    
    response = agent_executor.invoke({"input": user_input})
    print(f"\nAgent: {response['output']}\n")
