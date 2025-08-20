import tkinter as tk

from tkinter import messagebox
from inserir_funcionario import inserir_funcionario

def cadastrar_funcionario():
    nome = entry_nome.get()
    idade = entry_idade.get()
    setor = entry_setor.get()
    

    if nome == "" or idade == "" or setor == "" :
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return None

    try:
        inserir_funcionario(nome, idade, setor)
        messagebox.showinfo("Sucesso", "O registro do funcionário foi cadastrado com sucesso!")
        entry_idade.delete(0, tk.END)
        entry_setor.delete(0, tk.END)
        entry_nome.focus_set()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Cadastro de Funcionários")
janela.geometry("500x350")
janela.resizable(True, True)

# Campos
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Idade:").pack(pady=5)
entry_idade = tk.Entry(janela, width=40)
entry_idade.pack()

tk.Label(janela, text="Setor:").pack(pady=5)
entry_setor = tk.Entry(janela, width=40)
entry_setor.pack()


tk.Button(janela, text="Cadastrar", command=cadastrar_funcionario).pack(pady=15)

janela.mainloop()