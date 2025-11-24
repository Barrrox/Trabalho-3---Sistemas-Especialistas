from variaveis_e_predicados import *


# (EI02/03CG04) Demonstrar progressiva independência no cuidado do seu corpo.

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG04') /
    (usa_ambiente(Atividade, 'banheiro') & /
    promove_a_meta(Atividade, 'obedecer_regras') & /
    promove_a_meta(Atividade, 'autonomia_nas_tarefas') & /
    usa_material(Atividade, 'utensilios_de_higiene')) | /
    usa_ambiente(Atividade, 'cantina') | /
    usa_material(Atividade, 'comida') | /
    usa_material(Atividade, 'utensilios_de_cozinha')



