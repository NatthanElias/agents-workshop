# Example 3: Agent ReAct Data Scientist

Este exemplo demonstra um Agent ReAct usando LangChain que age como um Data Scientist, capaz de analisar dados de um CSV usando código Python.

## ▶️ Executar

```bash
python agent_data_scientist.py
```

O agent iniciará em modo interativo no terminal.

## 🧪 Testando

Exemplos de perguntas para fazer ao agent:

### Análises básicas:
- "Quantos registros existem no dataset?"
- "Quais são as colunas disponíveis?"
- "Mostre as primeiras 5 linhas"

### Análises por região:
- "Qual o total de vendas por região?"
- "Qual região vendeu mais?"
- "Quantos produtos foram vendidos em cada região?"

### Análises por produto:
- "Qual produto gerou mais receita?"
- "Qual a quantidade média vendida de cada produto?"
- "Liste os produtos ordenados por faturamento"

### Análises temporais:
- "Qual mês teve mais vendas?"
- "Mostre a evolução das vendas ao longo do tempo"

### Análises estatísticas:
- "Qual a média de vendas?"
- "Qual o desvio padrão das vendas?"
- "Quais são os valores máximo e mínimo de vendas?"

## 📚 O que este exemplo demonstra

- **ReAct Agent**: Padrão de raciocínio e ação (Reasoning + Acting)
- **Python REPL Tool**: Execução de código Python para análise de dados
- **Data Analysis**: Agent capaz de escrever e executar código para análise
- **Error Handling**: Agent capaz de corrigir erros e tentar novamente

## 🔧 Componentes

- **LLM**: `gemini-2.5-flash`
- **Tool**: `PythonREPLTool` para execução de código Python
- **Agent Type**: ReAct (Reasoning + Acting)
- **Data**: CSV com dados de vendas fictícios

## 💡 Como funciona

1. **Usuário faz uma pergunta** sobre os dados
2. **Agent raciocina** sobre como responder
3. **Agent escreve código Python** para analisar os dados
4. **Código é executado** no Python REPL
5. **Agent interpreta** os resultados
6. **Resposta final** é fornecida ao usuário

O ciclo ReAct pode se repetir várias vezes até o agent ter informações suficientes para responder.

## 📊 Estrutura do CSV

O arquivo `sales_data.csv` contém:
- `data`: Data da venda
- `regiao`: Região da venda (Norte, Sul, Leste, Oeste)
- `produto`: Nome do produto (Laptop, Mouse, Teclado, Monitor)
- `vendas`: Valor total da venda em R$
- `quantidade`: Quantidade de itens vendidos