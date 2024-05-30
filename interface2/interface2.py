import os
import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import messagebox
janela = Tk()

def principal():
    janela = Tk()
    janela.title("Sistema Bancário")
    janela.geometry('620x400')
    janela.config(bg='black')

    titulo1 = Label(janela, text="SISTEMA BANCÁRIO", font=("Helvetica", 16, "italic", "bold"), fg="blue", bg="black")
    titulo1.place(x=215, y=10)

    titulo2 = Label(janela, text="Selecione a opção desejada", font=("Helvetica", 10, "bold"), fg="blue", bg="black")
    titulo2.place(x=220, y=50)

    botao_cadastro = Button(janela, text="Cadastrar", command=tela_cadastro(), width=30)
    botao_cadastro.place(x=200, y=100)

    botao_login = Button(janela, text="Login",  width=30)
    botao_login.place(x=200, y=150)

    botao_sair = Button(janela, text="Sair", width=30)
    botao_sair.place(x=200, y=200)

    janela.mainloop()

def tela_cadastro():
    global janela
    janela.destroy()
    janela_cadastro= Tk()

    janela_cadastro.title("Tela de Cadastro")
    janela_cadastro.geometry('620x400')
    janela_cadastro.config(bg='gray')
    
    Label(janela_cadastro, text="CPF:", bg='gray', fg='black').grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(janela_cadastro)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Nome de usuário:", bg='gray', fg='black').grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(janela_cadastro)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Senha:", bg='gray', fg='black').grid(row=2, column=0, padx=10, pady=10)
    password_entry = Entry(janela_cadastro, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    Button(janela_cadastro, text="voltar", comand=janela_cadastro.destroy()).grid(row=3, columnspan=2, pady=10)

principal()
