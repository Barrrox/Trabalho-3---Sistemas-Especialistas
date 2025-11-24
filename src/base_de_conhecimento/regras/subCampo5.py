from variaveis_e_predicados import *


# (EI02/03CG05) Desenvolver progressivamente as habilidades manuais, adquirindo controle 
# para desenhar, pintar, rasgar, folhear, entre outros

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG05') <= \
    (usa_partes_do_corpo(Atividade, 'maos') & \
    promove_tipo_esforco(Atividade, 'coordernacao_motora_fina')) | \
    usa_ambiente(Atividade, 'sala') | \
    usa_ambiente(Atividade, 'biblioteca')