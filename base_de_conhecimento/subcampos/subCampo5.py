from base_de_conhecimento.variaveis_e_predicados import *

# (EI02/03CG05) Desenvolver progressivamente as habilidades manuais, adquirindo controle 
# para desenhar, pintar, rasgar, folhear, entre outros. 

# ==========================================
# Regras
# ==========================================

atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG05') <= atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina')
atividade_pertence_ao_subcampo(Atividade, 'EI02/03CG05') <= atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear')


# ==========================================
# Regras específicas para saberes do subcampo
# ==========================================

atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') <= \
    tem_caracteristica(Atividade, 'desenho_e_pintura') & \
    tem_caracteristica(Atividade, 'maos')

atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'lapis_de_cor')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'giz_de_cera')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'pinceis')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'papel')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'tinta_guache')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'massinha_de_modelar')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'tesoura')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'cola')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'livros')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'quebra_cabeca')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'blocos_de_montar')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'pecas_de_encaixe')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'quebra_cabeca')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    usa_material(Atividade, 'mesa_de_coordenacao_motora_fina')
atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') <= \
    tem_caracteristica(Atividade, 'desenho_e_pintura') & \
    tem_caracteristica(Atividade, 'maos')



# ==========================================
# Regras específicas para objetivos do subcampo
# ==========================================

# OBJ1: Conhecer a forma como segura instrumentos graficos
atinge_objetivo(Atividade, 'subcampo5_objetivo1') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear')

# OBJ2: Virar paginas de livros, revistas, jornais, etc
atinge_objetivo(Atividade, 'subcampo5_objetivo2') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    tem_caracteristica(Atividade, 'autonomia_nas_tarefas') & \
    atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') & \
    usa_material(Atividade, 'livros')

# OBJ3: Manusear diferentes riscadores em suportes e planos variados
atinge_objetivo(Atividade, 'subcampo5_objetivo3') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    tem_caracteristica(Atividade, 'desenho_e_pintura') & \
    atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear')

# OBJ4: Explorar jogos de montar, empilhar e encaixar
atinge_objetivo(Atividade, 'subcampo5_objetivo4') <= \
    usa_material(Atividade, 'blocos_de_montar')
atinge_objetivo(Atividade, 'subcampo5_objetivo4') <= \
    usa_material(Atividade, 'pecas_de_encaixe')
atinge_objetivo(Atividade, 'subcampo5_objetivo4') <= \
    usa_material(Atividade, 'quebra_cabeca')

# OBJ5: Modelar diferentes formas de diferentes tamanhos com massinha, argila, etc
atinge_objetivo(Atividade, 'subcampo5_objetivo5') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    usa_material(Atividade, 'massinha_de_modelar') & \
    tem_caracteristica(Atividade, 'imaginacao')

# OBJ6: Explorar livros de materiais diversos
atinge_objetivo(Atividade, 'subcampo5_objetivo6') <= \
    atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') & \
    usa_material(Atividade, 'livros')

# OBJ7: Pintar, desenhar, rabiscar, folhear, rasgar, picotar utilizando diferentes recursos e suportes
atinge_objetivo(Atividade, 'subcampo5_objetivo7') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    atividade_desenvolve_saber(Atividade, 'suportes_materiais_e_instrumentos_para_desenhar_pintar_folhear') & \
    tem_caracteristica(Atividade, 'desenho_e_pintura')

# OBJ8: Participar de situacoes que envolvam o rasgar, o enrolar e o amassar
atinge_objetivo(Atividade, 'subcampo5_objetivo8') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    usa_material(Atividade, 'papel')
atinge_objetivo(Atividade, 'subcampo5_objetivo8') <= \
    atividade_desenvolve_saber(Atividade, 'coordenacao_motora_fina') & \
    usa_material(Atividade, 'massinha_de_modelar')
