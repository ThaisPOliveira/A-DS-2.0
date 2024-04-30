#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os, sqlite3,pwinput
from datetime import datetime
estrato=[]
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
def extrato():
    arquivo_estrato=open("CRUD\estrato.txt","w")
    arquivo_estrato.write(f"{"EXTRATO":^50}\n")
    arquivo_estrato.write(f"{username:^50}\n")
    for i,(usuario,hora,relatorio) in enumerate(estrato):
        arquivo_estrato.write(f"{relatorio} {hora} \n")
    conn.close()
def Cadastro_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return "Nome de usuário já existe. Por favor, escolha outro."
    elif username==password:
        print("Usuario e senhas iguais, tente novamente")
    elif username!='' and password!="":
        cursor.execute("INSERT INTO usuarios (username, password, saldo) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        return "Cadastro realizado com sucesso!"
    else:
        print("usuario ou senha vazio")

def Login_usuario(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    if user:
        return user
    else:
        return None
def horario():
    hora=datetime.now()
    hora=hora.strftime("%d/%m/%Y %H:%M")
    return hora
def opcoes_banco(username, saldo):
    while True:
        opc1 = input(f'''
{"="*30}
DIGITE A OPERAÇÃO DESEJADA
1) Consultar saldo
2) Saque 
3) Depositar
4) Deletar conta
5) Pesquisar conta
0) Encerrar sessão: 
{"="*30}\n''')
        if opc1 == "1":
            print( "Seu saldo é de R$ {}".format(saldo))
        elif opc1 == "2":
            saque = float(input("Qual valor você deseja sacar? "))       
            if saldo < saque:
                print("\nValor insuficiente")
            else:
                saldo -= saque
                cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
                conn.commit()
                relato_saque=f"Saque de R$ {saque:.2f} realizado com sucesso."
                print(relato_saque)
                estrato.append([username,relato_saque,horario()])
        elif opc1 == "3":
            deposito=float(input("Qual valor que deseja depositar? "))
            saldo += deposito
            cursor.execute("UPDATE usuarios SET saldo = ? WHERE username = ?", (saldo, username))
            conn.commit()
            relato_deposito=f"Depósito de R$ {deposito} realizado."
            print(relato_deposito)
            estrato.append([username,relato_deposito,horario()])
        elif opc1 == "4":
            deletar_conta=input("Deseja deletar sua conta? (S/N)")
            if deletar_conta.lower() == "s":
                cursor.execute("DELETE FROM usuarios WHERE username = ?", (username,))
                conn.commit()
                print("Conta deletada.")
                return
        elif opc1=='5':
            pesquisa=input("digite nome do usuario ")
            cursor.execute("SELECT username FROM usuarios WHERE username= ?",(pesquisa,))
            pesquisa = cursor.fetchone()
            if pesquisa:
                print(f"usuario {pesquisa[0]} encontrado")
            else:
                print("nao encontrado")
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
extrato()