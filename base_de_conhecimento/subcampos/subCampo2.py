from base_de_conhecimento.variaveis_e_predicados import *

# (EI02/03CG02) Deslocar seu corpo no espaço, orientando-se por noções como em frente, 
# atrás, no alto, embaixo, dentro, fora etc., ao se envolver em brincadeiras e atividades de 
# diferentes naturezas. 

# ==========================================
# Regras
# ==========================================

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG02') <= atividade_desenvolve_saber(Atividade, 'corpo_e_espaco')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG02') <= atividade_desenvolve_saber(Atividade, 'nocoes_espaciais')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG02') <= atividade_desenvolve_saber(Atividade, 'orientacao_espacial')

# ==========================================
# Regras específicas para saberes do subcampo
# ==========================================

atividade_desenvolve_saber(Atividade, 'corpo_e_espaco') <= \
    tem_caracteristica(Atividade, 'exploracao_sensorial') & \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal') & \
    tem_caracteristica(Atividade, 'expressao_corporal')
atividade_desenvolve_saber(Atividade, 'corpo_e_espaco') <= \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')
atividade_desenvolve_saber(Atividade, 'nocoes_espaciais') <= \
    tem_caracteristica(Atividade, 'reconhecimento_de_padroes') & \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')
atividade_desenvolve_saber(Atividade, 'orientacao_espacial') <= \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas')


# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

# OBJ1: Explorar espaco com movimentos
atinge_objetivo(Atividade, 'subcampo2_objetivo1') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_espaco')

# OBJ2: Localizar e buscar brinquedo
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'pecas_de_encaixe')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'quebra_cabeca')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'carrinhos')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'bolas')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'jogos_de_tabuleiro')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'blocos_de_montar')
atinge_objetivo(Atividade, 'subcampo2_objetivo2') <= \
    tem_caracteristica(Atividade, 'bonecas')

# OBJ3: Exploracoes com diferentes perspectivas
atinge_objetivo(Atividade, 'subcampo2_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'orientacao_espacial') & \
    tem_caracteristica(Atividade, 'exploracao_sensorial')

# OBJ4: percorrer trajetos inventados ou propostos
atinge_objetivo(Atividade, 'subcampo2_objetivo4') <= \
    atividade_desenvolve_saber(Atividade, 'corpo_e_espaco') & \
    atividade_desenvolve_saber(Atividade, 'nocoes_espaciais') & \
    tem_caracteristica(Atividade, 'obedecer_regras')

# OBJ5: Reconhecer local com pertences pessoais
atinge_objetivo(Atividade, 'subcampo2_objetivo5') <= \
    atividade_desenvolve_saber(Atividade, 'orientacao_espacial') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    usa_material(Atividade, 'objetos_pessoais')

# OBJ6: Observar e imitar colegas na exploracao
atinge_objetivo(Atividade, 'subcampo2_objetivo6') <= \
    atividade_desenvolve_saber(Atividade, 'orientacao_espacial') & \
    tem_caracteristica(Atividade, 'socializacao') & \
    tem_caracteristica(Atividade, 'reconhecimento_de_padroes')

# OBJ7: Participar de situações com comandos
atinge_objetivo(Atividade, 'subcampo2_objetivo7') <= \
    atividade_desenvolve_saber(Atividade, 'nocoes_espaciais') & \
    tem_caracteristica(Atividade, 'obedecer_regras')

# OBJ8: Explorar ambiente da escola considerando os elementos no espaco
atinge_objetivo(Atividade, 'subcampo2_objetivo8') <= \
    atividade_desenvolve_saber(Atividade, 'nocoes_espaciais')

# OBJ9: Participar de situacoes que o professor demonstra localização de objetos
atinge_objetivo(Atividade, 'subcampo2_objetivo9') <= \
    atividade_desenvolve_saber(Atividade, 'orientacao_espacial') & \
    tem_caracteristica(Atividade, 'obedecer_regras')
