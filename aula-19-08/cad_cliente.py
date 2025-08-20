import tkinter as tk

from tkinter import messagebox
from inserir_cliente import inserir_cliente

def cadastrar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()

    if nome == "" or email == "" or cidade == "" or estado == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    try:
        inserir_cliente(nome, email, cidade, estado)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
        entry_estado.delete(0, tk.END)
        entry_nome.focus_set()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("350x250")
janela.resizable(False, False)

# Campos
tk.Label(janela, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(janela, width=40)
entry_nome.pack()

tk.Label(janela, text="Email:").pack(pady=5)
entry_email = tk.Entry(janela, width=40)
entry_email.pack()

tk.Label(janela, text="Cidade:").pack(pady=5)
entry_cidade = tk.Entry(janela, width=40)
entry_cidade.pack()

tk.Label(janela, text="Estado:").pack(pady=5)
entry_estado = tk.Entry(janela, width=5)
entry_estado.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar_cliente).pack(pady=15)

janela.mainloop()