import tkinter as tk
from tkinter import messagebox
import flask_requests
from inserir_fornecedor import inserir_fornecedor
# ---------------------------
# Função para salvar cliente
# ---------------------------
def salvar_fornecedor():
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    if not (nome and email and telefone):
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    # Inserir no banco MySQL
    if not inserir_fornecedor(nome, email, telefone):
        messagebox.showerror("Erro", "Falha ao salvar no banco de dados.")
        return

    # Enviar para API web
    try:
        flask_requests.post(
            "http://127.0.0.1:5000/clientes",
            json={"nome": nome, "email": email, "telefone": telefone}
        )
    except:
        messagebox.showwarning(
            "Aviso",
            "API web não encontrada. Fornecedor salvo apenas no MySQL."
        )

    messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")

    # Limpar os campos
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

# ---------------------------
# Janela principal
# ---------------------------
root = tk.Tk()
root.title("Cadastro de Fornecedor")
root.resizable(False, False)

# Centralizar a tela
largura, altura = 350, 220
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

# ---------------------------
# Layout
# ---------------------------
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Nome:", anchor="w").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame, width=30)
entry_nome.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Email:", anchor="w").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Telefone:", anchor="w").grid(row=2, column=0, sticky="w")
entry_telefone = tk.Entry(frame, width=30)
entry_telefone.grid(row=2, column=1, pady=5)

btn_salvar = tk.Button(frame, text="Salvar Fornecedor", width=20, command=salvar_fornecedor)
btn_salvar.grid(row=3, column=0, columnspan=2, pady=15)

# ---------------------------
# Rodar aplicação
# ---------------------------
root.mainloop()