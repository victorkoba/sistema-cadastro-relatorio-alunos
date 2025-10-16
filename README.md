# Sistema de Cadastro de Alunos (Tkinter + Pandas)

Este projeto é uma aplicação desktop desenvolvida em **Python** utilizando a biblioteca **Tkinter** para interface gráfica e **Pandas** para manipulação e exportação de dados.  
O sistema permite cadastrar, visualizar, filtrar, salvar e carregar informações de alunos de forma simples e interativa.

---

## Funcionalidades

### Cadastrar Alunos  
Permite inserir nome, idade, curso e nota final dos alunos.

### Exibir Tabela  
Mostra todos os alunos cadastrados em uma tabela interativa (`Treeview`).

### Filtrar Alunos  
Filtra os alunos com **nota acima de uma média definida** pelo usuário.

### Salvar Dados em CSV  
Exporta todos os alunos cadastrados para um arquivo `.csv`.

### Carregar Dados de CSV  
Importa uma planilha `.csv` existente e exibe os alunos na tabela.

### Exportar Relatório Filtrado  
Cria um relatório `.csv` apenas com os alunos que atingiram a média mínima informada.

---

## Interface Gráfica

A interface foi construída com **Tkinter**, apresentando três seções principais:

1. **Cadastro de Alunos**  
   Campos para preencher Nome, Idade, Curso e Nota Final.

2. **Tabela de Alunos**  
   Exibe todos os cadastros feitos na sessão.

3. **Filtros e Relatórios**  
   Permite filtrar por média, salvar, carregar e exportar relatórios.

---

## Estrutura do Código

- `alunos = []` → Lista usada para armazenar os dados em memória.  
- `cadastrar()` → Adiciona novo aluno à lista e atualiza a tabela.  
- `atualizar_tabela()` → Atualiza a visualização da tabela com os dados atuais.  
- `filtrar()` → Exibe apenas os alunos com nota acima da média digitada.  
- `salvar_csv()` → Salva todos os cadastros em um arquivo CSV.  
- `carregar_csv()` → Carrega os dados de um arquivo CSV.  
- `exportar_filtrado()` → Exporta apenas os alunos filtrados por média.

---

## Como Executar o Projeto

### Pré-requisitos

Você precisa ter o **Python 3.8+** instalado em seu computador.  
Além disso, instale as dependências com o comando:

```bash
pip install pandas
```

### Executar o Programa

Baixe o arquivo .py e execute no terminal:
```bash
python sistema_cadastro_alunos.py
```

### Estrutura de Arquivos

```bash
sistema-cadastro-alunos
├── sistema_cadastro_alunos.py   # Código principal da aplicação
├── alunos.csv                   # (opcional) Arquivo de exemplo com dados
└── README.md                    # Documentação do projeto
```

### Bibliotecas Utilizadas
```bash
| Biblioteca     | Função                                              |
| -------------- | --------------------------------------------------- |
| **tkinter**    | Interface gráfica (janela, botões, campos e tabela) |
| **pandas**     | Manipulação e exportação de dados em CSV            |
| **messagebox** | Exibição de alertas e mensagens                     |
| **filedialog** | Seleção de arquivos no sistema operacional          |
```
