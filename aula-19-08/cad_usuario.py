import tkinter as tk

from tkinter import messagebox
from inserir_usuario import inserir_usuario
def cadastrar_usuario():
    nome = entry_nome.get()
    senha = entry_senha.get()
    

    if nome == "" or senha == "" :
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return None

    try:
        inserir_usuario(nome, senha)
        messagebox.showinfo("Sucesso", "O usuário foi cadastrado!")
        entry_nome.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
        entry_nome.focus_set()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Cadastro de usuário")
janela.geometry("500x350")
janela.resizable(True, True)

# Campos
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Senha:").pack(pady=5)
entry_senha = tk.Entry(janela, width=40)
entry_senha.pack()


tk.Button(janela, text="Cadastrar", command=cadastrar_usuario).pack(pady=15)

janela.mainloop()