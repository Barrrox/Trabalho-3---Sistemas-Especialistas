from base_de_conhecimento.variaveis_e_predicados import *

# (EI02/03CG01) Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e 
# nos jogos e brincadeiras.

# ==========================================
# Regras
# ==========================================

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

# Coordenação motora ampla: equilíbrio, destreza e postura corporal.
atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') <= \
    promove_tipo_esforco(Atividade, 'coordenacao_motora_ampla')

# Manifestações culturais
atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') <= \
    tem_caracteristica(Atividade, 'instrumentos_musicais')
atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') <= \
    tem_caracteristica(Atividade, 'musicas')

# Orientação espacial
atividade_desenvolve_saber(Atividade, 'orientacao_espacial') <= \
    promove_tipo_esforco(Atividade, 'coordenacao_motoroa_ampla')
atividade_desenvolve_saber(Atividade, 'orientacao_espacial') <= \
     tem_caracteristica(Atividade, 'jogos_de_tabuleiro')
atividade_desenvolve_saber(Atividade, 'orientacao_espacial') <= \
     tem_caracteristica(Atividade, 'quebra_cabeca')

# Grupos Sociais (família)
atividade_desenvolve_saber(Atividade, 'grupos_sociais(familia)') <= \
     tem_caracteristica(Atividade, 'obedecer_regras')
atividade_desenvolve_saber(Atividade, 'grupos_sociais(familia)') <= \
     tem_caracteristica(Atividade, 'socializacao')
    
# Esquema corporal
atividade_desenvolve_saber(Atividade, 'esquema_corporal') <= \
    tem_caracteristica(Atividade, 'exploracao_sensorial')
atividade_desenvolve_saber(Atividade, 'esquema_corporal') <= \
    tem_caracteristica(Atividade, 'equilibrio_e_controle_corporal')
atividade_desenvolve_saber(Atividade, 'esquema_corporal') <= \
    tem_caracteristica(Atividade, 'expressao_corporal')
    
# Materiais de higiene, procedimentos e cuidados consigo mesmo
atividade_desenvolve_saber(Atividade, 'materiais_de_higiene') <= \
    tem_caracteristica(Atividade, 'utensilios_de_higiene')

# Órgãos dos sentidos
atividade_desenvolve_saber(Atividade, 'orgaos_dos_sentidos') <= \
    usa_parte_do_corpo(Atividade, ParteDoCorpo) & \
    caracteristica_implica_esforco(ParteDoCorpo, 'fisico')
atividade_desenvolve_saber(Atividade, 'orgaos_dos_sentidos') <= \
    tem_caracteristica(Atividade, 'exploracao_sensorial')

# ...

# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

"""
❖ 
❖ 
❖ 
❖ 
❖ 
❖ .
❖ .
❖ .
❖ 9 Reconhecer texturas, formatos e tamanhos por meio da exploração de objetos.
❖ 10 Reconhecer diferentes temperaturas, por meio da experimentação.
❖ Explorar seu corpo e o corpo do outro, por meio do toque.
❖ Perceber diferentes sabores por meio da experimentação de diversos tipos de alimentos, com diferentes texturas.
❖ Reconhecer alimentos com diferentes sabores.
❖ Desenvolver a percepção olfativa, sentindo diferentes odores.
❖ Explorar o próprio corpo na perspectiva de
conhecê-lo, sentindo os seus movimentos, ouvindo
seus barulhos, conhecendo suas funções.
❖ Conhecer e apontar partes do seu corpo e mostrar a correspondência destas em seus colegas.(cabeça, dente, olho, boca, cabelo, unha, dedo, nariz, mão, pé, pescoço, umbigo, joelho, dentre outros).

❖ Vivenciar brincadeiras de esquema corporal, de
exploração e expressão diante do espelho,
utilizando as diferentes formas de linguagens e
percebendo suas características.
❖ Observar e imitar gestos e movimentos típicos dos
profissionais da escola e de sua comunidade
próxima.
❖ Expressar, por meio do corpo, de seus gestos e
movimentos, confortos e desconfortos.
❖ Perceber o desconforto do colega e oferecer-lhe
acolhimento.
❖ Participar de atividades que desenvolvam o chutar,
pegar, manusear, mover e transportar objetos com
diferentes características.

"""
# OBJETIVO 1: Participar de brincadeiras com cantigas, rimas, histórias,
# parlendas ou outras situações que envolvam movimentos corporais.
atinge_objetivo(Atividade, 'subcampo1_objetivo1') <= \
    atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais') & \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla')


# OBJETIVO 2: Acompanhar ritmos de diferentes músicas com o corpo
atinge_objetivo(Atividade, 'subcampo1_objetivo2') <= \
    tem_caracteristica(Atividade, 'musicas') & \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla')

# OBJETIVO 3: Executar movimentos e gestos a partir de estímulos visuais e auditivos.
atinge_objetivo(Atividade, 'subcampo1_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') & \
    tem_caracteristica(Atividade, 'olhos')
atinge_objetivo(Atividade, 'subcampo1_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') & \
    tem_caracteristica(Atividade, 'ouvidos')
atinge_objetivo(Atividade, 'subcampo1_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') & \
    tem_caracteristica(Atividade, 'exploracao_sensorial')


# OBJETIVO 4: Conhecer os objetos, materiais, expressões culturais corporais, danças,
# músicas e brincadeiras típicas de sua região e de sua cultura e de outras.
atinge_objetivo(Atividade, 'subcampo1_objetivo4') <= \
    atividade_desenvolve_saber(Atividade, 'manifestacoes_culturais')


# OBJETIVO 5: Imitar movimentos fundamentais, com auxílio do professor.
atinge_objetivo(Atividade, 'subcampo1_objetivo5') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_ampla') & \
    atividade_desenvolve_saber(Atividade, 'esquema_corporal')

# OBJETIVO 6: Identificar objetos por meio da visão
atinge_objetivo(Atividade, 'subcampo1_objetivo6') <= \
    atividade_desenvolve_saber(Atividade, 'orgaos_dos_sentidos') & \
    tem_caracteristica(Atividade, 'exploracao_sensorial') & \
    tem_caracteristica(Atividade, 'olhos')
    

# OBJETIVO 7: Manipular objetos, visando ao desenvolvimento da coordenação óculo-manual
atinge_objetivo(Atividade, 'subcampo1_objetivo7') <= \
    usa_parte_do_corpo(Atividade, ParteDoCorpo) & \
    caracteristica_implica_esforco(ParteDoCorpo, 'coordenacao_motora_fina') & \
    tem_caracteristica(Atividade, 'olhos') & \
    atividade_desenvolve_saber(Atividade, 'orgaos_dos_sentidos')

# OBJETIVO 8: Identificar, por meio de expressões e da linguagem, alguns sons presentes
# em seu cotidiano


    







