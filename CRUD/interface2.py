import os
import sqlite3
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pwinput

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    cpf TEXT PRIMARY KEY,
                    username TEXT,
                    password TEXT,
                    saldo INTEGER
                )''')
conn.commit()

# Criando a tabela de extrato se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS extrato (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cpf_usuario TEXT,
                    tipo TEXT,
                    valor FLOAT,
                    hora TEXT
                )''')
conn.commit()

def Cadastro_usuario(cpf, username, password):
    cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (cpf,))
    user = cursor.fetchone()
    if user:
        return "CPF já cadastrado. Por favor, escolha outro."
    elif username == password:
        return "Usuário e senha iguais, tente novamente."
    elif username != '' and password != "":
        cursor.execute("INSERT INTO usuarios (cpf, username, password, saldo) VALUES (?, ?, ?, ?)", (cpf, username, password, 0))
        conn.commit()
        return "Cadastro realizado com sucesso!"
    else:
        return "Usuário ou senha vazio."

def Login_usuario(cpf, username, password):
    cursor.execute("SELECT * FROM usuarios WHERE cpf = ? AND username = ? AND password = ?", (cpf, username, password))
    user = cursor.fetchone()
    if user:
        return list(user)
    else:
        return None

def horario():
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return hora

def exibir_mensagem(texto_mensagem, mensagem):
    texto_mensagem.insert(END, mensagem + '\n')
    texto_mensagem.see(END)

def tela_cadastro():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_cadastro = Toplevel()
    janela_cadastro.title("Tela de Cadastro")
    janela_cadastro.geometry('620x400')
    janela_cadastro.config(bg='black')
    
    Label(janela_cadastro, text="CPF:", bg='black', fg='blue').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    cpf_entry = Entry(janela_cadastro)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Nome de usuário:", bg='black', fg='blue').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    username_entry = Entry(janela_cadastro)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Senha:", bg='black', fg='blue').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    password_entry = Entry(janela_cadastro, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def realizar_cadastro():
        cpf = cpf_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        mensagem = Cadastro_usuario(cpf, username, password)
        exibir_mensagem(caixa_mensagem, mensagem)
    
    Button(janela_cadastro, text="Cadastrar", command=realizar_cadastro).grid(row=3, columnspan=2, pady=10)
    Button(janela_cadastro, text="Voltar", command=lambda: voltar(janela_cadastro)).grid(row=3, column=1, pady=10)
    
    caixa_mensagem = Text(janela_cadastro, width=50, height=10)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

def opcoes_banco(cpf, username, saldo):
    janela_menu = Toplevel()
    janela_menu.title("Menu")
    janela_menu.geometry('620x400')
    janela_menu.config(bg='black')
    
    caixa_mensagem = Text(janela_menu, width=30, height=10)
    caixa_mensagem.grid(row=0, column=1, padx=10, pady=10, rowspan=4, sticky=E)

    def consultar_extrato():
        cursor.execute("SELECT * FROM extrato WHERE cpf_usuario = ?", (cpf,))
        extratos = cursor.fetchall()
        if extratos:
            for extrato in extratos:
                mensagem = f"Tipo: {extrato[2]}, Valor: {extrato[3]}, Hora: {extrato[4]}"
                exibir_mensagem(caixa_mensagem, mensagem)
        else:
            exibir_mensagem(caixa_mensagem, "Nenhum extrato encontrado.")

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
                    cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, 'saque', saque_valor, horario()))
                    conn.commit()
                    exibir_mensagem(caixa_mensagem, f"Saque de R$ {saque_valor:.2f} realizado com sucesso.")
            except ValueError:
                exibir_mensagem(caixa_mensagem, "Digite um valor válido.")
        
        saque_window = Toplevel(janela_menu)
        saque_window.title("Saque")
        saque_window.geometry('300x200')
        Label(saque_window, text="Valor do Saque:").pack(pady=10)
        saque_entry = Entry(saque_window)
        saque_entry.pack(pady=10)
        Button(saque_window, text="Confirmar", command=saque).pack(pady=10)

    def realizar_deposito():
        def deposito():
            try:
                deposito_valor = float(deposito_entry.get())
                cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
                saldo_atual = cursor.fetchone()[0]
                novo_saldo = saldo_atual + deposito_valor
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE cpf = ?", (novo_saldo, cpf))
                cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, 'deposito', deposito_valor, horario()))
                conn.commit()
                exibir_mensagem(caixa_mensagem, f"Depósito de R$ {deposito_valor:.2f} realizado com sucesso.")
            except ValueError:
                exibir_mensagem(caixa_mensagem, "Digite um valor válido.")
        
        deposito_window = Toplevel(janela_menu)
        deposito_window.title("Depósito")
        deposito_window.geometry('300x200')
        Label(deposito_window, text="Valor do Depósito:").pack(pady=10)
        deposito_entry = Entry(deposito_window)
        deposito_entry.pack(pady=10)
        Button(deposito_window, text="Confirmar", command=deposito).pack(pady=10)
    
    def deletar_conta():
        def confirmar_delecao():
            cursor.execute("DELETE FROM usuarios WHERE cpf = ?", (cpf,))
            cursor.execute("DELETE FROM extrato WHERE cpf_usuario = ?", (cpf,))
            conn.commit()
            exibir_mensagem(caixa_mensagem, "Conta deletada com sucesso.")
            janela_menu.destroy()

        confirm_window = Toplevel(janela_menu)
        confirm_window.title("Confirmar Deleção")
        confirm_window.geometry('300x200')
        Label(confirm_window, text="Deseja deletar sua conta?").pack(pady=10)
        Button(confirm_window, text="Sim", command=confirmar_delecao).pack(side=LEFT, padx=20, pady=10)
        Button(confirm_window, text="Não", command=confirm_window.destroy).pack(side=RIGHT, padx=20, pady=10)
    
    Button(janela_menu, text="Consultar Extrato", command=consultar_extrato, width=30).grid(row=0, column=0, padx=10, pady=10, sticky=W)
    Button(janela_menu, text="Saque", command=realizar_saque, width=30).grid(row=1, column=0, padx=10, pady=10, sticky=W)
    Button(janela_menu, text="Depósito", command=realizar_deposito, width=30).grid(row=2, column=0, padx=10, pady=10, sticky=W)
    Button(janela_menu, text="Deletar Conta", command=deletar_conta, width=30).grid(row=4, column=1, padx=10, pady=10, sticky=E)

