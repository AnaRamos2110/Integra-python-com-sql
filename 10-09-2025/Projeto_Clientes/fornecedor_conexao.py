import mysql.connector

def criar_conexao_fornecedor():
    conexao = mysql.connector.connect(
        host="localhost",      # endereço do servidor MySQL
        user="root",           # usuário do MySQL
        password="",  # senha do MySQL
        database="fornecedores"    # nome do banco de dados
    )
    return conexao