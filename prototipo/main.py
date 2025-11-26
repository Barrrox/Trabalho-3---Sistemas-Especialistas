"""
main.py

Interface de Linha de Comando (CLI) para o Sistema Especialista CMEI.
Responsável por coletar entradas do usuário, invocar o motor de inferência
e exibir os resultados em formato de árvore hierárquica.
"""

from pyDatalog import pyDatalog as pyd
from variaveis_e_predicados import *
# Importa regras específicas (necessário para que o pyDatalog conheça as implicações)
from subCampo1 import * # Importa os dados para gerar os menus dinamicamente
from config_dados import DADOS_ESFORCO

def obter_opcoes_unicas(chave_dicionario):
    """
    Varre todo o config_dados e retorna uma lista 
    de todos os itens de uma categoria (ex: todos os materiais).
    """
    itens = set()
    for categoria in DADOS_ESFORCO.values():
        lista = categoria.get(chave_dicionario, [])
        itens.update(lista)
    return sorted(list(itens))

def exibir_menu_e_selecionar(titulo, lista_opcoes):
    """
    Exibe uma lista numerada e solicita ao usuário que escolha os índices.
    Retorna uma lista com as strings escolhidas.
    """
    print(f"\n=== {titulo} ===")
    print("  - Digite os números separados por vírgula. Ex: 1, 3, 5")
    print("  - Pressione Enter sem digitar nada para selecionar nenhum")
    
    for i, item in enumerate(lista_opcoes):
        # # Formata o texto para ficar mais bonito (troca _ por espaço)
        # nome_exibicao = item.replace('_', ' ').capitalize()
        print(f"[{i}] {item}")
    
    escolha_valida = False
    selecionados = []
    
    while not escolha_valida:
        entrada = input(">> ")
        if not entrada.strip():
            # Se der enter vazio, retorna lista vazia (nenhuma seleção)
            return []
            
        try:
            indices = [int(x.strip()) for x in entrada.split(',')]
            
            print(indices)
            # Valida se os indices existem
            if any(i < 0 or i >= len(lista_opcoes) for i in indices):
                print("ERRO: Um ou mais números são inválidos. Tente novamente.")
                continue
                
            selecionados = [lista_opcoes[i] for i in indices]
            escolha_valida = True
        except ValueError:
            print("ERRO: Digite apenas números separados por vírgula.")
            
    return selecionados

