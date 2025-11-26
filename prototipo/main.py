"""Esse arquivo faz um teste declarando regras e fatos necessários para tentar representar a
regra "Se saber_coordenação e manifestacao_cultural, então objetivo" que foi proposta pela Lóra"""

from pyDatalog import pyDatalog as pyd
from variaveis_e_predicados import *
from subCampo1 import *  


def iniciar_consulta():
    
    # declara variaveis locais
    pyd.create_terms('Y')

    
    print("\n--- SISTEMA ESPECIALISTA CMEI (TESTE) ---")
    
    # inicializa a variavel de atividade
    atividade_atual = 'atividade_do_usuario'
    
    # Exemplo de atividade: musica no patio
    + usa_material(atividade_atual, 'musicas')
    + usa_ambiente(atividade_atual, 'patio_descoberto')
    + usa_parte_do_corpo(atividade_atual, 'pernas')
    + usa_parte_do_corpo(atividade_atual, 'corpo')
    + usa_parte_do_corpo(atividade_atual, 'ouvidos')
    + promove_a_meta(atividade_atual, 'exploracao_sensorial')

    # ---------------------------------------------------------
    # MOTOR DE INFERÊNCIA (Consultas)
    # ---------------------------------------------------------

    print("\n--- [1] Análise de Sub Campo---")
    subcampos_encontrados = atividade_pertence_ao_subcampo(atividade_atual, Y)
    if subcampos_encontrados:
        for subcampo in subcampos_encontrados:
            print(f"-> Atividade pertence ao subcampo: {subcampo[0]}")


    # # PERGUNTA 1: Material
    # print("\nQuais materiais foram usados? (Digite o número correspondente)")
    # print("1. Instrumentos musicais")
    # print("2. Papel e caneta")
    # resp_mat = input(">> ")

    # # PERGUNTA 2: Esforço
    # print("\nQual o tipo de esforço principal? (Digite o número correspondente)")
    # print("1. Coordenação motora ampla")
    # print("2. Coordenação motora fina")
    # print("3. Esforço Mental")
    # resp_esf = input(">> ")
    
    # # CRIAÇÃO DA MEMÓRIA DE TRABALHO
    # # No PyDatalog, não existe uma interface direta para inserir regras na memoria de trabalho.
    # if resp_mat == '1': # Se o usuário escolheu instrumentos musicais
    #     # Para adicionar fatos dinamicamente, devemos usar o operador +
    #     + usa_material(atividade_atual, 'Instrumentos musicais')
    #     print(f"-> Fato adicionado na memória: {atividade_atual} tem Instrumentos")
    
    # # INSERINDO MAIS FATOS NA MEMÓRIA
    # if resp_esf == '1':
    #     + tipo_esforco(atividade_atual, 'Coordenação motora ampla')
    #     print(f"-> Fato adicionado na memória: {atividade_atual} tem Coordenação Ampla")

    # ==========================================
    # 3. MOTOR DE INFERÊNCIA
    # ==========================================
    print("\n--- PROCESSANDO LÓGICA ---\n")
    
    # Debug: Ver quais saberes ele encontrou (Intermediário)
    saberes_encontrados = atividade_desenvolve_saber(atividade_atual, Y)
    print(f"Saberes detectados: {saberes_encontrados}")

    # Final: Ver objetivos
    objetivos_atingidos = atinge_objetivo(atividade_atual, Y)
    saberes_encontrados = atividade_desenvolve_saber(atividade_atual, Y)
    subcampos_encontrados = atividade_pertence_ao_subcampo(atividade_atual, Y)

    
    if objetivos_atingidos:
        print(f"SUCESSO! O sistema concluiu: {objetivos_atingidos}\n")
    else:
        print("RESULTADO: Nenhum objetivo específico foi atingido com esses dados.\n")

    if saberes_encontrados:
        print(f"Saberes desenvolvidos pela atividade: {saberes_encontrados}\n")
    else:
        print("Nenhum saber foi desenvolvido pela atividade.\n")

    if subcampos_encontrados:
        print(f"Subcampos relacionados à atividade: {subcampos_encontrados}\n")
    else:
        print("Nenhum subcampo foi relacionado à atividade.\n")

# Executa o programa
if __name__ == "__main__":
    iniciar_consulta()