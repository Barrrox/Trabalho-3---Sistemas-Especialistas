"""
variaveis_e_predicados.py

Este arquivo define:
1. Todos os termos (Vocabulário) do sistema.
2. A CAMADA 1 da lógica: Tradução de Fatos Brutos (Materiais/Corpo) para Tipos de Esforço.
"""
from pyDatalog import pyDatalog as pyd

# ===========================================
# 1. DEFINIÇÃO DE TERMOS (VOCABULÁRIO)
# ===========================================

# Variáveis Genéricas
pyd.create_terms('Atividade, Material, Ambiente, ParteCorpo, Meta, Y')

# Predicados de Entrada (Fatos Brutos)
pyd.create_terms('usa_ambiente, usa_material, usa_parte_do_corpo, promove_a_meta')

# Predicados Intermediários (Camadas de Abstração)
pyd.create_terms('promove_tipo_esforco')
pyd.create_terms('eh_material_da_categoria')
pyd.create_terms('atividade_desenvolve_saber')
pyd.create_terms('atividade_pertence_ao_subcampo')

# Predicado Final (Saída)
pyd.create_terms('atinge_objetivo')

# ===========================================
# REGRAS
# ===========================================


# ===========================================
# Tipo de esforço
# ===========================================

"""
A seguir, existem listas com os materiais associados a cada tipo de esforço.

Essas listas são necessárias pois o método de implementação de regras que utilizávamos
anteriormente (uma regra com vários OR's) travava o python ou o pydatalog por algum motivo.

Além disso, era grande e difícil de manter.

Agora existem essas listas com os materiais de cada categoria
e um loop que carrega esses fatos na memória.
"""

# Materiais relacionados à coordenação motora fina
materiais_fina = [
    'lapis_de_cor', 'giz_de_cera', 'pinceis', 'tesoura', 'cola',
    'massinha_de_modelar', 'folhas_naturais', 'pedrinhas', 
    'pecas_de_encaixe', 'quebra_cabeca', 'mesa_de_coordenacao_motora_fina',
    'material_de_pesca'
]

# Materiais relacionados ao esforço: coordenação motora ampla
materiais_ampla = [
    'pula_pula', 'balanco', 'cavalinho_de_balanco', 'bamboles',
    'cones_de_marcacao', 'bola_de_pilates', 'carrinhos'
]

# Materiais relacionados ao esforço lógico
materiais_logica = [
    'livros', 'jogos_de_tabuleiro', 'quebra_cabeca', 
    'blocos_de_montar', 'videos'
]

# Materiais relacionados ao esforço físico/sensorial
materiais_fisico = [
    'tinta_guache', 'areia', 'agua', 'massinha_de_modelar',
    'instrumentos_musicais', 'musicas', 'folhas_naturais',
    'comida', 'utensilios_de_higiene'
]

# Carregando os fatos na memória
for material in materiais_fina:
    + eh_material_da_categoria(material, 'fina')

for material in materiais_ampla:
    + eh_material_da_categoria(material, 'ampla')

for material in materiais_logica:
    + eh_material_da_categoria(material, 'logica')

for material in materiais_fisico:
    + eh_material_da_categoria(material, 'fisico')


# ---------------------------------------------------------
# 1. COORDENAÇÃO MOTORA FINA
# ---------------------------------------------------------

# Regra 1: Pela parte do corpo
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= usa_parte_do_corpo(Atividade, 'dedos_das_maos')
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= usa_parte_do_corpo(Atividade, 'dedos_dos_pes')

# Regra 2: Pelo material (Usa a categoria carregada no loop)
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= \
    usa_material(Atividade, Material) & \
    eh_material_da_categoria(Material, 'fina')

# Regra 3: Casos especiais (Versáteis)
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= \
    (usa_material(Atividade, 'cordas') & usa_parte_do_corpo(Atividade, 'dedos_das_maos'))

# Regra 4: Pelas metas
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= promove_a_meta(Atividade, 'organizacao_de_objetos')
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= promove_a_meta(Atividade, 'autonomia_nas_tarefas')


# ---------------------------------------------------------
# 2. COORDENAÇÃO MOTORA AMPLA
# ---------------------------------------------------------

# Regra 1: Corpo
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_parte_do_corpo(Atividade, 'pernas')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_parte_do_corpo(Atividade, 'corpo')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_parte_do_corpo(Atividade, 'quadris')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_parte_do_corpo(Atividade, 'ombros')

# Regra 2: Ambiente
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_ambiente(Atividade, 'parquinho')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_ambiente(Atividade, 'gramado')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= usa_ambiente(Atividade, 'patio_descoberto')

# Regra 3: Material Categórico
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= \
    usa_material(Atividade, Material) & \
    eh_material_da_categoria(Material, 'ampla')

# Regra 4: Casos Especiais (Versáteis)
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= \
    usa_material(Atividade, 'bolas') & usa_parte_do_corpo(Atividade, 'pes')

promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= \
    usa_material(Atividade, 'bolas') & usa_parte_do_corpo(Atividade, 'pernas')

promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= \
    usa_material(Atividade, 'bolas') & usa_parte_do_corpo(Atividade, 'corpo')

# Regra 5: Metas 
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= promove_a_meta(Atividade, 'equilibrio_e_controle_corporal')
promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') <= promove_a_meta(Atividade, 'expressao_corporal')


# ---------------------------------------------------------
# 3. ESFORÇO LÓGICO
# ---------------------------------------------------------

promove_tipo_esforco(Atividade, 'logico') <= \
    usa_material(Atividade, Material) & \
    eh_material_da_categoria(Material, 'logica')

# Metas 
promove_tipo_esforco(Atividade, 'logico') <= promove_a_meta(Atividade, 'resolucao_de_problemas')
promove_tipo_esforco(Atividade, 'logico') <= promove_a_meta(Atividade, 'reconhecimento_de_padroes')
promove_tipo_esforco(Atividade, 'logico') <= promove_a_meta(Atividade, 'obedecer_regras')
promove_tipo_esforco(Atividade, 'logico') <= promove_a_meta(Atividade, 'imaginacao')


# ---------------------------------------------------------
# 4. ESFORÇO FÍSICO / SENSORIAL
# ---------------------------------------------------------

promove_tipo_esforco(Atividade, 'fisico') <= \
    usa_material(Atividade, Material) & \
    eh_material_da_categoria(Material, 'fisico')

# Partes do corpo 
promove_tipo_esforco(Atividade, 'fisico') <= usa_parte_do_corpo(Atividade, 'ouvidos')
promove_tipo_esforco(Atividade, 'fisico') <= usa_parte_do_corpo(Atividade, 'olhos')
promove_tipo_esforco(Atividade, 'fisico') <= usa_parte_do_corpo(Atividade, 'maos')

# Metas 
promove_tipo_esforco(Atividade, 'fisico') <= promove_a_meta(Atividade, 'exploracao_sensorial')