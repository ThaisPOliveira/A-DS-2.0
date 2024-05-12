#UMC ADS - 1°D
#Nomes: 
#       Eduardo Vicente Ferreira das Neves: 11241104345
#       Erick Fernando Martins Santos: 11241504537
#       Rafael da Silva Castro: 11241104987
#       Thais Perreira de Oliveira: 11241103553

#Pré Projeto Crud em Python
import os
import sqlite3
import pwinput
from datetime import datetime

estrato = []
os.system('cls')

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('banco.db')
cursor = conn.cursor() #tem q tirar isso aqui, né? ou nn

# Criando a tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    saldo INTEGER
                )''')  #tem q tirar isso aqui, né? ou nn

conn.commit()

#txt
def extrato():
    arquivo_estrato = open("CRUD\estrato.txt", "w")
    arquivo_estrato.write(f"{'EXTRATO':^50}\n")
    arquivo_estrato.write(f"{username:^50}\n")
    for i, (usuario, hora, relatorio) in enumerate(estrato):
        arquivo_estrato.write(f"{relatorio} {hora} \n")
    conn.close()

#txt
def Cadastro_usuario(username, password):
    arquivo_cadastrotxt = open ("crud\cadastrotxt", "w")
    for linha in arquivo_cadastrotxt:
      arquivo_cadastrotxt.readline(" ")
      if username in linha:
       return "\033[91mNome de usuário já existe. Por favor, escolha outro.\033[0m"
      elif username == password:
        return "\033[91mUsuario e senhas iguais, tente novamente\033[0m"
      elif username != '' and password != "":
        cursor.execute(".White usuarios (username, password, saldo) VALUES (?, ?, ?)", (username, password, 0))
        conn.commit()
        return "\033[92mCadastro realizado com sucesso!\033[0m"
      else:
        return "\033[91mUsuário ou senha vazio\033[0m"
