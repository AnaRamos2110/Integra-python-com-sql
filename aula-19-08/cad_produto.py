import tkinter as tk

from tkinter import messagebox
from inserir_produto import inserir_produto
def cadastrar_produto():
    descricao = entry_descricao.get()
    valor = entry_valor.get()
    

    if descricao == "" or valor == "" :
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return None

    try:
        inserir_produto(descricao, valor)
        messagebox.showinfo("Sucesso", "O registro do funcionário foi cadastrado com sucesso!")
        entry_descricao.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_descricao.focus_set()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Cadastro de Produtos")
janela.geometry("500x350")
janela.resizable(True, True)

# Campos
tk.Label(janela, text="Descrição:").pack(pady=5)
entry_descricao = tk.Entry(janela, width=40)
entry_descricao.pack()

tk.Label(janela, text="Valor:").pack(pady=5)
entry_valor = tk.Entry(janela, width=40)
entry_valor.pack()


tk.Button(janela, text="Cadastrar", command=cadastrar_produto).pack(pady=15)

janela.mainloop()