from conexao import conectar

def inserir_venda(descricao, quantidade, valor_unitario, valor_total, data_venda):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO vendas (descricao, quantidade, valor_unitario, valor_total, data_venda) VALUES (%s, %s, %s, %s, %s)"
        valores = (descricao, quantidade, valor_unitario, valor_total, data_venda)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()