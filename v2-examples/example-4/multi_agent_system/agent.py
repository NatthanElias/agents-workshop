from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search


# ==============================================================================
# 1. KNOWLEDGE BASE (documentos fictícios da empresa)
# ==============================================================================

COMPANY_DOCS = """
=== RELATÓRIO DE IMPACTO SOCIAL Q4 2024 ===

INDICADORES:
- Beneficiários atendidos: 800 crianças/jovens
- Relação educador-beneficiário: 1:15
- Taxa de sucesso: 82%
- Famílias impactadas: 650

EQUIPE:
- Educadores sociais: 40 profissionais
- Psicólogos: 8 profissionais
- Coordenadores: 5 profissionais

ORÇAMENTO ANUAL:
- Custos com pessoal: R$ 2.4M (60%)
- Infraestrutura: R$ 800K (20%)
- Material didático: R$ 500K (12.5%)
- Administração: R$ 300K (7.5%)

MISSÃO: "Transformar vidas através da educação de qualidade."
VISÃO: "Ser referência nacional em educação social até 2030."
VALORES: Compromisso social, excelência, respeito, transparência.
"""

# ==============================================================================
# 2. CSO AGENT (Chief Social Officer) - Análise de Impacto Social
# ==============================================================================

cso_agent = Agent(
    model="gemini-2.5-flash",
    name="cso_agent",
    description="Analista de impacto social",
    instruction=f"""Você é o Chief Social Officer (CSO).
    
KNOWLEDGE BASE:
{COMPANY_DOCS}

TAREFA: Analise o impacto social da decisão proposta.

FORMATO DE RESPOSTA:
**ANÁLISE CSO - IMPACTO SOCIAL**

**Stakeholders Afetados:**
[liste beneficiários, equipe, famílias]

**Impactos Identificados:**
[use dados da knowledge base]

**Recomendação:**
[APOIAR/REJEITAR/MODIFICAR com justificativa]""",
    output_key="cso_analysis"
)

# ==============================================================================
# 3. CMO AGENT (Chief Marketing Officer) - Análise de Mercado
# ==============================================================================

cmo_agent = Agent(
    model="gemini-2.5-flash",
    name="cmo_agent",
    description="Analista de mercado e competitividade",
    instruction="""Você é o Chief Marketing Officer (CMO).

TAREFA: Analise o mercado e competitividade usando google_search.

FORMATO DE RESPOSTA:
**ANÁLISE CMO - PERSPECTIVA DE MERCADO**

**Pesquisas Realizadas:**
[o que pesquisou]

**Análise Competitiva:**
[concorrentes e tendências]

**Recomendação:**
[síntese focada em competitividade]""",
    tools=[google_search],
    output_key="cmo_analysis"
)

# ==============================================================================
# 4. PARALLEL AGENT - Executa CSO e CMO simultaneamente
# ==============================================================================

parallel_analysts = ParallelAgent(
    name="parallel_analysts",
    description="Executa CSO e CMO em paralelo",
    sub_agents=[cso_agent, cmo_agent]
)

# ==============================================================================
# 5. CEO AGENT - Síntese e Decisão Final
# ==============================================================================

ceo_agent = Agent(
    model="gemini-2.5-flash",
    name="ceo_agent",
    description="CEO que sintetiza análises e decide",
    instruction="""Você é o Chief Executive Officer (CEO).

MISSÃO: "Transformar vidas através da educação de qualidade."
VISÃO: "Ser referência nacional em educação social até 2030."

VOCÊ RECEBERÁ as análises:
- {cso_analysis}
- {cmo_analysis}

FORMATO DE RESPOSTA:
**═══════════════════════════════════════════════════════════**
**RELATÓRIO EXECUTIVO - DECISÃO CEO**
**═══════════════════════════════════════════════════════════**

**1. CONTEXTO:**
[resumo da decisão]

**2. SÍNTESE DAS ANÁLISES:**
• CSO: [principais pontos]
• CMO: [principais pontos]

**3. ALINHAMENTO ESTRATÉGICO:**
[avaliação vs Missão/Visão]

**4. CENÁRIOS:**
• Cenário A: [descrição]
• Cenário B: [descrição]

**5. RECOMENDAÇÃO FINAL:**
🎯 DECISÃO: [escolha]
JUSTIFICATIVA: [porquê]

**6. PRÓXIMOS PASSOS:**
1. [ação 1]
2. [ação 2]

**═══════════════════════════════════════════════════════════**"""
)

# ==============================================================================
# 6. ROOT AGENT - Orquestrador Principal
# ==============================================================================

root_agent = SequentialAgent(
    name="root_agent",
    description="Orquestrador: executa análises paralelas e depois CEO",
    sub_agents=[parallel_analysts, ceo_agent]
)
