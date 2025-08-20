import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",  #Seu usuário Mysql
            password="", #A sua senha
            database="loja" #Seu banco de dados que se chama loja
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"Erro na conexão: {erro}")
        return None
    
