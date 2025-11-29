"""
Esse arquivo cria todos os termos/predicados que serão usados no projeto

"""

from pyDatalog import pyDatalog as pyd

# Variáveis Genéricas e de Consulta
pyd.create_terms('Atividade, Material, Ambiente, ParteDoCorpo, Esforco, Caracteristica, Item')
pyd.create_terms('Y, Objetivo, SubCampo') # Variáveis para consultas

# Predicados de Entrada
pyd.create_terms('usa_ambiente, usa_material, usa_parte_do_corpo, promove_a_meta')

# Predicados Auxiliares e Intermediários
pyd.create_terms('caracteristica_implica_esforco')
pyd.create_terms('tem_caracteristica')
pyd.create_terms('promove_tipo_esforco')
pyd.create_terms('atividade_desenvolve_saber')
pyd.create_terms('atividade_pertence_ao_subcampo')

# Predicados de Metadados e Saída
pyd.create_terms('objetivo_pertence_ao_subcampo')
pyd.create_terms('atinge_objetivo')