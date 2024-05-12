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
cursor = conn.cursor()

# Criando a tabela de usuários se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    username TEXT PRIMARY KEY,
                    password TEXT,
                    saldo INTEGER
                )''')

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