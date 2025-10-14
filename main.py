import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd

# Lista de alunos em memória
alunos = []

# Função para atualizar a tabela
def atualizar_tabela():
    for i in tree.get_children():
        tree.delete(i)
    for aluno in alunos:
        tree.insert("", "end", values=(aluno["Nome"], aluno["Idade"], aluno["Curso"], aluno["Nota Final"]))

# Função para cadastrar aluno
def cadastrar():
    nome = entry_nome.get()
    idade = entry_idade.get()
    curso = entry_curso.get()
    nota = entry_nota.get()

    if not nome or not idade or not curso or not nota:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
        nota = float(nota)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser número inteiro e nota um número decimal.")
        return

    alunos.append({"Nome": nome, "Idade": idade, "Curso": curso, "Nota Final": nota})
    atualizar_tabela()

    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_curso.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Função para filtrar alunos com nota acima da média
def filtrar():
    try:
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma média válida!")
        return

    filtrados = [a for a in alunos if a["Nota Final"] >= media]

    for i in tree.get_children():
        tree.delete(i)
    for aluno in filtrados:
        tree.insert("", "end", values=(aluno["Nome"], aluno["Idade"], aluno["Curso"], aluno["Nota Final"]))

# Função para salvar CSV
def salvar_csv():
    if not alunos:
        messagebox.showwarning("Atenção", "Nenhum aluno cadastrado!")
        return

    caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])
    if caminho:
        df = pd.DataFrame(alunos)
        df.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")

# Função para carregar CSV
def carregar_csv():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivo CSV", "*.csv")])
    if caminho:
        try:
            df = pd.read_csv(caminho)
            alunos.clear()
            for _, row in df.iterrows():
                alunos.append({
                    "Nome": row["Nome"],
                    "Idade": int(row["Idade"]),
                    "Curso": row["Curso"],
                    "Nota Final": float(row["Nota Final"])
                })
            atualizar_tabela()
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar arquivo:\n{e}")

# Função para exportar relatório filtrado
def exportar_filtrado():
    try:
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma média válida para exportar.")
        return

    filtrados = [a for a in alunos if a["Nota Final"] >= media]

    if not filtrados:
        messagebox.showwarning("Aviso", "Nenhum aluno com nota acima da média informada.")
        return

    caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])
    if caminho:
        df = pd.DataFrame(filtrados)
        df.to_csv(caminho, index=False)
        messagebox.showinfo("Sucesso", "Relatório exportado com sucesso!")

# =========================
# INTERFACE TKINTER
# =========================
janela = tk.Tk()
janela.title("Sistema de Cadastro de Alunos")
janela.geometry("750x500")
janela.configure(bg="#f2f2f2")

# Frame de cadastro
frame_cadastro = tk.LabelFrame(janela, text="Cadastrar Aluno", padx=10, pady=10, bg="#f2f2f2")
frame_cadastro.pack(fill="x", padx=10, pady=10)

tk.Label(frame_cadastro, text="Nome:", bg="#f2f2f2").grid(row=0, column=0)
entry_nome = tk.Entry(frame_cadastro)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_cadastro, text="Idade:", bg="#f2f2f2").grid(row=0, column=2)
entry_idade = tk.Entry(frame_cadastro)
entry_idade.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_cadastro, text="Curso:", bg="#f2f2f2").grid(row=1, column=0)
entry_curso = tk.Entry(frame_cadastro)
entry_curso.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_cadastro, text="Nota Final:", bg="#f2f2f2").grid(row=1, column=2)
entry_nota = tk.Entry(frame_cadastro)
entry_nota.grid(row=1, column=3, padx=5, pady=5)

tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar, bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=4, pady=10)

# Frame da tabela
frame_tabela = tk.Frame(janela, bg="#f2f2f2")
frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)

colunas = ("Nome", "Idade", "Curso", "Nota Final")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")
for col in colunas:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)

# Frame de filtros e ações
frame_filtro = tk.LabelFrame(janela, text="Filtrar e Relatórios", padx=10, pady=10, bg="#f2f2f2")
frame_filtro.pack(fill="x", padx=10, pady=10)

tk.Label(frame_filtro, text="Filtrar alunos com nota acima de:", bg="#f2f2f2").grid(row=0, column=0)
entry_media = tk.Entry(frame_filtro)
entry_media.grid(row=0, column=1, padx=5)
tk.Button(frame_filtro, text="Filtrar", command=filtrar, bg="#2196F3", fg="white").grid(row=0, column=2, padx=5)
tk.Button(frame_filtro, text="Mostrar Todos", command=atualizar_tabela, bg="#9E9E9E", fg="white").grid(row=0, column=3, padx=5)
tk.Button(frame_filtro, text="Salvar CSV", command=salvar_csv, bg="#FF9800", fg="white").grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_filtro, text="Carregar CSV", command=carregar_csv, bg="#607D8B", fg="white").grid(row=1, column=1, padx=5, pady=5)
tk.Button(frame_filtro, text="Exportar Relatório", command=exportar_filtrado, bg="#673AB7", fg="white").grid(row=1, column=2, padx=5, pady=5)

janela.mainloop()