def iniciar_consulta():
    # Inicializa variáveis do PyDatalog
    pyd.create_terms('Y, Z')
    atividade_atual = 'atividade_usuario'
    
    print("\n#################################################")
    print("### SISTEMA ESPECIALISTA: EDUCAÇÃO INFANTIL ###")
    print("#################################################")
    print("Responda às perguntas para classificar a atividade.")

    # ---------------------------------------------------------
    # 1. COLETA DE DADOS (Entradas)
    # ---------------------------------------------------------
    
    # Gera listas únicas a partir do config
    lista_ambientes = obter_opcoes_unicas('ambientes')
    lista_materiais = obter_opcoes_unicas('materiais')
    lista_corpo = obter_opcoes_unicas('partes_do_corpo')
    lista_metas = obter_opcoes_unicas('metas_promovidas')
    
    # Interação com usuário
    ambientes_escolhidos = exibir_menu_e_selecionar("ONDE a atividade foi realizada?", lista_ambientes)
    materiais_escolhidos = exibir_menu_e_selecionar("QUAIS MATERIAIS foram utilizados?", lista_materiais)
    corpo_escolhidos = exibir_menu_e_selecionar("QUAIS PARTES DO CORPO foram utilizadas?", lista_corpo)
    metas_escolhidas = exibir_menu_e_selecionar("QUAIS METAS foram estimuladas?", lista_metas)
    
    # Feedback visual
    print("\n" + "="*40)
    print("RESUMO DA ATIVIDADE:")
    print(f"Locais: {', '.join(ambientes_escolhidos) if ambientes_escolhidos else 'Nenhum'}")
    print(f"Materiais: {', '.join(materiais_escolhidos) if materiais_escolhidos else 'Nenhum'}")
    print(f"Corpo: {', '.join(corpo_escolhidos) if corpo_escolhidos else 'Nenhum'}")
    print(f"Metas: {', '.join(metas_escolhidas) if metas_escolhidas else 'Nenhum'}")
    print("="*40)

    # ---------------------------------------------------------
    # 2. INSERÇÃO NA MEMÓRIA DE TRABALHO
    # ---------------------------------------------------------
    
    # Limpa fatos antigos da memória (boa prática em loops, embora aqui seja run-once)
    # pyd.clear() # Cuidado: isso pode limpar as regras também dependendo da versão. 
                  # Melhor apenas adicionar os novos fatos para essa instância.

    for item in ambientes_escolhidos:
        + usa_ambiente(atividade_atual, item)
        
    for item in materiais_escolhidos:
        + usa_material(atividade_atual, item)
        
    for item in corpo_escolhidos:
        + usa_parte_do_corpo(atividade_atual, item)
        
    for item in metas_escolhidas:
        + promove_a_meta(atividade_atual, item)

    # ---------------------------------------------------------
    # 3. MOTOR DE INFERÊNCIA E EXIBIÇÃO
    # ---------------------------------------------------------
    print("\n--- ANALISANDO RESULTADOS ---\n")

    # Busca os resultados
    subcampos = atividade_pertence_ao_subcampo(atividade_atual, Y)
    saberes = atividade_desenvolve_saber(atividade_atual, Y)
    objetivos = atinge_objetivo(atividade_atual, Y)
    
    # Formata para listas limpas (pyDatalog retorna lista de tuplas ex: [('saber1',), ('saber2',)])
    lista_subcampos = sorted([x[0] for x in subcampos]) if subcampos else []
    lista_saberes = sorted([x[0] for x in saberes]) if saberes else []
    lista_objetivos = sorted([x[0] for x in objetivos]) if objetivos else []

    if not lista_subcampos:
        print(">> Nenhuma classificação encontrada. Tente fornecer mais detalhes.")
        return

    # ---------------------------------------------------------
    # 4. VISUALIZAÇÃO EM ÁRVORE
    # ---------------------------------------------------------
    # Como o pyDatalog desacopla as queries, montamos a árvore assumindo 
    # que os saberes e objetivos encontrados pertencem ao contexto dos subcampos válidos.
    
    print("Resultados Classificados:")
    
    for sub in lista_subcampos:
        print(f"\n SubCampo: {sub}")
        
        if not lista_saberes:
             print("    └── (Nenhum saber específico identificado)")
             continue

        for i, saber in enumerate(lista_saberes):
            # Formatação do conector da árvore
            conector_saber = "├──" if i < len(lista_saberes) - 1 else "└──"
            print(f"   {conector_saber}  Saber: {saber.replace('_', ' ')}")
            
            # Aqui listamos os objetivos. 
            # Nota: Idealmente, filtraríamos quais objetivos pertencem a este saber específico.
            # Como o predicado é global, listamos os objetivos atingidos neste contexto.
            if lista_objetivos:
                for j, obj in enumerate(lista_objetivos):
                    conector_obj = "│      ├──" if j < len(lista_objetivos) - 1 else "│      └──"
                    # Se for o último saber, ajusta a indentação visual
                    if conector_saber == "└──":
                         conector_obj = "       ├──" if j < len(lista_objetivos) - 1 else "       └──"
                    
                    print(f"   {conector_obj}  Objetivo: {obj.replace('_', ' ')}")
            else:
                prefixo_vazio = "│" if conector_saber == "├──" else " "
                print(f"   {prefixo_vazio}      └── (Nenhum objetivo curricular fechado atingido)")

    print("\n" + "="*40)

if __name__ == "__main__":
    iniciar_consulta()