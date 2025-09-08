import tkinter as tk
from tkinter import messagebox

# Funções para abrir as telas


def abrir_clientes():
    import cad_cliente

def abrir_funcionarios():
    import cad_funcionario

def abrir_produtos():
    import cad_produto

def abrir_usuarios():
    import cad_usuario

def abrir_vendas():
    import cad_venda

def list_users():
    import tela_listar_usuarios

def list_products():
    import tela_listar_produtos

def sair():
    if messagebox.askyesno("Sair", "Deseja encerrar o sistema?"):
        root.destroy()

# Criando a janela principal
root = tk.Tk()
root.title("Sistema Principal")

# Definindo tamanho e centralizando na tela
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

# Criando um frame central para os botões
frame = tk.Frame(root)
frame.pack(expand=True)

# Criando os botões
btn_clientes = tk.Button(frame, text="Clientes", width=20, command=abrir_clientes)
btn_funcionarios = tk.Button(frame, text="Funcionários", width=20, command=abrir_funcionarios)
btn_produtos = tk.Button(frame, text="Produtos", width=20, command=abrir_produtos)
btn_usuarios = tk.Button(frame, text="Usuários", width=20, command=abrir_usuarios)
btn_vendas = tk.Button(frame, text="Vendas", width=20, command=abrir_vendas)
btn_sair = tk.Button(frame, text="Encerrar Sistema", width=20, command=sair, bg="turquoise", fg="black")


# Posicionando os botões com grid (linha, coluna)
btn_clientes.grid(row=0, column=0, pady=5)
btn_funcionarios.grid(row=1, column=0, pady=5)
btn_produtos.grid(row=2, column=0, pady=5)
btn_usuarios.grid(row=3, column=0, pady=5)
btn_vendas.grid(row=4, column=0, pady=5)
btn_sair.grid(row=5, column=0, pady=15)

root.mainloop()