from base_de_conhecimento.variaveis_e_predicados import *

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

# OBJ3: Deslocar-se de diferentes modos
atinge_objetivo(Atividade, 'subcampo3_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') & \
    promove_tipo_esforco(Atividade, 'coordenaca_motora_ampla') & \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal')
    
# OBJ4: Descobrir diferentes formas de exploracao e compartilhar com colegas
atinge_objetivo(Atividade, 'subcampo3_objetivo4') <= \
    tem_caracteristica(Atividade, 'exploracao_sensorial') & \
    tem_caracteristica(Atividade, 'socializacao')

# OBJ5: Dancar executando movimentos variados 
atinge_objetivo(Atividade, 'subcampo3_objetivo5') <= \
    atividade_desenvolve_saber(Atividade, 'danca') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')

# OBJ6: Realizar atividades corporais e vencer desafios motores
atinge_objetivo(Atividade, 'subcampo3_objetivo6') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') & \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal')

# OBJ7: Deslocamento e movimento do corpo fora e dentro da sala
atinge_objetivo(Atividade, 'subcampo3_objetivo7') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')

# OBJ8: Deslocar-se em ambientes livres ou passando por obstaculos
atinge_objetivo(Atividade, 'subcampo3_objetivo8') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_movimentos') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') & \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal')

# OBJ9: Participar de jogos de imitacao
atinge_objetivo(Atividade, 'subcampo3_objetivo9') <= \
    atividade_desenvolve_saber(Atividade, 'imitacao_como_expressao') & \
    tem_caracteristica(Atividade, 'socializacao')