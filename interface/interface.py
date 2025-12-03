import customtkinter as ctk
import sys
import os

# =========================================================
# CONFIGURAÇÃO DE CAMINHOS
# =========================================================
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
    project_root = base_path
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.append(project_root)

# =========================================================
# IMPORTS DO SISTEMA ESPECIALISTA
# =========================================================
from pyDatalog import pyDatalog as pyd
from base_de_conhecimento.subcampos.subCampo1 import *
from base_de_conhecimento.subcampos.subCampo2 import *
from base_de_conhecimento.subcampos.subCampo3 import *
from base_de_conhecimento.subcampos.subCampo4 import *
from base_de_conhecimento.subcampos.subCampo5 import *
from base_de_conhecimento.config_dados import DADOS_ESFORCO

# =========================================================
# LÓGICA DO SISTEMA
# =========================================================

def obter_opcoes_unicas(chave):
    itens = set()
    for categoria in DADOS_ESFORCO.values():
        lista = categoria.get(chave, [])
        itens.update(lista)
    return sorted(list(itens))

def formatar_texto(texto):
    return texto.replace('_', ' ').capitalize()

def inicializar_pydatalog():
    pyd.create_terms('Y')
    # Inicializa fatos dummy para evitar erros de primeira execução
    + usa_ambiente('init', 'init'); - usa_ambiente('init', 'init')
    + usa_material('init', 'init'); - usa_material('init', 'init')
    + usa_parte_do_corpo('init', 'init'); - usa_parte_do_corpo('init', 'init')
    + promove_a_meta('init', 'init'); - promove_a_meta('init', 'init')

