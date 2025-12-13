"""
variaveis_e_predicados.py

Este arquivo define:
1. Todos os termos (Vocabulário) do sistema.
2. A CAMADA 1 da lógica: Tradução de Entradas (Materiais/Corpo/Ambiente/Meta) para Tipos de Esforço.
   Utiliza os dados importados de 'config_dados.py' para gerar regras dinamicamente.
"""
from pyDatalog import pyDatalog as pyd
from base_de_conhecimento.config_dados import DADOS_ESFORCO

# ===========================================
# 1. DEFINIÇÃO DE TERMOS (VOCABULÁRIO)
# ===========================================

# Variáveis Genéricas
pyd.create_terms('Atividade, Material, Ambiente, ParteDoCorpo, Esforco, Caracteristica, Y')

# Predicados de Entrada (Fatos Brutos fornecidos pelo usuário)
pyd.create_terms('usa_ambiente, usa_material, usa_parte_do_corpo, promove_a_meta')

# Predicados Auxiliares
# Este predicado diz: "A caracteristica X (independente se é material, corpo, etc) implica esforço Y"
pyd.create_terms('caracteristica_implica_esforco')

# Predicados Intermediários (O Funil)
# Unifica todas as entradas do usuário em uma única estrutura lógica
pyd.create_terms('tem_caracteristica')

# Predicados Intermediários (Camadas de Abstração)
pyd.create_terms('promove_tipo_esforco')
pyd.create_terms('atividade_desenvolve_saber')
pyd.create_terms('atividade_pertence_ao_subcampo')

# Predicado Final (Saída)
pyd.create_terms('atinge_objetivo')


# ===========================================
# 2. CARREGANDO FATOS (CONFIG -> PYDATALOG)
# ===========================================

# O loop abaixo converte o dicionário do Python em Fatos do PyDatalog.
# Ex: Se DADOS_ESFORCO diz que 'bola' é material de 'coordenacao_ampla',
# o loop cria o fato lógico: caracteristica_implica_esforco('bola', 'coordenacao_ampla').

# Itera sobre todos os tipos de esforço definidos no DADOS_ESFORCO
for tipo_esforco, categorias in DADOS_ESFORCO.items():
    # Itera sobre todas as sub-listas (materiais, ambientes, corpo, metas)
    # e trata tudo como "Item"
    for lista_itens in categorias.values():
        # Itera sobre cada item na sub-lista (Ex: lápis_de_cor, dedos_das_maos, etc)
        for item in lista_itens:
            + caracteristica_implica_esforco(item, tipo_esforco)


# ===========================================
# 3. REGRAS DE UNIFICAÇÃO
# ===========================================
"""
Convertemos as entradas específicas do usuário em uma característica genérica.
Isso simplifica a regra de esforço.
"""
tem_caracteristica(Atividade, Caracteristica) <= usa_material(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= usa_ambiente(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= usa_parte_do_corpo(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= promove_a_meta(Atividade, Caracteristica)


# ===========================================
# 4. REGRA MESTRA DE TIPO DE ESFORÇO
# ===========================================
"""
Regra no topo da hierarquia do tipo de esforço que substitui todas as anteriores.
Se a atividade tem uma característica, e essa característica implica um esforço,
então a atividade promove esse esforço.
"""

promove_tipo_esforco(Atividade, Esforco) <= \
    tem_caracteristica(Atividade, Caracteristica) & \
    caracteristica_implica_esforco(Caracteristica, Esforco)