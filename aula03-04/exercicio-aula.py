import sqlite3
conn = sqlite3.connect('C:/dados/clientes.db') #Conectando ao meu banco


id_cliente = input("Insira o ID a ser deletado: ") #Pedindo os dados ao usuário
print(f"O ID: {id_cliente} foi deletado com sucesso ") #Solicitando o id a ser deletado


cursor = conn.cursor() #Solicitando um comando novo
cursor.execute(f"DELETE FROM clientes WHERE id={id_cliente}") #Usando CRUD e pedindo para deletar uma linha 
conn.commit() #Pra salvar a alteração

result = cursor.fetchall() #Uma nova variável para mudar os resultados

for x in result: #Loop em FOR para resultados
    print(x)


cursor.execute("SELECT * FROM clientes")
result = cursor.fetchall() #Para exibir novo resultado

for x in result:
    print(x)