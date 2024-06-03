#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os
import sqlite3
from datetime import datetime

extrato = []
os.system('cls')

# Conexão com o banco de dados SQLite

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
def criar_tabela_usuarios():
    cursor.execute('''  CREATE TABLE IF NOT EXISTS usuarios (
                        cpf TEXT PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        saldo INTEGER
                    )''')

    conn.commit()

# Criando a tabela de extrato se não existir
def criar_tabela_extrato():
    cursor.execute('''CREATE TABLE IF NOT EXISTS extrato (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   cpf_usuario TEXT,
                   tipo TEXT,
                   valor FLOAT,
                   hora TEXT
    )''')
    conn.commit()
criar_tabela_usuarios()
criar_tabela_extrato()

# Função para consultar e exibir o extrato
def consultar_extrato(cpf):
    cursor.execute("SELECT * FROM extrato WHERE cpf_usuario = ? ORDER BY hora", (cpf,))
    extratos = cursor.fetchall()
    print("\n\033[94mExtrato:\n\033[0m")
    for extrato in extratos:
        print(f"Tipo: {extrato[2]}, Valor: R$ {extrato[3]:.2f}, Data/Hora: {extrato[4]}")
    cursor.execute("SELECT saldo FROM usuarios WHERE cpf = ?", (cpf,))
    saldo = cursor.fetchone()[0]
    print(f"\nSaldo atual: R$ {saldo:.2f}\n")

# Função para cadastrar usuário
def Cadastro_usuario(cpf, username, password):
    cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (cpf,))
    user = cursor.fetchone()
    if user:
        return "\033[91mNome de usuário já existe. Por favor, escolha outro.\033[0m"
    elif username == password:
        return "\033[91mUsuario e senhas iguais, tente novamente\033[0m"
    elif username != '' and password != "":
        cursor.execute("INSERT INTO usuarios (cpf, username, password, saldo) VALUES (?, ?, ?, ?)", (cpf, username, password, 0))
        conn.commit()
        return "\033[92mCadastro realizado com sucesso!\033[0m"
    else:
        return "\033[91mUsuário ou senha vazio\033[0m"

# Função para login de usuário
def Login_usuario(cpf, username, password):
    cursor.execute("SELECT * FROM usuarios WHERE cpf = ? AND username = ? AND password = ?", (cpf, username, password))
    user = cursor.fetchone()
    if user:
        return list(user)
    else:
        return None

# Função para obter o horário atual
def horario():
    hora = datetime.now()
    hora = hora.strftime("%Y-%m-%d %H:%M:%S")
    return hora

# Função de operações bancárias
def opcoes_banco(cpf, username, saldo):
    while True:
        print("=" * 33)
        print("\033[94mDIGITE A OPERAÇÃO DESEJADA\033[0m")
        print("\033[94m1) Consultar extrato\033[0m")
        print("\033[94m2) Saque\033[0m")
        print("\033[94m3) Depositar\033[0m")
        print("\033[94m4) Deletar conta\033[0m")
        print("\033[94m5) Pesquisar conta\033[0m")
        print("\033[94m0) Encerrar sessão\033[0m")
        print("=" * 33)
        opc1 = input()
        if opc1 == "1":
            os.system('cls')
            consultar_extrato(cpf)

        elif opc1 == "2":
            try:
                saque = float(input("Qual valor você deseja sacar? "))
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                if saldo < saque:
                    print("\033[91mValor insuficiente\033[0m")
                else:
                    tipo = "saque"
                    saldo -= saque
                    cursor.execute("UPDATE usuarios SET saldo = ? WHERE cpf = ?", (saldo, cpf))
                    hora = horario()
                    cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, tipo, saque, hora))
                    conn.commit()
                    print(f"\033[92mSaque de R$ {saque:.2f} realizado com sucesso.\033[0m")

        elif opc1 == "3":
            try:
                deposito = float(input("Qual valor que deseja depositar? "))
            except ValueError:
                print("\033[91mDigite um valor válido\033[0m")
            else:
                saldo += deposito
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE cpf = ?", (saldo, cpf))
                tipo = 'deposito'
                hora = horario()
                cursor.execute("INSERT INTO extrato (cpf_usuario, tipo, valor, hora) VALUES (?, ?, ?, ?)", (cpf, tipo, deposito, hora))
                conn.commit()
                print(f"\033[92mDepósito de R$ {deposito:.2f} realizado.\033[0m")

        elif opc1 == "4":
            deletar_conta = input("Deseja deletar sua conta? (S/N)")
            if deletar_conta.lower() == "s":
                cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
                conn.commit()
                print("\033[92mConta deletada.\033[0m")
                return

        elif opc1 == '5':
            pesquisa = input("Digite o nome do usuário: ")
            #cursor.execute("SELECT username FROM usuarios WHERE username = ?", (pesquisa,))
            cursor.execute("SELECT username, usuario FROM usuario")
            pesquisa = cursor.fetchone()
            if pesquisa:
                print(f"\033[92mUsuário {pesquisa[0]} encontrado.\033[0m")
            else:
                print("\033[91mNão encontrado.\033[0m")

        elif opc1 == "0":
            print("\033[92mEncerrando sessão...\033[0m")
            return
        else:
            print("\033[91mOpção inválida.\033[0m")

# Loop principal do programa
def principal():
    while True:
        print("=" * 33)
        print("\033[94m1. Cadastrar\033[0m")
        print("\033[94m2. Login\033[0m")
        print("\033[94m3. Sair\033[0m")
        print("=" * 33)

        opc = input("Escolha uma opção: ")

        if opc == "1":
            cpf = input("Digite um Cpf: ")
            username = input("Digite um nome de usuário: ")
            password = input("Digite uma senha: ", mask="*")
            print(Cadastro_usuario(cpf, username, password))
        elif opc == "2":
            cpf = input("Digite o seu Cpf: ")
            username = input("Digite seu nome de usuário: ")
            password = input ("Digite sua senha: ", mask="*")
            user = Login_usuario(cpf, username, password)
            if user:
                print("\033[92mLogin bem-sucedido!\033[0m")
                opcoes_banco(cpf, username, user[3])  # Passa o username e o saldo do usuário
            else:
                print("\033[91mNome de usuário ou senha incorretos. Tente novamente.\033[0m")
        elif opc == "3":
            print("\033[92mSaindo...\033[0m")
            break
        else:
            print("\033[91mOpção inválida. Por favor, escolha novamente.\033[0m")
