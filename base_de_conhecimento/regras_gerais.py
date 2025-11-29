from base_de_conhecimento.vocabulario import *

# ===========================================
# 1. REGRAS DE UNIFICAÇÃO (O FUNIL)
# ===========================================
tem_caracteristica(Atividade, Caracteristica) <= usa_material(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= usa_ambiente(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= usa_parte_do_corpo(Atividade, Caracteristica)
tem_caracteristica(Atividade, Caracteristica) <= promove_a_meta(Atividade, Caracteristica)

# ===========================================
# 2. REGRA MESTRA TIPO DE ESFORÇO
# ===========================================
promove_tipo_esforco(Atividade, Esforco) <= \
    tem_caracteristica(Atividade, Caracteristica) & \
    caracteristica_implica_esforco(Caracteristica, Esforco)

# ===========================================
# 3. CASOS ESPECIAIS (a definir)
# ===========================================
promove_tipo_esforco(Atividade, 'coordenacao_motora_fina') <= \
    (tem_caracteristica(Atividade, 'cordas') & tem_caracteristica(Atividade, 'dedos_das_maos'))