import tkinter as tk
from tkinter import messagebox
from inserir_produto import inserir_produto  # função separada no outro arquivo.
from tela_listar_produtos import exibir_produtos  # importa a tela de listagem

def abrir_tela_produto(master=None):
    def cadastrar_produto():
        descricao = entry_descricao.get()
        valor = entry_valor.get()

        if not (descricao and valor):
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        inserir_produto(descricao, valor)  # função no outro arquivo

        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        limpar_campos()
        entry_descricao.focus()

    def limpar_campos():
        entry_descricao.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_descricao.focus()

    def foco_valor(event): #Para digitar direto sem precisar clicar sempre
        entry_valor.focus()

    def salvar_enter(event):
        cadastrar_produto()

    # Criando janela
    
    janela = tk.Toplevel(master)  # filha da principal
    janela.title("Cadastro de Produtos")
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

    # Labels e Entrys
    tk.Label(janela, text="Descrição:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_descricao = tk.Entry(janela, width=30)
    entry_descricao.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(janela, text="Valor:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_valor = tk.Entry(janela, width=30)
    entry_valor.grid(row=1, column=1, padx=10, pady=10)

    # Botões #Salva os produtos
    btn_salvar = tk.Button(janela, text="Cadastrar", width=12, command=cadastrar_produto)
    btn_salvar.grid(row=2, column=0, padx=10, pady=15)

    #Limpa os campos
    btn_limpar = tk.Button(janela, text="Limpar", width=12, command=limpar_campos)
    btn_limpar.grid(row=2, column=1, padx=10, pady=15, sticky="e")

    # NOVO BOTÃO (Exibe os produtos)
    btn_listar = tk.Button(janela, text="Exibir Produtos", width=20, command=exibir_produtos)
    btn_listar.grid(row=3, column=0, columnspan=2, pady=10)

    # Eventos de tecla Enter
    entry_descricao.bind("<Return>", foco_valor)   # Enter no campo nome → vai para senha
    entry_valor.bind("<Return>", salvar_enter)  # Enter no campo senha → salva

    entry_descricao.focus()
    
    return janela