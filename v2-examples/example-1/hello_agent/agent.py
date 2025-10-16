from google.adk.agents import Agent

root_agent = Agent(
    model="gemini-2.0-flash-exp",
    name='greetings_agent',
    description='Um assistente simpático e proativo para responder o usuário.',
    instruction='''Você sempre inicia com a frase: "Olá Mundo! Qual seu nome?". 
    Depois do usuário informar o seu nome, Você deve dar oi para ele e perguntar se ele quer mais alguma coisa.''',
)
