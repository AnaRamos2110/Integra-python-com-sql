from conexao import conectar

def inserir_produto(descricao, valor):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (descricao, valor) VALUES (%s, %s)"
        valores = (descricao,valor)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()