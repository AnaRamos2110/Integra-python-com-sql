from tkinter import *#O QUE É TKinter? Tkinter é uma biblioteca da linguagem Python que acompanha a instalação padrão e permite desenvolver interfaces gráficas.
from tkinter import * 
import sqlite3

#Criando o frame
root = Tk() #Para criar a janela principal
root.title('Inserir cliente') #titulo da janela
root.geometry("700x400") #Dimensão da janela
 
conn = sqlite3.connect('C:/dados/clientes.db')
c = conn.cursor()

def submit():
    c.execute(f"INSERT INTO clientes VALUES ({f_id.get()}, '{f_name.get()}', '{f_email.get()}') ")
    conn.commit()

    f_id.delete(0, END) #REMOVE O CONTEÚDO DO CAMPO INICIANDO NA POSIÇÃO 0 ATÉ A ÚLTIMA POSIÇÃO 'END'
    f_name.delete(0, END) #REMOVE O CONTEÚDO DO CAMPO INICIANDO NA POSIÇÃO 0 ATÉ A ÚLTIMA POSIÇÃO 'END'
    f_email.delete(0, END) #REMOVE O CONTEÚDO DO CAMPO INICIANDO NA POSIÇÃO 0 ATÉ A ÚLTIMA POSIÇÃO 'END'
    f_id.focus() #POSICIONA O CURSOR NO CAMPO DESEJADO 


def query():
    c.execute("select * from clientes")
    records = c.fetchall()

    print_records = ''
    print_records += f"ID | Nome | Email \n"

    for record in records:
        print_records += f"{record[0]} | {record[1]} | {record[2]} \n"
#Também tem a opção de concatenação usando :
#       print_records += str(record[0]) + " | " + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0)


#Criando interface textual dentro do meu quadro(frame) para entender melhor, 
#Imagine como se fosse uma planilha em branco aonde você tem que atribuir aonde seus textos e os dados a serem preenchidos e mostrados serão posicionados!

f_id = Entry(root, width=30)
f_id.grid(row=0, column=1) #Estabelecendo tamanho e posicionamento do texto dentro do meu quadro


f_name = Entry(root, width=30) #Estabelecendo tamanho e posicionamento para atributo de texto
f_name.grid(row=1, column=1)


f_email = Entry(root, width=30) #Estabelecendo tamanho e posicionamento para atributo de texto
f_email.grid(row=2, column=1)

f_id_label =Label(root, text="ID Cliente") #Chamando valor de string para os atributos e os posicionando na tabela dentro do meu quadro
f_id_label.grid(row=0, column=0)

f_nome_label =Label(root, text="Nome Cliente") #Chamando valor de string para os atributos e os posicionando na tabela dentro do meu quadro
f_nome_label.grid(row=1, column=0)

f_email_label =Label(root, text="Email Cliente") #Chamando valor de string para os atributos e os posicionando na tabela dentro do meu quadro
f_email_label.grid(row=2, column=0)

submit_btn = Button(root, text="Adicionar cliente",command=submit)
submit_btn.grid(row=6, column=1)

query_btn = Button(root, text="Mostrar clientes",command=query)
query_btn.grid(row=7, column=1)

exit_button = Button(root, text="Sair",command=root.destroy)
exit_button.grid(row=7, column=3)

root.mainloop() #Para executar a aplicação

conn.close() #Fecha a conexão com o banco de dados, neste caso o SQLite