# =========================================================
# INTERFACE GRÁFICA (CustomTkinter)
# =========================================================

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title("Sistema Especialista - Educação Infantil")
        self.geometry("900x800")
        
        # Inicializa Lógica
        inicializar_pydatalog()
        
        # --- ESTRUTURA DE LAYOUT ---
        # Ordem de empacotamento (pack) é importante aqui
        # Queremos:
        # 1. Resultados (Fixo no fundo)
        # 2. Botões (Fixo acima dos resultados)
        # 3. Formulário (Restante do espaço no topo, rolável)

        # 1. Frame Inferior (Resultados - Fixo)
        self.frame_resultados = ctk.CTkFrame(self)
        self.frame_resultados.pack(side="bottom", fill="x", padx=10, pady=(5, 10))

        # 2. Frame de Botões (Ações - Fixo)
        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack(side="bottom", fill="x", padx=20, pady=(10, 5))

        # 3. Frame Superior (Formulário - Rolável e Expansível)
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Formulário de Atividade")
        self.scroll_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # Dicionário para guardar as checkboxes e seus valores
        self.checkboxes = {
            'ambientes': [],
            'materiais': [],
            'corpo': [],
            'metas': []
        }

        # PREENCHIMENTO DO FORMULÁRIO
        self.add_section("1. Onde a atividade foi realizada?", 'ambientes')
        self.add_section("2. Quais materiais foram utilizados?", 'materiais')
        self.add_section("3. Quais partes do corpo foram usadas?", 'partes_do_corpo', key_storage='corpo')
        self.add_section("4. Quais metas foram estimuladas?", 'metas_promovidas', key_storage='metas')

        # BOTÕES DE AÇÃO 
        
        # Botão Limpar / Nova Consulta
        self.btn_limpar = ctk.CTkButton(
            self.frame_botoes, 
            text="NOVA CONSULTA", 
            height=50,
            fg_color="#555555",
            hover_color="#333333",
            font=("Arial", 14, "bold"),
            command=self.limpar_tudo
        )
        self.btn_limpar.pack(side="left", fill="x", expand=True, padx=(0, 10))

        # Botão Analisar
        self.btn_analisar = ctk.CTkButton(
            self.frame_botoes, 
            text="VER RESULTADOS", 
            height=50,
            fg_color="#2CC985",
            hover_color="#229A66",
            font=("Arial", 16, "bold"),
            command=self.analisar_resultados
        )
        self.btn_analisar.pack(side="right", fill="x", expand=True, padx=(10, 0))

        # --- ÁREA DE RESULTADO (Fixo embaixo) ---
        self.lbl_resultado = ctk.CTkLabel(self.frame_resultados, text="Resultados da Análise:", font=("Arial", 18, "bold"), anchor="w")
        self.lbl_resultado.pack(fill="x", padx=10, pady=(10, 5))

        self.textbox_resultado = ctk.CTkTextbox(self.frame_resultados, height=200, font=("Consolas", 14))
        self.textbox_resultado.pack(fill="x", padx=10, pady=(0, 10))
        self.textbox_resultado.insert("0.0", "Preencha o formulário acima e clique em 'Ver Resultados'.")
        self.textbox_resultado.configure(state="disabled")

    def add_section(self, titulo, chave_dados, key_storage=None):
        if key_storage is None: key_storage = chave_dados
        
        label = ctk.CTkLabel(self.scroll_frame, text=titulo, font=("Arial", 16, "bold"), anchor="w")
        label.pack(fill="x", padx=10, pady=(20, 5))
        
        frame_opcoes = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        frame_opcoes.pack(fill="x", padx=10)
        
        opcoes = obter_opcoes_unicas(chave_dados)
        
        for opcao in opcoes:
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(frame_opcoes, text=formatar_texto(opcao), variable=var)
            chk.pack(anchor="w", pady=2, padx=10)
            
            self.checkboxes[key_storage].append({
                'valor_real': opcao,
                'variavel': var
            })

    def limpar_memoria_pydatalog(self, atividade_id):
        """
        Remove fatos antigos da memória do pyDatalog para evitar conflitos.
        """
        # Limpa ambientes
        for item in obter_opcoes_unicas('ambientes'):
            - usa_ambiente(atividade_id, item)
            
        # Limpa materiais
        for item in obter_opcoes_unicas('materiais'):
            - usa_material(atividade_id, item)
            
        # Limpa corpo
        for item in obter_opcoes_unicas('partes_do_corpo'):
            - usa_parte_do_corpo(atividade_id, item)
            
        # Limpa metas
        for item in obter_opcoes_unicas('metas_promovidas'):
            - promove_a_meta(atividade_id, item)

    def limpar_tudo(self):
        """Reseta a interface visual e a memória lógica."""
        
        # 1. Resetar Checkboxes (Interface)
        for lista_cat in self.checkboxes.values():
            for item in lista_cat:
                item['variavel'].set(False) # Desmarca

        # 2. Limpar Caixa de Texto (Interface)
        self.textbox_resultado.configure(state="normal")
        self.textbox_resultado.delete("0.0", "end")
        self.textbox_resultado.insert("0.0", "Nova consulta iniciada. Aguardando dados...")
        self.textbox_resultado.configure(state="disabled")

        # 3. Limpar Memória Lógica (pyDatalog)
        self.limpar_memoria_pydatalog('atividade_usuario')

    def analisar_resultados(self):
        atividade_atual = 'atividade_usuario'
        
        # 1. Limpeze por segurança
        self.limpar_memoria_pydatalog(atividade_atual)
        
        # 2. Coletar Inputs
        selecoes = {'ambientes': [], 'materiais': [], 'corpo': [], 'metas': []}
        algum_selecionado = False

        for categoria, lista_chk in self.checkboxes.items():
            for item in lista_chk:
                if item['variavel'].get():
                    selecoes[categoria].append(item['valor_real'])
                    algum_selecionado = True
        
        if not algum_selecionado:
            self.textbox_resultado.configure(state="normal")
            self.textbox_resultado.delete("0.0", "end")
            self.textbox_resultado.insert("0.0", ">> Selecione pelo menos uma opção para analisar.")
            self.textbox_resultado.configure(state="disabled")
            return

        # 3. Inserir fatos no PyDatalog (+)
        for item in selecoes['ambientes']: + usa_ambiente(atividade_atual, item)
        for item in selecoes['materiais']: + usa_material(atividade_atual, item)
        for item in selecoes['corpo']: + usa_parte_do_corpo(atividade_atual, item)
        for item in selecoes['metas']: + promove_a_meta(atividade_atual, item)

        # 4. Consultar
        objetivos = atinge_objetivo(atividade_atual, Y)

        # 5. Formatar Saída
        self.textbox_resultado.configure(state="normal")
        self.textbox_resultado.delete("0.0", "end")
        
        if not objetivos:
            self.textbox_resultado.insert("0.0", ">> Nenhuma classificação encontrada para essa combinação.")
        else:
            res_dict = {i+1 : set() for i in range(5)}
            for tupla in objetivos:                
                subcampo_objetivo_str = tupla[0]

                try:
                    # Divide a string em duas partes usando o '_' como separador
                    # Ex: ['subcampo1', 'objetivo19']
                    partes = subcampo_objetivo_str.split('_')
                    
                    # Parte 1: Remove a palavra 'subcampo' e converte o resto para int
                    # Ex: 'subcampo1' -> '1' -> 1
                    subcampo_str = partes[0].replace('subcampo', '')
                    sub = int(subcampo_str)

                    # Parte 2: Remove a palavra 'objetivo' e converte o resto para int
                    # Ex: 'objetivo19' -> '19' -> 19
                    objetivo_str = partes[1].replace('objetivo', '')
                    obj = int(objetivo_str)
                                        
                    if sub in res_dict: res_dict[sub].add(obj)
                except: continue

            texto_final = ""
            found = False
            for num_sub, objs in res_dict.items():
                if objs:
                    found = True
                    texto_final += f"📂 Subcampo {num_sub}\n"
                    sorted_objs = sorted(list(objs))
                    for i, o in enumerate(sorted_objs):
                        conector = "└──" if i == len(sorted_objs)-1 else "├──"
                        texto_final += f"   {conector} Objetivo {o}\n"
                    texto_final += "\n"
            
            if not found:
                texto_final = "Nenhum objetivo específico identificado."
                
            self.textbox_resultado.insert("0.0", texto_final)
            
        self.textbox_resultado.configure(state="disabled")

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()