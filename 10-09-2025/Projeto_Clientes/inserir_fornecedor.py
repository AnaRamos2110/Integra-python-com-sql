from fornecedor_conexao import criar_conexao_fornecedor

def inserir_fornecedor(nome, email, telefone):
    try:
        conn = criar_conexao_fornecedor()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO fornecedores(nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        return False