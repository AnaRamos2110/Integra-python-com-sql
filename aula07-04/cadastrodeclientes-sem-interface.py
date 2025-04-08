import sys #Biblioteca para auxiliar no nosso sistema de cadastramento
import sqlite3 #Chamando nosso banco de dados 

conn = sqlite3.connect('C:/dados/clientes.db')  #Conectando ao banco
cursor = conn.cursor() #iniciando comandos para o banco


linha = "*" * 63

def exibir_menu(): #Função para exibir menu de cadastro
    print("Menu")
    print("1. Adicionar cliente")
    print("2.Atualizar cliente")
    print("3. Deletar cliente")
    print("4. Sair")

def adicionar_cliente(): #Função que adiciona clientes ao banco
    id = input("Digite novo ID: ") #solicitação de dados do usuário
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu e-mail: ")
    cursor.execute(f"INSERT INTO clientes values({id}, '{nome}' , '{email}') ") #Função a ser executada
    conn.commit() #Pra salvar a alteração 
    result = cursor.fetchall() #Uma nova variável para exibir resultados
    

def atualizar_cliente(): #Função que atualiza dados do cliente 
    print("Para atualização de cadastro entre com o ID do usuário. ")
    id = input("Digite o ID do usuário: ")
    nome = input("Digite/Altere seu nome: ")
    email = input("Digite/Altere seu email: ")
    cursor.execute(f"UPDATE clientes SET NOME='{nome}' WHERE id={id}") #Usando CRUD e pedindo para alterar uma linha
    conn.commit() #Pra salvar a alteração 
    result = cursor.fetchall() #Uma nova variável para exibir resultados
    print("Dados alterados com sucesso!")
    return result


def deletar_cliente(): #função que deleta dados do cliente
    print("Para deletar o cadastro, é necessário o ID do usuário.")
    id = input("Digite o ID do usuário: ")
    cursor = conn.cursor() #Solicitando um comando novo
    cursor.execute(f"DELETE FROM clientes WHERE id={id}") #Usando CRUD e pedindo para deletar um cadastro
    conn.commit() #Pra salvar a alteração
    result = cursor.fetchall() #Uma nova variável para exibir resultados


  

def main():
    while True:
        exibir_menu()

        opcao = input("Selecione uma opção do menu.")

        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            atualizar_cliente()
        elif opcao == "3":
            deletar_cliente()
        elif opcao == "4":
            sys.exit()
        else:
            print("Opç~qao inválida. Tente novamente.")
            
            
            



if __name__ == "__main__":
    main()
    
    