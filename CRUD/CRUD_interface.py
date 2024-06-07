#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

# OBS: código funcionando importando as funções do arquivo CRUD.py
import sqlite3
from tkinter import *
from tkinter import messagebox, filedialog
import CRUD as crud
from datetime import datetime
from PIL import ImageTk, Image
import os


# Conexão com o banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
crud.criar_tabela_usuarios()

# Criando a tabela de extrato se não existir
crud.criar_tabela_extrato()

def exibir_mensagem(caixa_mensagem_texto, mensagem):
    caixa_mensagem_texto.insert(END, mensagem + '\n')
    caixa_mensagem_texto.see(END)

def tela_cadastro():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_cadastro = Toplevel()
    janela_cadastro.title("Tela de Cadastro")
    janela_cadastro.geometry('445x310')
    janela_cadastro.config(bg='black')
   
    Label(janela_cadastro, text="CPF:", bg='black', fg='white').grid(row=0, column=0, padx=10, pady=10, sticky=W)
   
    cpf_entry = Entry(janela_cadastro)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Nome de usuário:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    username_entry = Entry(janela_cadastro)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Senha:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    password_entry = Entry(janela_cadastro, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def realizar_cadastro():
        cpf = cpf_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        mensagem = crud.Cadastro_usuario(cpf, username, password)
        exibir_mensagem(caixa_mensagem, mensagem)
    
    Button(janela_cadastro, text="Cadastrar", command=realizar_cadastro).grid(row=3, columnspan=2, pady=10)
    Button(janela_cadastro, text="Voltar", command=lambda: voltar(janela_cadastro)).grid(row=3, column=1, pady=10)
    
    caixa_mensagem = Text(janela_cadastro, width=50, height=5)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

def opcoes_banco(cpf, username, saldo):
    
    janela_menu = Toplevel()
    janela_menu.title("Menu")
    janela_menu.geometry('620x400')
    janela_menu.config(bg='black')
    frame = Frame(janela_menu, bg='black')
    frame.pack()

    caixa_mensagem = Text(janela_menu, width=60, height=5, bg='white', fg='black')
    caixa_mensagem.pack(side='bottom', pady=10)

    def consultar_extrato():
        cursor.execute("SELECT * FROM extrato WHERE cpf_usuario = ?", (cpf,))
        extratos = cursor.fetchall()
        cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
        saldo = cursor.fetchone()[0]
        if extratos:
            for extrato in extratos:
                mensagem = f"Tipo: {extrato[2]}, Valor: {extrato[3]}, Hora: {extrato[4]}"
                saldo_atual = f"Saldo atual R${saldo}"
                exibir_mensagem(caixa_mensagem, mensagem)
        else:
            exibir_mensagem(caixa_mensagem, "Nenhum extrato encontrado.")
            saldo = 0
            saldo_atual = f"Saldo atual R${saldo}"
        exibir_mensagem(caixa_mensagem, saldo_atual)


    def realizar_saque():
        def saque():
            try:
                saque_valor = float(saque_entry.get())
                cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
                saldo_atual = cursor.fetchone()[0]
                if saque_valor > saldo_atual:
                    exibir_mensagem(caixa_mensagem, "Valor insuficiente.")
                else:
                    novo_saldo = saldo_atual - saque_valor
                    cursor.execute("UPDATE usuarios SET saldo = ? WHERE cpf = ?", (novo_saldo, cpf))
                    cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, 'saque', saque_valor, crud.horario()))
                    conn.commit()
                    exibir_mensagem(caixa_mensagem, f"Saque de R$ {saque_valor:.2f} realizado com sucesso.")
            except ValueError:
                exibir_mensagem(caixa_mensagem, "Digite um valor válido.")
        
        saque_window = Toplevel(janela_menu)
        saque_window.title("Saque")
        saque_window.geometry('300x200')
        saque_window.config(bg='black')
        Label(saque_window, text="Valor do Saque:", bg='black', fg='white').pack(pady=10)
        saque_entry = Entry(saque_window)
        saque_entry.pack(pady=10)
        frame = Frame(saque_window,bg='black')
        frame.pack()
        Button(frame, text="Confirmar", command=saque).pack(side="left", padx=7, pady=10)
        Button(frame, text="Voltar", command=saque_window.destroy).pack(side="left", padx=10, pady=10)

    def realizar_deposito():
        def deposito():
            try:
                deposito_valor = float(deposito_entry.get())
                cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
                saldo_atual = cursor.fetchone()[0]
                novo_saldo = saldo_atual + deposito_valor
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE cpf = ?", (novo_saldo, cpf))
                cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, 'deposito', deposito_valor, crud.horario()))
                conn.commit()
                exibir_mensagem(caixa_mensagem, f"Depósito de R$ {deposito_valor:.2f} realizado com sucesso.")
            except ValueError:
                exibir_mensagem(caixa_mensagem, "Digite um valor válido.")
        
        deposito_window = Toplevel(janela_menu)
        deposito_window.title("Depósito")
        deposito_window.geometry('300x200')
        deposito_window.config(bg='black')
        Label(deposito_window, text="Valor do Depósito:", bg='black', fg='white').pack(pady=10)
        deposito_entry = Entry(deposito_window)
        deposito_entry.pack(pady=10)
        frame = Frame(deposito_window,bg='black')
        frame.pack()
        Button(frame, text="Confirmar", command=deposito).pack(side="left", padx=7, pady=10)
        Button(frame, text="Voltar", command=deposito_window.destroy).pack(side="left", padx=10, pady=10)
   
    
    def deletar_conta():
        def confirmar_delecao():
            cursor.execute("DELETE FROM usuarios WHERE cpf = ?", (cpf,))
            cursor.execute("DELETE FROM extrato WHERE cpf_usuario = ?", (cpf,))
            conn.commit()
            exibir_mensagem(caixa_mensagem, "Conta deletada com sucesso.")
            janela_menu.destroy()
            janela_principal.deiconify()

        confirm_window = Toplevel(janela_menu)
        confirm_window.title("Confirmar zDeleção")
        confirm_window.geometry('300x200')
        confirm_window.config(bg='black')
        cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
        saldo_atual = cursor.fetchone()[0]
        Label(confirm_window, text="Deseja deletar sua conta?"+
              "\n Conta atual"+
              f"\nCPF: {cpf} Saldo R${saldo_atual}  ",  bg='black', fg='white').pack(pady=10)
        Button(confirm_window, text="Sim", command=confirmar_delecao).pack(side=LEFT, padx=20, pady=10)
        Button(confirm_window, text="Não", command=confirm_window.destroy).pack(side=RIGHT, padx=20, pady=10)
    
    Button(frame, text="Consultar Extrato", command=consultar_extrato, width=30).grid(row=0, column=0, padx=10, pady=10, sticky=W)
    Button(frame, text="Saque", command=realizar_saque, width=30).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    Button(frame, text="Depósito", command=realizar_deposito, width=30).grid(row=2, column=0, padx=10, pady=10, sticky=W)
    Button(frame, text="Deletar Conta", command=deletar_conta, width=30).grid(row=3, column=0, padx=10, pady=10, sticky=W)
    Button(frame, text="Sair", command=janela_menu.destroy, width=30).grid(row=4, column=0, padx=10, pady=10, sticky=W)
    

