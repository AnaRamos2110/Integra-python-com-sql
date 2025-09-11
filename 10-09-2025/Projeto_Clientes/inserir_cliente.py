from conexao import criar_conexao

def inserir_cliente(nome, email, telefone):
    try:
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)",
            (nome, email, telefone)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao inserir cliente:", e)
        return False