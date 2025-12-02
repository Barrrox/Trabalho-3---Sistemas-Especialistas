# Sistema Especialista - Educação Infantil (BNCC)

**Disciplina:** Inteligência Artificial - Trabalho 3 (Sistemas Especialistas)

### Autores
* **Nome do Autor 1** ([@usuario_github](https://github.com/usuario))
* **Nome do Autor 2** ([@usuario_github](https://github.com/usuario))
* **Nome do Autor 3** ([@usuario_github](https://github.com/usuario))
* **Nome do Autor 4** ([@usuario_github](https://github.com/usuario))

---

## Sobre o Projeto

Este projeto é um Sistema Especialista desenvolvido em Python 3.14 para classificar atividades pedagógicas de acordo com a Base Nacional Comum Curricular (BNCC).

O sistema utiliza um motor de inferência lógica para analisar entradas (ambiente, materiais, partes do corpo e metas) e determinar quais Objetivos de Aprendizagem e Desenvolvimento são contemplados pela atividade proposta.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **Interface:** CustomTkinter
* **Motor de Inferência:** pyDatalog
* **Build:** PyInstaller

## Estrutura de Arquivos

```text
raiz/
│
├── base_de_conhecimento/      # Regras lógicas, fatos e subcampos
│   ├── subcampos/             # Regras específicas por subcampo BNCC
│   ├── config_dados.py        # Dados de entrada (Vocabulário)
│   └── variaveis_e_predicados.py
│
├── interface/
│   └── interface.py           # Interface gráfica do usuário
│
├── main.py                    # Versão CLI (Linha de Comando)
├── SistemaEspecialista.spec   # Arquivo de configuração de build
└── README.md
```

## Instalação e Execução

### 1. Instalar Dependências
No terminal, na raiz do projeto:

```bash
pip install pyDatalog customtkinter pyinstaller
```

### 2. Executar a Interface
Para iniciar o sistema:

```bash
python interface/interface.py
```

## Gerar Executável (.exe)

Para compilar o projeto em um arquivo executável único para Windows:

1. Abra o terminal na **raiz do projeto**.
2. Comando que utilizei:

```bash
pyinstaller --noconfirm --onefile --windowed --name "SistemaEspecialista" --add-data "base_de_conhecimento;base_de_conhecimento" --hidden-import "pyDatalog" interface/interface.py
```
O arquivo final ```SistemaEspecialista.exe``` será gerado na pasta ```dist/```.