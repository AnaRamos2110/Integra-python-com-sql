import tkinter as tk
from tkinter import messagebox
from inserir_produto import listar_produto, excluir_produto

def exibir_produtos():
    produtos = listar_produto()  # pega os produtos do banco

    if not produtos:
        messagebox.showinfo("Produtos", "Nenhum produto cadastrado.")
        return

    # Cria janela filha
    janela_lista = tk.Toplevel()
    janela_lista.title("Produtos Cadastrados")
    janela_lista.resizable(False, False)

    # Centraliza
    window_width = 450
    window_height = 350
    screen_width = janela_lista.winfo_screenwidth()
    screen_height = janela_lista.winfo_screenheight()
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))
    janela_lista.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Janela modal
    janela_lista.transient(janela_lista.master)
    janela_lista.grab_set()

    tk.Label(janela_lista, text="Produtos cadastrados:", font=("Arial", 12, "bold")).pack(pady=10)

    # Listbox
    listbox = tk.Listbox(janela_lista, width=60, height=10)
    listbox.pack(padx=10, pady=10, fill="both", expand=True)

    for descricao, valor in produtos:
        listbox.insert(tk.END, f"{descricao} | {valor}")

    # Função para atualizar listbox
    def atualizar_lista():
        listbox.delete(0, tk.END)
        for d, v in listar_produto():
            listbox.insert(tk.END, f"{d} | {v}")

    # Função para excluir produto
    def excluir():
        selecionado = listbox.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir.")
            return

        produto_texto = listbox.get(selecionado[0])
        descricao = produto_texto.split(" | ")[0]

        confirmar = messagebox.askyesno("Confirmação", f"Deseja realmente excluir o produto '{descricao}'?")
        if confirmar:
            excluir_produto(descricao)
            messagebox.showinfo("Sucesso", f"Produto '{descricao}' excluído com sucesso.")
            atualizar_lista()

    # Botões
    btn_excluir = tk.Button(janela_lista, text="Excluir Produto", width=20, command=excluir)
    btn_excluir.pack(pady=5)

    def fechar():
        janela_lista.grab_release()
        janela_lista.destroy()

    tk.Button(janela_lista, text="Fechar", width=12, command=fechar).pack(pady=5)

    # Bloqueia fechar pelo X
    janela_lista.protocol("WM_DELETE_WINDOW", lambda: None)
