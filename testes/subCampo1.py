from variaveis_e_predicados import *

# (EI02/03CG01) Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e 
# nos jogos e brincadeiras.

# ==========================================
# Regras
# ==========================================

# Apropriar-se de gestos e movimentos...
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'orientacao_espacial')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'grupos_sociais_familia')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'esquema_corporal')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'materiais_de_higiene')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG01') <= atividade_desenvolve_saber(Atividade, 'orgaos_dos_sentidos')

# ==========================================
# Regras específicas para saberes do subcampo
# ==========================================

atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') <= \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')

atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') <= usa_material(Atividade, 'instrumentos_musicais')
atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') <= usa_material(Atividade, 'musicas')
    
# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

# OBJETIVO 1: Acompanhar ritmos de diferentes músicas com o corpo
atinge_objetivo(Atividade, 'subcampo1_objetivo2') <= \
    atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') & \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla')

# Objetivo teste
atinge_objetivo(Atividade, 'obj_teste1') <= \
    atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais')
atinge_objetivo(Atividade, 'obj_teste2') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla')