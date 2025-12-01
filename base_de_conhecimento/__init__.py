"""
Esse arquivo inicializa

"""

print("Inicializando Base de Conhecimento...")

# 1. Criar o Vocabulário (Termos vazios)
from . import vocabulario

# 2. Carregar os Fatos (Preencher os termos com dados estáticos)
from . import carregador
carregador.carregar_fatos_iniciais()

# 3. Carregar as Regras Gerais (Lógica Base)
from . import regras_gerais

# 4. Carregar os Subcampos (Regras Específicas)
# Aqui importamos todos os arquivos da pasta subcampos
from .subcampos import subCampo1
from .subcampos import subCampo2
from .subcampos import subCampo3
from .subcampos import subCampo4
from .subcampos import subCampo5

print("Base de Conhecimento Carregada")