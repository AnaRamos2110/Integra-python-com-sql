import tkinter as tk
from tkinter import messagebox
from inserir_venda import inserir_usuario  # função separada no outro arquivo.
from tela_listar_vendas import exibir_vendas # importa a tela de listagem

def abrir_tela_vendas(master=None):
    def salvar_vendas():
        id_vendas = entry_id_vendas.get()
        descricao = entry_descricao.get()
        quantidade= entry_quantidade.get()
        valor_unitario = entry_valor_unitario.get()
        valor_total = entry_valor_total.get()

        if not (id_vendas and descricao and quantidade and valor_unitario and valor_total):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        inserir_usuario(id_vendas, descricao, quantidade, valor_unitario, valor_total)  # função no outro arquivo

        messagebox.showinfo("Sucesso", "Sua venda foi cadastrada!")
        limpar_campos()
        entry_id_vendas.focus() #O cursor volta para o campo do Id de vendas

    def limpar_campos(): #id_vendas, descricao, quantidade, valor_unitario, valor_total 
        entry_id_vendas.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_valor_unitario.delete(0, tk.END)
        entry_valor_total.delete(0, tk.END)
        entry_valor_total.focus()


    def foco_senha(event):
        entry_valor_total.focus()

    def salvar_enter(event):
        salvar_vendas()

    # Criando janela
    #janela = tk.Tk()
    janela = tk.Toplevel(master)  # filha da principal
    janela.title("Registro de vendas")
    janela.geometry("320x200")
    janela.resizable(False, False)

    # Centralizar a janela
    window_width = 400
    window_height = 300
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Faz a janela ficar sempre acima da principal e modal
    janela.transient(janela.master)  # depende da janela principal
    janela.grab_set()  # impede interação com a principal até fechar

   # Id da venda
tk.Label(janela, text="Id da venda:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_id_vendas = tk.Entry(janela, width=30)
entry_id_vendas.grid(row=0, column=1, padx=10, pady=10)

# Descrição
tk.Label(janela, text="Descrição:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_descricao = tk.Entry(janela, width=30)
entry_descricao.grid(row=1, column=1, padx=10, pady=10)

# Quantidade
tk.Label(janela, text="Quantidade:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_quantidade = tk.Entry(janela, width=30)
entry_quantidade.grid(row=2, column=1, padx=10, pady=10)

# Valor por unidade
tk.Label(janela, text="Valor por unidade:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
entry_valor_unitario = tk.Entry(janela, width=30)
entry_valor_unitario.grid(row=3, column=1, padx=10, pady=10)

# Valor total
tk.Label(janela, text="Valor total da compra:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
entry_valor_total = tk.Entry(janela, width=30)
entry_valor_total.grid(row=4, column=1, padx=10, pady=10)
)

    # Botões
    btn_salvar = tk.Button(janela, text="Salvar", width=12, command=salvar_vendas)
    btn_salvar.grid(row=2, column=0, padx=10, pady=15)

    btn_limpar = tk.Button(janela, text="Limpar", width=12, command=limpar_campos)
    btn_limpar.grid(row=2, column=1, padx=10, pady=15, sticky="e")

    # NOVO BOTÃO (sem função ainda)
    btn_listar = tk.Button(janela, text="Exibir Usuários", width=20, command=exibir_vendas)
    btn_listar.grid(row=3, column=0, columnspan=2, pady=10)

    # Eventos de tecla Enter
    entry_id_vendas.bind("<Return>", foco_descricao)   # Enter no campo nome → vai para senha
    entry_descricao.bind("<Return>", foco_quantidade)
    entry_quantidade.bind("<Return>", foco_quantidade)
    entry_valor_unitario("<Return>", foco_quantidade)
    entry_valor_total.bind("<Return>", salvar_enter)

    entry_descricao.focus()
    r
return janela