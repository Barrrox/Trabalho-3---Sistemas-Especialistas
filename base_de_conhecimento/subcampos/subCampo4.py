from base_de_conhecimento.variaveis_e_predicados import *

# (EI02/03CG04) Demonstrar progressiva independência no cuidado do seu corpo. 

# ==========================================
# Regras
# ==========================================

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG04') <= atividade_desenvolve_saber(Atividade, 'praticas_sociais_relativas_a_higiene')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG04') <= atividade_desenvolve_saber(Atividade, 'materiais_uso_pessoal')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG04') <= atividade_desenvolve_saber(Atividade, 'habitos_alimentares_de_higiene_e_repouso')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG04') <= atividade_desenvolve_saber(Atividade, 'cuidados_com_saude')

# ==========================================
# Regras específicas para saberes do subcampo
# ==========================================

atividade_desenvolve_saber(Atividade, 'praticas_sociais_relativas_a_higiene') <= \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    usa_material(Atividade, 'utensilios_de_higiene') & \
    tem_caracteristica(Atividade, 'obedecer_regras')
atividade_desenvolve_saber(Atividade, 'materiais_uso_pessoal') <= \
    usa_material(Atividade, 'objetos_pessoais')
atividade_desenvolve_saber(Atividade, 'habitos_alimentares_de_higiene_e_repouso') <= \
    usa_material(Atividade, 'utensilios_de_higiene') & \
    usa_material(Atividade, 'comida') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    usa_ambiente(Atividade, 'cantina') & \
    usa_ambiente(Atividade, 'banheiro')
atividade_desenvolve_saber(Atividade, 'cuidados_com_saude') <= \
    usa_material(Atividade, 'utensilios_de_higiene') & \
    tem_caracteristica(Atividade, 'exploracao_sensorial') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas')


# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

# OBJ1: Cuidar do corpo executando acoes de saude e higiene
atinge_objetivo(Atividade, 'subcampo4_objetivo1') <= \
    atividade_desenvolve_saber(Atividade, 'cuidados_com_saude') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas')

# OBJ2: Vivenciar praticas que desenvolvam bons habitos alimentares
atinge_objetivo(Atividade, 'subcampo4_objetivo2') <= \
    atividade_desenvolve_saber(Atividade, 'habitos_alimentares_de_higiene_e_repouso') & \
    usa_material(Atividade, 'comida') & \
    usa_ambiente(Atividade, 'cantina')

# OBJ3: Participar de momentos de cuidados de si, solicitando ajuda
atinge_objetivo(Atividade, 'subcampo4_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'praticas_sociais_relativas_a_higiene') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    tem_caracteristica(Atividade, 'pedir_ajuda') & \
    atividade_desenvolve_saber(Atividade, 'cuidados_com_saude')

# OBJ4: Participar de praticas de higiene com autonomia
atinge_objetivo(Atividade, 'subcampo4_objetivo4') <= \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    atividade_desenvolve_saber(Atividade, 'praticas_sociais_relativas_a_higiene')
    
# OBJ5: Identificar os cuidados basicos ouvindo as acoes a serem realizadas
atinge_objetivo(Atividade, 'subcampo4_objetivo5') <= \
    atividade_desenvolve_saber(Atividade, 'cuidados_com_saude') & \
    tem_caracteristica(Atividade, 'obedecer_regras') & \
    promove_tipo_esforco(Atividade, 'logico')

# OBJ6: Usar os utensilios apropriados na alimentacao e higiene
atinge_objetivo(Atividade, 'subcampo4_objetivo6') <= \
    usa_material(Atividade, 'utensilios_de_higiene') & \
    usa_material(Atividade, 'comida') & \
    atividade_desenvolve_saber(Atividade, 'habitos_alimentares_de_higiene_e_repouso') & \
    tem_caracteristica(Atividade, 'obedecer_regras')

# OBJ7: Utilizar o assento sanitario
atinge_objetivo(Atividade, 'subcampo4_objetivo7') <= \
    usa_material(Atividade, 'utensilios_de_higiene') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas')

# OBJ8: Conhecer o material de uso pessoal
atinge_objetivo(Atividade, 'subcampo4_objetivo8') <= \
    atividade_desenvolve_saber(Atividade, 'materiais_uso_pessoal') & \
    tem_caracteristica(Atividade, 'organizacao_de_objetos')

# OBJ9: Demonstrar as necessidades fisiologicas com gestos ou palavras
atinge_objetivo(Atividade, 'subcampo4_objetivo9') <= \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    tem_caracteristica(Atividade, 'pedir_ajuda') & \
    tem_caracteristica(Atividade, 'expressao_corporal')
