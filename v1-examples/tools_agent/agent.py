from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from datetime import datetime

def get_current_time() -> dict:
    """
    Informa o tempo atual no formato DD-MM-YYYY HH:MM:SS
    """
    return {
        "current_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

root_agent = Agent(
    #model=LiteLlm(model="groq/llama3-8b-8192"),
    model=LiteLlm(model="openai/gpt-4.1-nano"),
    name='tools_agent',
    description='Um assistente com poder de invocar tools',
    instruction='''Você é um assistente simpático e proativo para responder o usuário com acesso as seguintes tools:
    - get_current_time
    ''',
    tools=[get_current_time]
)
