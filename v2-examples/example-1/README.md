# Example 1: Hello World Agent

Este é um exemplo simples que demonstra o funcionamento básico do Google ADK (Agent Development Kit).

## ▶️ Executar

### Modo CLI (linha de comando)
```bash
adk run .
```

Agora você pode conversar com o agente no terminal!

### Modo Web UI (interface gráfica)
```bash
adk web .
```

Acesse http://localhost:8000 no navegador.

**Obs**: por padrão porta 8000, mas pode ser mudada com a flag `--port`. EX: `adk web --port 8001`

## 🧪 Testando

Exemplos de mensagens para enviar ao agente:
- "Hello!"
- "Hi there"
- "Good morning"

O agente sempre responderá com uma mensagem alegre de "Hello World!".

## 📚 O que este exemplo demonstra

- **Criação básica de um agente** com Google ADK
- **Integração com Google Gemini** (modelo gratuito - 1.500 req/dia)
- **Configuração de instruções** para o comportamento do agente
- **Execução via CLI e Web UI**

## 🔧 Modelo usado

- `gemini-2.0-flash-exp` (gratuito via Google AI Studio)

Você pode trocar por outros modelos Gemini disponíveis: https://ai.google.dev/gemini-api/docs/models/gemini