def tela_login():
    janela_principal.withdraw()  # Oculta a janela principal
    janela_login = Toplevel()
    janela_login.title("Tela de Login")
    janela_login.geometry('620x400')
    janela_login.config(bg='black')
    
    Label(janela_login, text="CPF:", bg='black', fg='blue').grid(row=0, column=0, padx=10, pady=10, sticky=W)
    cpf_entry = Entry(janela_login)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_login, text="Nome de usuário:", bg='black', fg='blue').grid(row=1, column=0, padx=10, pady=10, sticky=W)
    username_entry = Entry(janela_login)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_login, text="Senha:", bg='black', fg='blue').grid(row=2, column=0, padx=10, pady=10, sticky=W)
    password_entry = Entry(janela_login, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    
    def realizar_login():
        cpf = cpf_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        usuario = Login_usuario(cpf, username, password)
        if usuario:
            opcoes_banco(cpf, username, usuario[3])
        else:
            exibir_mensagem(caixa_mensagem, "Usuário ou senha incorretos.")
    
    Button(janela_login, text="Login", command=realizar_login).grid(row=3, columnspan=2, pady=10)
    Button(janela_login, text="Voltar", command=lambda: voltar(janela_login)).grid(row=3, column=1, pady=10)
    
    caixa_mensagem = Text(janela_login, width=50, height=10)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

def voltar(janela):
    janela.destroy()
    janela_principal.deiconify()  # Mostra a janela principal novamente

# Janela Principal
janela_principal = Tk()
janela_principal.title("Sistema Bancário")
janela_principal.geometry('620x400')
janela_principal.config(bg='black')

Label(janela_principal, text="Bem-vindo ao Sistema Bancário", bg='black', fg='blue', font=("Helvetica", 16)).pack(pady=20)
Button(janela_principal, text="Cadastro", command=tela_cadastro, width=30).pack(pady=10)
Button(janela_principal, text="Login", command=tela_login, width=30).pack(pady=10)
Button(janela_principal, text="Sair", command=janela_principal.quit, width=30).pack(pady=10)

janela_principal.mainloop()

conn.close()
