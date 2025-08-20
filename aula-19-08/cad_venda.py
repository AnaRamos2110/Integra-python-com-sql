import tkinter as tk

from tkinter import messagebox
from inserir_venda import inserir_venda

def cadastrar_venda():
    descricao = entry_descricao.get()
    quantidade = entry_quantidade.get()
    valor_unitario = entry_valor_unitario.get()
    valor_total = entry_valor_total.get()
    data_venda = entry_data_venda.get()

    if descricao == "" or quantidade == "" or valor_unitario == "" or valor_total == "" or data_venda == "":
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return None

    try:
        inserir_venda(descricao, quantidade, valor_unitario, valor_total, data_venda)
        messagebox.showinfo("Sucesso", "O usuário foi cadastrado!")
        entry_descricao.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_valor_unitario.delete(0, tk.END)
        entry_valor_total.delete(0, tk.END)
        entry_data_venda.delete(0, tk.END)
        entry_descricao.focus_set()
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível cadastrar: {e}")

# Janela
janela = tk.Tk()
janela.title("Bem vindo! ")
janela.geometry("500x350")
janela.resizable(True, True)

# Campos

tk.Label(janela, text="Descrição:").pack(pady=5)
entry_descricao = tk.Entry(janela, width=40)
entry_descricao.pack()

tk.Label(janela, text="Quantidade:").pack(pady=5)
entry_quantidade = tk.Entry(janela, width=40)
entry_quantidade.pack()

tk.Label(janela, text="Valor unitario:").pack(pady=5)
entry_valor_unitario = tk.Entry(janela, width=40)
entry_valor_unitario.pack()

tk.Label(janela, text="Valor total:").pack(pady=5)
entry_valor_total = tk.Entry(janela, width=40)
entry_valor_total.pack()


tk.Label(janela, text="Data venda:").pack(pady=5)
entry_data_venda = tk.Entry(janela, width=40)
entry_data_venda.pack()



tk.Button(janela, text="Cadastrar", command=cadastrar_venda).pack(pady=15)

janela.mainloop()