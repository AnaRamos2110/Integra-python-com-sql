from conexao import conectar

def inserir_usuario(nome, senha):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
        valores = (nome, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()