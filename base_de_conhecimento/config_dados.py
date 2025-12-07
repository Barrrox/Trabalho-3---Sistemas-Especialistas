"""
config_dados.py

Este arquivo serve como o banco de dados do sistema.
Aqui você define quais itens (materiais, ambientes, partes do corpo, metas)
estão associados a qual Tipo de Esforço.

Estrutura:

DADOS_ESFORCO = {
    'tipo_de_esforco': {
        'materiais': [material1, material2, ...],
        'ambientes': [ambiente1, ambiente2, ...],
        'partes_do_corpo': [parte_do_corpo1, parte_do_corpo2, ...],
        'metas_promovidas': [meta1, meta2, ...]
    }
}

IMPORTANTE:

1. Os nomes dos itens aqui devem seguir o seguinte padrão de nomeclatura:
    - letras minúsculas
    - palavras separadas por underline (_)
    - sem acentuação
    - sem caracteres especiais (ex: ç, ã, ê, etc.)

"""

DADOS_ESFORCO = {
    
    # =========================================================
    # 1. COORDENAÇÃO MOTORA FINA
    # =========================================================
    'coordenacao_motora_fina': {
        'materiais': [
            'lapis_de_cor', 'giz_de_cera', 'pinceis', 'tesoura', 'cola',
            'massinha_de_modelar', 'folhas_naturais', 'pedrinhas', 
            'pecas_de_encaixe', 'quebra_cabeca', 'mesa_de_coordenacao_motora_fina',
            'material_de_pesca', 'papel', 'tinta_guache', 'utensilios_de_higiene', 'bonecas'
        ],
        'ambientes': [
            'sala', 'refeitorio', 'biblioteca', 'solario'
        ],
        'partes_do_corpo': [
            'maos'
        ],
        'metas_promovidas': [
            'organizacao_de_objetos', 'autonomia_nas_tarefas', 'desenho_e_pintura'
        ]
    },

    # =========================================================
    # 2. COORDENAÇÃO MOTORA AMPLA
    # =========================================================
    'coordenacao_motora_ampla': {
        'materiais': [
            'pula_pula', 'balanco', 'cavalinho_de_balanco', 'bamboles',
            'cones_de_marcacao', 'bola_de_pilates', 'carrinhos', 'cordas',
            'bolas'
        ],
        'ambientes': [
            'parquinho', 'gramado', 'patio', 'solario',
            'parquinho_de_areia', 'saguao'
        ],
        'partes_do_corpo': [
            'pernas', 'quadris', 'ombros', 'bracos', 'cabeca'
        ],
        'metas_promovidas': [
            'equilibrio_e_controle_corporal', 'expressao_corporal'
        ]
    },

    # =========================================================
    # 3. ESFORÇO LÓGICO / COGNITIVO
    # =========================================================
    'logico': {
        'materiais': [
            'livros', 'jogos_de_tabuleiro', 'quebra_cabeca', 
            'blocos_de_montar', 'videos'
        ],
        'ambientes': [
            'sala', 'biblioteca'
        ],
        'partes_do_corpo': [
            # Geralmente lógico não é definido por parte do corpo, mas pode haver exceções
        ],
        'metas_promovidas': [
            'resolucao_de_problemas', 'reconhecimento_de_padroes', 
            'obedecer_regras', 'imaginacao', 'pedir_ajuda', 'socializacao'
        ]
    },

    # =========================================================
    # 4. ESFORÇO SENSORIAL
    # =========================================================
    'uso_dos_sentidos': {
        'materiais': [
            'areia', 'agua', 'massinha_de_modelar',
            'instrumentos_musicais', 'musicas', 'folhas_naturais',
            'comida', 'utensilios_de_higiene', 'objetos_pessoais'
        ],
        'ambientes': [
            'refeitorio', 'sala', 'parquinho_de_areia', 'banheiro'
        ],
        'partes_do_corpo': [
            'ouvidos', 'olhos', 'maos', 'boca', 'nariz'
        ],
        'metas_promovidas': [
            'exploracao_sensorial' 
        ]
    }
}

