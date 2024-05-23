from tkinter import *
janela = Tk()

janela.title("Oiiiiii")
janela.geometry('600x400')

titulo = Label(janela,text="erick cabeção")
titulo.place(x=300, y=180) 
titulo['fg'] = ("purple")
sair = Button(text="sair",command=janela.destroy)
janela.mainloop()