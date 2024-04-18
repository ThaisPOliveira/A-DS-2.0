#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os, sqlite3,pwinput
os.system('cls')
# Conexão com o banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    saldo INTEGER
                )''')
conn.commit()

def Cadastro_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return "Nome de usuário já existe. Por favor, escolha outro."
    else:
        cursor.execute("INSERT INTO usuarios (username, password, saldo) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        return "Cadastro realizado com sucesso!"

def Login_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return user
    else:
        return None

def opcoes_banco(username, saldo):
    while True:
        opc1 = input(f'''
{"="*30}
DIGITE A OPERAÇÃO DESEJADA
1) Consultar saldo
2) Saque 
3) Depositar
4) Deletar conta
0) Encerrar sessão: 
{"="*30}\n''')
        if opc1 == "1":
            print( "Seu saldo é de R$ {}".format(saldo))
        elif opc1 == "2":
            saque = int(input("Qual valor você deseja sacar? "))       
            if saldo < saque:
                print("\nValor insuficiente")
            else:
                saldo -= saque
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
                conn.commit()
                print("Valor do saque de R$ {} realizado com sucesso".format(saque))
        elif opc1 == "3":
            deposito=int(input("Qual valor que deseja depositar? "))
            saldo += deposito
            cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
            conn.commit()
            print(f"Depósito de R$ {deposito} realizado \nSaldo atual R$ {saldo}")
        elif opc1 == "4":
            deletar_conta=input("Deseja deletar sua conta? (S/N)")
            if deletar_conta.lower() == "s":
                cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
                conn.commit()
                print("Conta deletada.")
                return
        elif opc1 == "0":
            print("Encerrando sessão...")
            return
        else:
            print("Opção inválida.")

while True:
    print("="*30)
    opc = input(f'''
    1. Cadastrar
    2. Login
    3. Sair
    Escolha uma opção: ''')
    print("="*30)

    if opc == "1":
        username = input("Digite um nome de usuário: ")
        password = pwinput.pwinput("Digite uma senha: ", mask="*")
        print(Cadastro_usuario(username, password))
    elif opc == "2":
        username = input("Digite seu nome de usuário: ")
        password = pwinput.pwinput("Digite sua senha: ", mask="*")

        user = Login_usuario(username, password)
        if user:
            print("Login bem-sucedido!")
            opcoes_banco(username, user[2])  # Passa o username e o saldo do usuário
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
    elif opc == "3":
        print("Saindo...")
        break   
    else:
        print("Opção inválida. Por favor, escolha novamente.")

conn.close()