# =========================================================
# Mapeamento de Códigos de Subcampo para Descrição Completa
# =========================================================

SUBCAMPOS_COMPLETOS = {
    # Número do Subcampo : Descrição completa
    1: 'EI02/03CG01: Apropriar-se de gestos e movimentos de sua cultura no cuidado de si e nos jogos e brincadeiras.',
    2: 'EI02/03CG02: Deslocar seu corpo no espaço, orientando-se por noções como em frente, atrás, no alto, embaixo, dentro, fora etc., ao se envolver em brincadeiras e atividades de diferentes naturezas.',
    3: 'EI02/03CG03: Explorar formas de deslocamento no espaço (pular, saltar, dançar), combinando movimentos e seguindo orientações.',
    4: 'EI02/03CG04: Demonstrar progressiva independência no cuidado do seu corpo.',
    5: 'EI02/03CG05: Desenvolver progressivamente as habilidades manuais, adquirindo controle para desenhar, pintar, rasgar, folhear, entre outros.',
}

# =========================================================
# Códigos de Objetivos para Descrição Completa
# =========================================================

OBJETIVOS_COMPLETOS = {
    # Subcampo 1: (EI02/03CG01) Apropriar-se de gestos e movimentos de sua cultura...
    'subcampo1_objetivo1': 'Participar de brincadeiras com cantigas, rimas, histórias, parlendas ou outras situações que envolvam movimentos corporais.',
    'subcampo1_objetivo2': 'Acompanhar ritmos de diferentes músicas com o corpo.',
    'subcampo1_objetivo3': 'Executar movimentos e gestos a partir de estímulos visuais e auditivos.',
    'subcampo1_objetivo4': 'Conhecer os objetos, materiais, expressões culturais corporais, danças, músicas e brincadeiras típicas de sua região e de sua cultura e de outras.',
    'subcampo1_objetivo5': 'Imitar movimentos fundamentais, com auxílio do professor.',
    'subcampo1_objetivo6': 'Identificar objetos por meio da visão.',
    'subcampo1_objetivo7': 'Manipular objetos, visando ao desenvolvimento da coordenação óculo-manual.',
    'subcampo1_objetivo8': 'Identificar, por meio de expressões e da linguagem, alguns sons presentes em seu cotidiano.',
    'subcampo1_objetivo9': 'Reconhecer texturas, formatos e tamanhos por meio da exploração de objetos.',
    'subcampo1_objetivo10': 'Reconhecer diferentes temperaturas, por meio da experimentação.',
    'subcampo1_objetivo11': 'Explorar seu corpo e o corpo do outro, por meio do toque.',
    'subcampo1_objetivo12': 'Perceber diferentes sabores por meio da experimentação de diversos tipos de alimentos, com diferentes texturas.',
    'subcampo1_objetivo13': 'Reconhecer alimentos com diferentes sabores.',
    'subcampo1_objetivo14': 'Desenvolver a percepção olfativa, sentindo diferentes odores.',
    'subcampo1_objetivo15': 'Explorar o próprio corpo na perspectiva de conhecê-lo, sentindo os seus movimentos, ouvindo seus barulhos, conhecendo suas funções.',
    'subcampo1_objetivo16': 'Conhecer e apontar partes do seu corpo e mostrar a correspondência destas em seus colegas (cabeça, dente, olho, boca, cabelo, unha, dedo, nariz, mão, pé, pescoço, umbigo, joelho, dentre outros).',
    'subcampo1_objetivo17': 'Vivenciar brincadeiras de esquema corporal, de exploração e expressão diante do espelho, utilizando as diferentes formas de linguagens e percebendo suas características.',
    'subcampo1_objetivo18': 'Observar e imitar gestos e movimentos típicos dos profissionais da escola e de sua comunidade próxima.',
    'subcampo1_objetivo19': 'Expressar, por meio do corpo, de seus gestos e movimentos, confortos e desconfortos.',
    'subcampo1_objetivo20': 'Perceber o desconforto do colega e oferecer-lhe acolhimento.',
    'subcampo1_objetivo21': 'Participar de atividades que desenvolvam o chutar, pegar, manusear, mover e transportar objetos com diferentes características.',

    # Subcampo 2: (EI02/03CG02) Deslocar seu corpo no espaço, orientando-se por noções como em frente, atrás...
    'subcampo2_objetivo1': 'Explorar espaço com movimentos.',
    'subcampo2_objetivo2': 'Localizar e buscar brinquedo.',
    'subcampo2_objetivo3': 'Explorações com diferentes perspectivas.',
    'subcampo2_objetivo4': 'Percorrer trajetos inventados ou propostos.',
    'subcampo2_objetivo5': 'Reconhecer local com pertences pessoais.',
    'subcampo2_objetivo6': 'Observar e imitar colegas na exploração.',
    'subcampo2_objetivo7': 'Participar de situações com comandos.',
    'subcampo2_objetivo8': 'Explorar ambiente da escola considerando os elementos no espaço.',
    'subcampo2_objetivo9': 'Participar de situações que o professor demonstra localização de objetos.',
    
    # Subcampo 3: (EI02/03CG03) Explorar formas de deslocamento no espaço (pular, saltar, dançar)...
    'subcampo3_objetivo1': 'Explorar espaço com movimentos.',
    'subcampo3_objetivo2': 'Explorar mais em maiores espaços com variedade de movimentos.',
    'subcampo3_objetivo3': 'Deslocar-se de diferentes modos.',
    'subcampo3_objetivo4': 'Descobrir diferentes formas de exploração e compartilhar com colegas.',
    'subcampo3_objetivo5': 'Dançar executando movimentos variados.',
    'subcampo3_objetivo6': 'Realizar atividades corporais e vencer desafios motores.',
    'subcampo3_objetivo7': 'Deslocamento e movimento do corpo fora e dentro da sala.',
    'subcampo3_objetivo8': 'Deslocar-se em ambientes livres ou passando por obstáculos.',
    'subcampo3_objetivo9': 'Participar de jogos de imitação.',

    # Subcampo 4: (EI02/03CG04) Demonstrar progressiva independência no cuidado do seu corpo.
    'subcampo4_objetivo1': 'Cuidar do corpo executando ações de saúde e higiene.',
    'subcampo4_objetivo2': 'Vivenciar práticas que desenvolvam bons hábitos alimentares.',
    'subcampo4_objetivo3': 'Participar de momentos de cuidados de si, solicitando ajuda.',
    'subcampo4_objetivo4': 'Participar de práticas de higiene com autonomia.',
    'subcampo4_objetivo5': 'Identificar os cuidados básicos ouvindo as ações a serem realizadas.',
    'subcampo4_objetivo6': 'Usar os utensílios apropriados na alimentação e higiene.',
    'subcampo4_objetivo7': 'Utilizar o assento sanitário.',
    'subcampo4_objetivo8': 'Conhecer o material de uso pessoal.',
    'subcampo4_objetivo9': 'Demonstrar as necessidades fisiológicas com gestos ou palavras.',

    # Subcampo 5: (EI02/03CG05) Desenvolver progressivamente as habilidades manuais...
    'subcampo5_objetivo1': 'Conhecer a forma como segura instrumentos gráficos.',
    'subcampo5_objetivo2': 'Virar páginas de livros, revistas, jornais, etc.',
    'subcampo5_objetivo3': 'Manusear diferentes riscadores em suportes e planos variados.',
    'subcampo5_objetivo4': 'Explorar jogos de montar, empilhar e encaixar.',
    'subcampo5_objetivo5': 'Modelar diferentes formas de diferentes tamanhos com massinha, argila, etc.',
    'subcampo5_objetivo6': 'Explorar livros de materiais diversos.',
    'subcampo5_objetivo7': 'Pintar, desenhar, rabiscar, folhear, rasgar, picotar utilizando diferentes recursos e suportes.',
    'subcampo5_objetivo8': 'Participar de situações que envolvam o rasgar, o enrolar e o amassar.',
}