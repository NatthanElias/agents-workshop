import os
import pandas as pd
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.utilities import PythonREPL
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

# Carregar variáveis de ambiente
load_dotenv()

# Configurar a API key do Google Gemini
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY não encontrada no arquivo .env")

# 1. Carregar o CSV
df = pd.read_csv("sales_data.csv")

# 2. Criar a ferramenta Python REPL com o dataframe no contexto
python_repl = PythonREPL()
python_repl.locals = {"df": df, "pd": pd}

# 3. Criar a tool wrapper para o agent
python_repl_tool = Tool(
    name="python_repl",
    description="Execute código Python. O DataFrame 'df' e 'pd' (pandas) já estão disponíveis.",
    func=python_repl.run
)

# 4. Definir ferramentas disponíveis para o agent
tools = [python_repl_tool]

# 5. Criar o wrapper do modelo a ser usado
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=google_api_key
)

# 6. Criar prompt personalizado para Data Scientist
template = """Você é um Agente de Análise de Dados especializado em manipular e analisar dados de vendas usando Python e pandas.

CONTEXTO DO AMBIENTE:
- DataFrame disponível: df
- Biblioteca disponível: pd (pandas)
- Colunas: data, regiao, produto, vendas, quantidade

FERRAMENTAS DISPONÍVEIS:
{tools}

REGRAS OBRIGATÓRIAS:
1. SEMPRE use print() ao executar código Python
2. Escreva código em UMA LINHA ou use ponto-e-vírgula (;)
3. Use APENAS os nomes de ferramentas: {tool_names}
4. Após ver o resultado da execução, forneça a Final Answer

FORMATO DE RESPOSTA:
Thought: [Análise breve do que precisa fazer]
Action: [nome exato da ferramenta]
Action Input: [código python com print()]
Observation: [resultado será mostrado aqui]
... (repita Thought/Action/Observation se necessário)
Thought: I now know the final answer
Final Answer: [resposta em português]

EXEMPLOS:
Pergunta: Quantos registros no dataset?
Thought: Preciso contar registros usando len(df)
Action: python_repl
Action Input: print(len(df))
Observation: 20
Final Answer: O dataset contém 20 registros de vendas.

Pergunta: Total de vendas por região?
Thought: Preciso agrupar por regiao e somar vendas
Action: python_repl
Action Input: print(df.groupby('regiao')['vendas'].sum())
Observation: [resultado do agrupamento]
Final Answer: [interprete e responda em português]

IMPORTANTE: Sempre use print() e sempre forneça Final Answer após ver o resultado!

Histórico da conversa:
{agent_scratchpad}

Pergunta: {input}
Thought:"""

prompt = PromptTemplate(
    template=template,
    input_variables=["input", "agent_scratchpad", "tools", "tool_names"]
)


# 7. Criar o agent ReAct
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True, # EX: erro no parsing de chamadas de Tools -> continua executando
    max_iterations=10,
    early_stopping_method="generate"  # Gera resposta mesmo se não terminar
)

# 8. Interface de CLI interativa
print("🤖 Data Scientist Agent pronto!")
print("💬 Digite 'sair' para encerrar\n")
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("👋 Até logo!")
        break
    
    try:
        response = agent_executor.invoke({"input": user_input})
        print(f"\n🤖 Agent: {response['output']}\n")
    except Exception as e:
        print(f"\n❌ Erro: {e}\n")
        print("💡 Tente reformular sua pergunta.\n")
