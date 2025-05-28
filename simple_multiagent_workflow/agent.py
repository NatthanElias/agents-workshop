from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

MODEL_NAME = LiteLlm(model="openai/gpt-4.1-nano")
# MODEL_NAME = LiteLlm(model="groq/llama3-8b-8192")

poem_agent = Agent(
    model= MODEL_NAME,
    name='poem_agent',
    description='Você é o melhor escritor de Poemas de todos os tempos.',
    instruction='''Você deve escrever um poema baseado no tema dito pelo usuário.
    ''',
)

joke_agent = Agent(
    model= MODEL_NAME,
    name='joke_agent',
    description='Você é um tiozão muito engraçado e gosta de fazer todos rirem.',
    instruction=''' Você deve contar um piada de tiozão baseado no tema informado pelo usuário.
    ''',
)

root_agent = Agent(
    model= MODEL_NAME,
    name='root_agent',
    description='Pode controlar o fluxo escolhendo para qual Agente delegar.',
    instruction='''Você deve sempre perguntar:" Qual tema gostaria? Você quer rir ou chorar? ". Depois delega para um dos seus sub-agents que você tem acesso, sendo eles:
    - poem_agent
    - joke_agent
    ''',
    sub_agents=[poem_agent, joke_agent]
)
