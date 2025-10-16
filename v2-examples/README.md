# Oficina Agents

## 📋 Pré-requisitos
- Python 3.10 ou superior
- Conta Google (gratuita)

## 🚀 Setup

### 1. Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar API Key
1. Acesse https://aistudio.google.com/apikey
2. Faça login com sua conta Google
3. Clique em "Create API key"
4. Copie a chave gerada
5. Crie o arquivo `.env`, copie o conteúdo de `.env.example` para `.env` e substitua `your_google_api_key_here` pela sua chave

**Tier gratuito**: 1.500 requisições por dia