"""Esse arquivo faz um teste declarando regras e fatos necessários para tentar representar a
regra "Se saber_coordenação e manifestacao_cultural, então objetivo" que foi proposta pela Lóra"""

from pyDatalog import pyDatalog as pyd

# Declarando os termos que serão usados no teste

# variaveis
pyd.create_terms('Atividade, Saber, Material, Esforco, Objetivo, Y')

# ==========================================
# Predicados
# ==========================================

# Predicado de entrada
pyd.create_terms('usa_material, usa_espaco, tipo_esforco')

# Predicaos intermediarios
pyd.create_terms('desenvolve_saber, material_relacionado_ao_saber, saber_relacionado_ao_objetivo, esforco_relacionado_ao_saber') # parte esquerda do documento da proposta curricular

# Predicados de saída/finais
pyd.create_terms('atinge_objetivo') # parte direita do documento da proposta curricular

# ==========================================
# Fatos 
# ==========================================


# RELAÇÃO: SABER -> OBJETIVO
# Objetivo 2: Acompanhar ritmos de diferentes músicas com movimentos corporais.
+ saber_relacionado_ao_objetivo('coordenacao_motora_ampla', "Objetivo2")
+ saber_relacionado_ao_objetivo('manifestacoes_culturais', "Objetivo2")
# ... 

# RELAÇÃO: MATERIAL -> SABER
+ material_relacionado_ao_saber('Instrumentos musicais', 'manifestacoes_culturais')
+ material_relacionado_ao_saber('Instrumentos musicais', 'coordenacao_motora_ampla')
# ...

# RELAÇÃO: ESFORÇO -> SABER
+ esforco_relacionado_ao_saber('Coordenação motora ampla', 'coordenacao_motora_ampla')
+ esforco_relacionado_ao_saber('Coordenação motora fina', 'coordenacao_motora_fina')
# ...

# ==========================================
# Regras
# ==========================================


# Regra 1: Descobrir Saberes pelo MATERIAL
desenvolve_saber(Atividade, Saber) <= \
    usa_material(Atividade, Material) & \
    material_relacionado_ao_saber(Material, Saber)

# Regra 2: Descobrir Saberes pelo ESFORÇO
desenvolve_saber(Atividade, Saber) <= \
    tipo_esforco(Atividade, Esforco) & \
    esforco_relacionado_ao_saber(Esforco, Saber)

# Regra Principal/Final: Objetivo relacionado à atividade
atinge_objetivo(Atividade, Objetivo) <= \
    desenvolve_saber(Atividade, Saber) & \
    saber_relacionado_ao_objetivo(Saber, Objetivo)

# ==========================================
# Função para iniciar consulta / interface
# ==========================================

def iniciar_consulta():
    print("\n--- SISTEMA ESPECIALISTA CMEI ---")
    
    # Definimos um ID para a consulta atual
    atividade_atual = 'atividade_do_usuario'
    
    # PERGUNTA 1: Material
    print("\nQuais materiais foram usados? (Digite o número correspondente)")
    print("1. Instrumentos musicais")
    print("2. Papel e caneta")
    resp_mat = input(">> ")

    # PERGUNTA 2: Esforço
    print("\nQual o tipo de esforço principal? (Digite o número correspondente)")
    print("1. Coordenação motora ampla")
    print("2. Coordenação motora fina")
    print("3. Esforço Mental")
    resp_esf = input(">> ")
    
    # CRIAÇÃO DA MEMÓRIA DE TRABALHO
    # No PyDatalog, não existe uma interface direta para inserir regras na memoria de trabalho.
    if resp_mat == '1': # Se o usuário escolheu instrumentos musicais
        # Para adicionar fatos dinamicamente, devemos usar o operador +
        + usa_material(atividade_atual, 'Instrumentos musicais')
        print(f"-> Fato adicionado na memória: {atividade_atual} tem Instrumentos")
    
    # INSERINDO MAIS FATOS NA MEMÓRIA
    if resp_esf == '1':
        + tipo_esforco(atividade_atual, 'Coordenação motora ampla')
        print(f"-> Fato adicionado na memória: {atividade_atual} tem Coordenação Ampla")

    # ==========================================
    # 3. MOTOR DE INFERÊNCIA
    # ==========================================
    print("\n--- PROCESSANDO LÓGICA ---\n")
    
    # Debug: Ver quais saberes ele encontrou (Intermediário)
    saberes_encontrados = desenvolve_saber(atividade_atual, Y)
    print(f"Saberes detectados: {saberes_encontrados}")

    # Final: Ver objetivos
    resultado = atinge_objetivo(atividade_atual, Y)
    
    if resultado:
        print(f"SUCESSO! O sistema concluiu: {resultado[0][0]}")
    else:
        print("RESULTADO: Nenhum objetivo específico foi atingido com esses dados.")

# Executa o programa
if __name__ == "__main__":
    iniciar_consulta()