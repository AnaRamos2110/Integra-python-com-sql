import sqlite3 #chamando a biblioteca sqlite pro código
conn = sqlite3.connect('C:/dados/clientes.db') #Chamando a função connect para conectar no database
 
cursor = conn.cursor() #A função cursor obedece um comando

id_cliente = input("Insira um ID de cliente: ") #Pedindo os dados ao usuário
print(f"Valor digitado : {id_cliente} ")

nome_cliente = input("Insira o nome do cliente: ")
print(f"O nome inserido foi : {nome_cliente} ")

email_cliente = input("Por favor, digite seu email ")
print(f"O email selecionado foi : {email_cliente} ")

cursor.execute(f"INSERT INTO clientes VALUES ({id_cliente}, '{nome_cliente}', '{email_cliente}')") #Chamando os dados do cliente
conn.commit() #Commitando no banco

result = cursor.fetchall() #Pedindo ao fetchall para exibir resultados

for x in result:
    print(x)  #Iteração para exibir os dados

cursor.execute("SELECT * FROM clientes") #Nova consulta 
result = cursor.fetchall()

for x in result: #Nova iteração para exibir os dados alterados
    print(x)