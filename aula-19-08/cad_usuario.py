import tkinter as tk
from tkinter import messagebox
from inserir_usuario import inserir_usuario  # função separada no outro arquivo.
from tela_listar_usuarios import exibir_usuarios  # importa a tela de listagem


def salvar_usuario():
    nome = entry_nome.get()
    senha = entry_senha.get()

    if not (nome and senha):
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return
    
    inserir_usuario(nome, senha)  # função no outro arquivo

    messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    limpar_campos()
    entry_nome.focus()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    entry_nome.focus()

def foco_senha(event):
    entry_senha.focus()

def salvar_enter(event):
    salvar_usuario()

# Criando janela
#janela = tk.Tk()
janela = tk.Toplevel()  # filha da principal
janela.title("Cadastro de Usuários")
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
tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_senha = tk.Entry(janela, width=30, show="*")
entry_senha.grid(row=1, column=1, padx=10, pady=10)

# Botões
btn_salvar = tk.Button(janela, text="Salvar", width=12, command=salvar_usuario)
btn_salvar.grid(row=2, column=0, padx=10, pady=15)

btn_limpar = tk.Button(janela, text="Limpar", width=12, command=limpar_campos)
btn_limpar.grid(row=2, column=1, padx=10, pady=15, sticky="e")

# NOVO BOTÃO (sem função ainda)
btn_listar = tk.Button(janela, text="Exibir Usuários", width=20, command=exibir_usuarios)
btn_listar.grid(row=3, column=0, columnspan=2, pady=10)

# Eventos de tecla Enter
entry_nome.bind("<Return>", foco_senha)   # Enter no campo nome → vai para senha
entry_senha.bind("<Return>", salvar_enter)  # Enter no campo senha → salva

entry_nome.focus()
janela.mainloop()