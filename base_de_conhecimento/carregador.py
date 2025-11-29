"""
Esse arquivo define a função para carregar fatos no sistema

"""

from base_de_conhecimento.vocabulario import caracteristica_implica_esforco, objetivo_pertence_ao_subcampo
from base_de_conhecimento.dados import DADOS_ESFORCO, SUBCAMPOS # importa dados

def carregar_fatos_iniciais():
    """
    Função que deve ser chamada pelo __init__
    """
    # 1. Carrega Esforços
    for tipo_esforco, categorias in DADOS_ESFORCO.items():
        for lista_itens in categorias.values():
            for item in lista_itens:
                + caracteristica_implica_esforco(item, tipo_esforco)

    # 2. Carrega Objetivos (Metadados)
    for subcampo, objetivos in SUBCAMPOS.items():
        for objetivo in objetivos:
            + objetivo_pertence_ao_subcampo(objetivo, subcampo)
            
    # 3. Inicializa Predicados Vazios
    # No pydatalgo há um erro quando há um predicado sem nenhum fato vinculado. Para resolver
    # isso utilizamos de um truque (vulgo gambiarra) que consiste em inicializar o motor de 
    # inferência com um fato dummy e removê-lo logo depois.
    
    # Importamos aqui dentro para não poluir o escopo global
    from base_de_conhecimento.vocabulario import usa_ambiente, usa_material, usa_parte_do_corpo, promove_a_meta
    
    predicados_entrada = [usa_ambiente, usa_material, usa_parte_do_corpo, promove_a_meta]
    for P in predicados_entrada:
        + P('init', 'init')
        - P('init', 'init')