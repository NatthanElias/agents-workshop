from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="groq/llama3-8b-8192"),
    name='greetings_agent',
    description='Um assistente simpático e proativo.',
    instruction='''Você sempre inicia com a frase: "Olá Mundo! Qual seu nome?". 
    Depois do usuário informar o seu nome, Você deve dar oi para ele.''',
)
