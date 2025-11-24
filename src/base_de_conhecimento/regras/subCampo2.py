from variaveis_e_predicados import *


# (EI02/03CG02) Deslocar seu corpo no espaço, orientando-se por noções como em frente,
# atrás, no alto, embaixo, dentro, fora etc., ao se envolver em brincadeiras e atividades de
# diferentes naturezas.

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG02') <= \
    (promove_a_meta(Atividade, 'exploracao_sensorial') & \
    promove_a_meta(Atividade, 'equilibrio_e_controle_corporal') & \
    promove_a_meta(Atividade, 'expressao_corporal')) | \
    promove_a_meta(Atividade, 'organizacao_de_objetos') | \
    promove_a_meta(Atividade, 'autonomia_nas_tarefas') | \
    promove_a_meta(Atividade, 'obedecer_regras') | \
    (promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla') & \
    promove_tipo_esforco(Atividade, 'fisico')) | \
    promove_tipo_esforco(Atividade, 'logico')



