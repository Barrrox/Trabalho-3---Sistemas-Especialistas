"""
main.py

Interface de Linha de Comando (CLI) para o Sistema Especialista CMEI.
Responsável por coletar entradas do usuário, invocar o motor de inferência
e exibir os resultados em formato de árvore hierárquica.
"""

from pyDatalog import pyDatalog as pyd
# Importa regras específicas (necessário para que o pyDatalog conheça as implicações)
from base_de_conhecimento.subcampos.subCampo1 import *
from base_de_conhecimento.subcampos.subCampo2 import *
from base_de_conhecimento.subcampos.subCampo3 import *
from base_de_conhecimento.subcampos.subCampo4 import *
from base_de_conhecimento.subcampos.subCampo5 import *
from base_de_conhecimento.config_dados import DADOS_ESFORCO

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

        # Opção secreta para os devs :)
        if entrada == "tudo":
            selecionados = [lista_opcoes[i] for i in range(len(lista_opcoes))]
            escolha_valida = True
            return selecionados

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
    pyd.create_terms('Y')
    atividade_atual = 'atividade_usuario'

    # O pyDatalog falha se um predicado usado em regras não tiver NENHUM fato.
    # O truque abaixo adiciona um fato dummy e o remove imediatamente.
    # Isso inicializa a estrutura interna do motor para receber consultas vazias.
    
    + usa_ambiente('init', 'init')
    - usa_ambiente('init', 'init')

    + usa_material('init', 'init')
    - usa_material('init', 'init')

    + usa_parte_do_corpo('init', 'init')
    - usa_parte_do_corpo('init', 'init')

    + promove_a_meta('init', 'init')
    - promove_a_meta('init', 'init')
    
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

    # Busca os resultados (retorna lista de tuplas)
    # A variável 'objetivos' conterá algo como [('EI02CG01',), ('EI03TS02',)]
    objetivos_atingidos_consulta = atinge_objetivo(atividade_atual, Y)

    if not objetivos_atingidos_consulta:
        print(">> Nenhuma classificação encontrada (nenhum objetivo atingido).")
        return

    # ---------------------------------------------------------
    # 4. VISUALIZAÇÃO COM NOVA LÓGICA (DICIONÁRIO)
    # ---------------------------------------------------------

    # Cria dicionário para guardar os resultados: Chave = Subcampo (int), Valor = Set de Objetivos (int)
    # Suporta subcampos 1 a 4 (range(5) gera 0,1,2,3,4 - ignoramos o 0 ou ajustamos conforme necessidade)
    resultados = {i+1 : set() for i in range(5)}

    # Itera sobre a lista de objetivos atingidos para capturar
    # o numero do subcampo e seus respectivos objetivos atingidos
    for tupla_obj in objetivos_atingidos_consulta:
        subcampo_objetivo_str = tupla_obj[0] # Extrai a string da tupla
        
        try:
            # Lógica de parsing solicitada: índice 8 para subcampo, último char para objetivo
            subcampo = int(subcampo_objetivo_str[8]) 
            objetivo = int(subcampo_objetivo_str[-1])
            
            if subcampo in resultados:
                resultados[subcampo].add(objetivo)
        except (IndexError, ValueError):
            # Caso a string do objetivo não esteja no formato esperado (ex: muito curta)
            continue

    print("Resultados Classificados:\n")
    
    resultado_encontrado = False

    # Itera sobre o dicionário para exibir a árvore
    for num_subcampo, set_objetivos in resultados.items():
        if set_objetivos:
            resultado_encontrado = True
            print(f"Subcampo {num_subcampo}")
            
            lista_obj_ordenada = sorted(list(set_objetivos))
            
            for i, num_obj in enumerate(lista_obj_ordenada):
                # Verifica se é o último item para decidir o conector
                is_last = (i == len(lista_obj_ordenada) - 1)
                conector = "└──" if is_last else "├──"
                
                print(f"   {conector} Objetivo {num_obj}")
    
    if not resultado_encontrado:
        print("   └── (Nenhum objetivo específico identificado na análise)")

    print("\n" + "="*40)
    
   
if __name__ == "__main__":
    iniciar_consulta()