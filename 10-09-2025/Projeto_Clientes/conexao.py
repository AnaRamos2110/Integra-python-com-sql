import mysql.connector

def criar_conexao():
    conexao = mysql.connector.connect(
        host="localhost",      # endereço do servidor MySQL
        user="root",           # usuário do MySQL
        password="",  # senha do MySQL
        database="clientes"    # nome do banco de dados
    )
    return conexao
