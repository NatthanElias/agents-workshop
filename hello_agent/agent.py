from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    #model=LiteLlm(model="groq/llama3-8b-8192"),
    model=LiteLlm(model="openai/gpt-4.1-nano"),
    name='greetings_agent',
    description='Um assistente simpático e proativo para responder o usuário.',
    instruction='''Você sempre inicia com a frase: "Olá Mundo! Qual seu nome?". 
    Depois do usuário informar o seu nome, Você deve dar oi para ele e perguntar se ele quer mais alguma coisa.''',
)
