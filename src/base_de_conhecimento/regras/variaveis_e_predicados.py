"""
Esse arquivo define os nomes das variáveis e predicados que serão usados nas regras do 
sistema especialista.

"""
from pyDatalog import pyDatalog as pyd



# ==========================
# Variaveis
# ==========================
pyd.create_terms('Atividade, Objetivo, SubCampo')


# ==========================
# Predicados de entrada do usuario
# ==========================

# Ambientes 
    # sala, 
    # parquinho, 
    # solario_coberto, 
    # solario_descoberto, 
    # cantina, 
    # saguao_coberto, 
    # patio_descoberto, 
    # gramado, 
    # parquinho, 
    # parquinho_de_areia, 
    # biblioteca
    # banheiro
pyd.create_terms('usa_ambiente')

# Materiais
    # papel,
    # lapis_de_cor,
    # giz_de_cera,
    # tinta_guache,
    # pinceis,
    # massinha_de_modelar,
    # tesoura,
    # cola,
    # blocos_de_montar,
    # bolas,
    # cordas,
    # bamboles,
    # cones_de_marcacao,
    # livros,
    # instrumentos_musicais,
    # musicas,
    # videos,
    # areia,
    # agua,
    # folhas_naturais,
    # pedrinhas,
    # carrinhos,
    # bonecas,
    # pecas_de_encaixe,
    # pula_pula,
    # bola_de_pilates,
    # material_de_pesca,
    # mesa_de_coordenacao_motora_fina,
    # balanco,
    # cavalinho_de_balanco,
    # cadeira,
    # mesa,
    # quebra_cabeca,
    # jogos_de_tabuleiro,
    # comida
    # utensilios_de_higiene
    # utensilios_de_cozinha
pyd.create_terms('usa_material')

# Partes do corpo
    # maos,
    # pes,
    # bracos,
    # pernas,
    # cabeca,
    # olhos,
    # dedos_das_maos,
    # dedos_dos_pes,
    # ombros,
    # quadris,
    # ouvidos
pyd.create_terms('usa_parte_do_corpo')

# Metas
    # organizacao_de_objetos,
    # socializacao,
    # reconhecimento_de_padroes,
    # exploracao_sensorial,
    # equilibrio_e_controle_corporal,
    # expressao_corporal,
    # resolucao_de_problemas,
    # imaginacao,
    # autonomia_nas_tarefas,
    # obedecer_regras
pyd.create_terms('promove_a_meta')

# ==========================
# Predicados auxiliares
# ==========================

# Tipo de esforço
    # coordenacao_motora_fina,
    # coordenacao_motora_ampla,
    # logico,
    # fisico
pyd.create_terms('promove_tipo_esforco')

# ==========================
# Predicados intermediarios
# ==========================

pyd.create_terms('atividade_pertence_ao_subcampo')
pyd.create_terms('saber_relacionado_ao_subcampo')
pyd.create_terms('objetivo_relacionado_ao_saber')


# ==========================
# Regras
# ==========================

atividade_objetivo(Atividade, Objetivo) <= \
    atividade_pertence_ao_subcampo(Atividade, SubCampo) & \
    saber_relacionado_ao_subcampo(SubCampo, Saber) & \
    objetivo_relacionado_ao_saber(Saber, Objetivo)