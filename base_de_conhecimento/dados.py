"""
Esse arquivo simula um banco de dados estático (usando dicionários python) para guardar relações entre diferentes
elementos do projeto


IMPORTANTE:

1. Os nomes dos itens aqui devem seguir o seguinte padrão de nomeclatura:
    - letras minúsculas
    - palavras separadas por underline (_)
    - sem acentuação
    - sem caracteres especiais (ex: ç, ã, ê, etc.)
"""

DADOS_ESFORCO = {
    'coordenacao_motora_fina': {
        'materiais': ['lapis_de_cor', 'giz_de_cera', 'pinceis', 'tesoura', 'cola', 'massinha_de_modelar', 'folhas_naturais', 'pedrinhas', 'pecas_de_encaixe', 'quebra_cabeca', 'mesa_de_coordenacao_motora_fina', 'material_de_pesca', 'papel', 'tinta_guache'],
        'ambientes': ['sala', 'cantina', 'biblioteca', 'solario_coberto'],
        'partes_do_corpo': ['dedos_das_maos', 'dedos_dos_pes', 'maos'],
        'metas_promovidas': ['organizacao_de_objetos', 'autonomia_nas_tarefas', 'desenho_e_pintura']
    },
    'coordenacao_motora_ampla': {
        'materiais': ['pula_pula', 'balanco', 'cavalinho_de_balanco', 'bamboles', 'cones_de_marcacao', 'bola_de_pilates', 'carrinhos', 'cordas', 'bolas'],
        'ambientes': ['parquinho', 'gramado', 'patio_descoberto', 'solario_descoberto', 'parquinho_de_areia', 'saguao_coberto'],
        'partes_do_corpo': ['pernas', 'corpo', 'quadris', 'ombros', 'bracos', 'cabeca'],
        'metas_promovidas': ['equilibrio_e_controle_corporal', 'expressao_corporal']
    },
    'logico': {
        'materiais': ['livros', 'jogos_de_tabuleiro', 'quebra_cabeca', 'blocos_de_montar', 'videos'],
        'ambientes': ['sala', 'biblioteca'],
        'partes_do_corpo': [],
        'metas_promovidas': ['resolucao_de_problemas', 'reconhecimento_de_padroes', 'obedecer_regras', 'imaginacao', 'pedir_ajuda']
    },
    'fisico': {
        'materiais': ['tinta_guache', 'areia', 'agua', 'massinha_de_modelar', 'instrumentos_musicais', 'musicas', 'folhas_naturais', 'comida', 'utensilios_de_higiene'],
        'ambientes': ['banheiro', 'cantina', 'parquinho_de_areia'],
        'partes_do_corpo': ['ouvidos', 'olhos', 'maos', 'boca', 'nariz'],
        'metas_promovidas': ['exploracao_sensorial', 'socializacao']
    }
}

# Objetivos automáticos para testes
SUBCAMPOS = {
    'EI02/03CG01' : ['objetivo' + str(i+ 1) for i in range(21)],
    'EI02/03CG02' : ['objetivo' + str(i+ 1) for i in range(9)],
    'EI02/03CG03' : ['objetivo' + str(i+ 1) for i in range(9)],
    'EI02/03CG04' : ['objetivo' + str(i+ 1) for i in range(9)],
    'EI02/03CG05' : ['objetivo' + str(i+ 1) for i in range(8)]
}