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
pip install pyDatalog customtkinter
```

Para criar um arquivo executável do sistema, baixe o pyinstaller:

```bash
pip install pyinstaller
```

### 2. Executar a Interface

*ATENÇÃO: É necessário estar na raiz do projeto para executá-lo*

Há 3 formas de utilizar esse sistema. Primeiro, você pode executar a main para obter uma interface CLI. Essa interface foi utiliza inicialmente para testes e provavelmente estará desatualizada em relação à interface iterativa. Utilize o comando:

```bash
python main.py
```

Você pode executar o código da interface com comando:

```bash
python interface/interface.py
```

E você também pode gerar um executável (que no fim das contas, vai executar interface.py também)

## Gerar Executável (.exe)

Para compilar o projeto em um arquivo executável único para Windows:

1. Abra o terminal na **raiz do projeto**.
2. Digite o comando para executar com os parâmetros que utilizamos:

```bash
pyinstaller SistemaEspecialista.spec
```

Ou pode mudar com o comando completo:

```bash
pyinstaller --noconfirm --onefile --windowed --name "SistemaEspecialista" --add-data "base_de_conhecimento;base_de_conhecimento" --hidden-import "pyDatalog" interface/interface.py
```

O arquivo final ```SistemaEspecialista.exe``` será gerado na pasta ```dist/```.