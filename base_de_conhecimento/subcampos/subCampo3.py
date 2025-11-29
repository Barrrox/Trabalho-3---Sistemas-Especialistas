from base_de_conhecimento.vocabulario import *

# (EI02/03CG03) Explorar formas de deslocamento no espaço (pular, saltar, dançar), 
# combinando movimentos e seguindo orientações. 

# ==========================================
# Regras
# ==========================================

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG03') <= atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG03') <= atividade_desenvolve_saber(Atividade, 'esquema_corporal')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG03') <= atividade_desenvolve_saber(Atividade, 'danca')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG03') <= atividade_desenvolve_saber(Atividade, 'imitacao_como_expressao')

# ==========================================
# Regras específicas para saberes do subcampo
# ==========================================

atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') <= \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')
atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') <= \
    promove_tipo_esforco(Atividade, 'fisico') 
atividade_desenvolve_saber(Atividade, 'esquema_corporal') <= \
    tem_caracteristica(Atividade, 'expressao_sensorial')
atividade_desenvolve_saber(Atividade, 'danca') <= \
    tem_caracteristica(Atividade, 'expressao_corporal') & \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal')
atividade_desenvolve_saber(Atividade, 'imitacao_como_expressao') <= \
    tem_caracteristica(Atividade, 'socializacao')
atividade_desenvolve_saber(Atividade, 'imitacao_como_expressao') <= \
    tem_caracteristica(Atividade, 'expressao_corporal') & \
    tem_caracteristica(Atividade, 'reconhecimento_de_padroes')


# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

# OBJ1: Explorar espaco com movimentos
atinge_objetivo(Atividade, 'subcampo3_objetivo1') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos')

# OBJ2: Explorar mais em maiores espacos com variedade de movimentos
atinge_objetivo(Atividade, 'subcampo3_objetivo2') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')

