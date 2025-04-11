#Criando um checkbox para selecionar Jogadores 
import tkinter as tk

from tkinter import ttk

#Criando o frame e defnindo tamanho
window = tk.Tk() 
window.title('Combobox')
window.geometry('500x250')

ttk.Label(window).grid(row = 0, column = 1) #posicionando texto

n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width= 27, textvariable = n)

monthchoosen['values'] = ('Yuri', 'Garro', 'Cassio')

monthchoosen.grid(column= 1, row = 5)
monthchoosen.current()
var = tk.IntVar()

def show_selection():
    print(f"Checkbox is {'checked' if var.get() else 'unchecked'}")

checkbox = tk.Checkbutton(window, text="Clique aqui", variable=var, command=show_selection)
checkbox.grid()

window.mainloop()