def tela_login():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_login = Toplevel()
    janela_login.title("Tela de Login")
    janela_login.geometry('445x310')
    janela_login.config(bg='black')
    
    Label(janela_login, text="CPF:", bg='black', fg='white').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    cpf_entry = Entry(janela_login)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_login, text="Nome de usuário:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    username_entry = Entry(janela_login)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_login, text="Senha:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    password_entry = Entry(janela_login, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def realizar_login():
        cpf = cpf_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        usuario = crud.Login_usuario(cpf, username, password)
        if usuario:
            opcoes_banco(cpf, username, usuario[3])
            janela_login.withdraw()
        else:
            exibir_mensagem(caixa_mensagem, "Usuário ou senha incorretos.")
    
    Button(janela_login, text="Login", command=realizar_login).grid(row=3, columnspan=2, pady=10)
    Button(janela_login, text="Voltar", command=lambda: voltar(janela_login)).grid(row=3, column=1, pady=10)
    
    caixa_mensagem = Text(janela_login, width=50, height=5)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

def voltar(janela):
    janela.destroy()
    janela_principal.deiconify()  # Mostra a janela principal novamente

# Janela Principal
janela_principal = Tk()
janela_principal.title("Sistema Bancário")
janela_principal.geometry('620x400')
janela_principal.config(bg='black')
frame = Frame(janela_principal, bg='black')
frame.pack()

image = Image.open("CRUD/logo_reet.jpg")
resize=image.resize((100,100))
image = ImageTk.PhotoImage(resize)
logo = Label(image= image)
logo.image=image
logo.place(x=510, y=300)
# -----

Label(frame, text="Bem-vindo ao Sistema Bancário", bg='black', fg='white', font=("Helvetica", 16)).pack(pady=20)
Button(frame, text="Cadastro", command=tela_cadastro, width=30).pack(pady=10)
Button(frame, text="Login", command=tela_login, width=30).pack(pady=10)
Button(frame, text="Sair", command=janela_principal.quit, width=30).pack(pady=10)

janela_principal.mainloop()

conn.close()

