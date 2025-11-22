"""Esse arquivo faz um teste declarando regras e fatos necessários para tentar representar a
regra "Se saber_coordenação e manifestacao_cultural, então objetivo" que foi proposta pela Lóra"""

from pyDatalog import pyDatalog as pyd

# Declarando os termos que serão usados no teste

# variaveis
pyd.create_terms('X, Y')

# entradas
pyd.create_terms('tem_material, usa_espaco, tipo_esforco')

# intermediarias
pyd.create_terms('desenvolve_saber') # parte esquerda do documento da proposta curricular


# saida
pyd.create_terms('atinge_objetivo') # parte direita do documento da proposta curricular

# ==========================================
# Fatos (HARDCODED)
# ==========================================

# Exemplo de fatos que poderiam ser inseridos na memória de trabalho 
# de forma HARDCODED

# Cenário: Uma atividade de dança/música no pátio

# # 1. Fato que ativa cultura
# + tem_material('atividade_01', 'Instrumentos musicais')

# # 2. Fato que ativa coordenação motora ampla
# + tipo_esforco('atividade_01', 'Coordenação motora ampla')

# ==========================================
# Regras
# ==========================================

# Regra Intermediária 1: Definindo como se chega em "Coordenação motora ampla"
# Se a atividade é no pátio OU exige esforço de coordenação -> Gera o saber
desenvolve_saber(X, 'coordenacao_motora_ampla') <= \
    tipo_esforco(X, 'Coordenação motora ampla')

# Regra Intermediária 2: Definindo como se chega em "Manifestações culturais"
desenvolve_saber(X, 'manifestacoes_culturais') <= \
    tem_material(X, 'Instrumentos musicais')

# Objetivo1: "Desenvolver saberes relacionados à coordenação de projetos culturais e à
# manifestação cultural na comunidade escolar"
atinge_objetivo(X, 'Objetivo1') <= \
    desenvolve_saber(X, 'coordenacao_motora_ampla') & \
    desenvolve_saber(X, 'manifestacoes_culturais')

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
        + tem_material(atividade_atual, 'Instrumentos musicais')
        print(f"-> Fato adicionado na memória: {atividade_atual} tem Instrumentos")
    
    # INSERINDO MAIS FATOS NA MEMÓRIA
    if resp_esf == '1':
        + tipo_esforco(atividade_atual, 'Coordenação motora ampla')
        print(f"-> Fato adicionado na memória: {atividade_atual} tem Coordenação Ampla")

    # ==========================================
    # 3. MOTOR DE INFERÊNCIA
    # ==========================================
    print("\n--- PROCESSANDO LÓGICA ---\n")
    
    # O pyDatalog agora olha para a memória que acabamos de criar e tenta resolver X
    resultado = atinge_objetivo(atividade_atual, Y)
    
    if resultado:
        print(f"SUCESSO! O sistema concluiu: {resultado[0][0]}")
    else:
        print("RESULTADO: Nenhum objetivo específico foi atingido com esses dados.")

# Executa o programa
if __name__ == "__main__":
    iniciar_consulta()