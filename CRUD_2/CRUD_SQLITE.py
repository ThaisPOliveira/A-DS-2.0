# Victor Lindolfo Silva
# Bruno Teodoro Oliveira da Lomba
# João Martins Bernades
# Luis Felipe Rodrigues da Silva

import os
import sqlite3

# Códigos ANSI para cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Gerador de ASCII para o título da aplicação
def gerar_ascii():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = f"""
{GREEN} 
  ___ ___    _   ___ _  _ 
 | _ ) _ \  /_\ |_ _| \| |
 | _ \   / / _ \ | || .` |
 |___/_|_\/_/ \_\___|_|\_|
                          
   {RESET}
    """
    print(ascii_art)

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            genero TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um livro
def adicionar_livro():
    try: 
        isbn = int(input(f"{CYAN}Digite o ISBN-13, somente números (formato XXXXXXXXXXXXXXX (13 digitos)): {RESET}"))
    except ValueError:
        print(f"{RED}Digite somente números.{RESET}")
        return
    else:
        isbn = str(isbn)
        if not len(isbn) == 13:
            print(f"{RED}ISBN inválido! Tente novamente.{RESET}")
            return
        titulo = input(f"{CYAN}Digite o título: {RESET}") 
        autor = input(f"{CYAN}Digite o autor: {RESET}")
        genero = input(f"{CYAN}Digite o gênero: {RESET}")

    if not all([isbn, titulo, autor, genero]):
        print(f"{RED}Todos os campos são obrigatórios!{RESET}")
        return

    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros WHERE isbn = ? OR titulo = ?', (isbn, titulo))
    if cursor.fetchone():
        print(f"{RED}ISBN ou Título já cadastrado.{RESET}")
    else:
        cursor.execute('INSERT INTO livros (isbn, titulo, autor, genero) VALUES (?, ?, ?, ?)', (isbn, titulo, autor, genero))
        conn.commit()
        print(f"{GREEN}Livro adicionado com sucesso!{RESET}")

    conn.close()

# Função para visualizar todos os livros
def visualizar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()

    if not livros:
        print(f"{YELLOW}Nenhum livro cadastrado.{RESET}")
        return

    print(f"{BLUE}Lista de Livros:{RESET}")
    for livro in livros:
        print(f"{WHITE}ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}{RESET}")

# Função para buscar um livro por ISBN
def buscar_livro_isbn():
    isbn = input(f"{CYAN}Digite o ISBN: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()
    conn.close()

    if livro:
        print(f"{WHITE}ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}{RESET}")
    else:
        print(f"{RED}ISBN não encontrado.{RESET}")

# Função para buscar um livro por título
def buscar_livro_titulo():
    titulo = input(f"{CYAN}Digite o título: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE titulo = ?', (titulo,))
    livros = cursor.fetchall()
    conn.close()

    if livros:
        for livro in livros:
            print(f"{WHITE}Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função para buscar um livro por autor
def buscar_livro_autor():
    autor = input(f"{CYAN}Digite o autor: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor,))
    livros = cursor.fetchall()
    conn.close()

    if livros:
        for livro in livros:
            print(f"{WHITE}Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}{RESET}")
    else:
        print(f"{RED}Autor não encontrado.{RESET}")

# Função para buscar um livro por gênero
def buscar_livro_genero():
    genero = input(f"{CYAN}Digite o gênero: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE genero = ?', (genero,))
    livros = cursor.fetchall()
    conn.close()

    if livros:
        for livro in livros:
            print(f"{WHITE}Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}{RESET}")
    else:
        print(f"{RED}Nenhum livro corresponde a esse gênero.{RESET}")

# Função para atualizar um livro
def atualizar_livro():
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja atualizar: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()

    if not livro:
        print(f"{RED}Livro não encontrado.{RESET}")
        conn.close()
        return

    titulo = input(f"{CYAN}Digite o novo título (ou pressione Enter para manter o atual: {livro[1]}): {RESET}")
    autor = input(f"{CYAN}Digite o novo autor (ou pressione Enter para manter o atual: {livro[2]}): {RESET}")
    genero = input(f"{CYAN}Digite o novo gênero (ou pressione Enter para manter o atual: {livro[3]}): {RESET}")

    if titulo:
        cursor.execute('UPDATE livros SET titulo = ? WHERE isbn = ?', (titulo, isbn))
    if autor:
        cursor.execute('UPDATE livros SET autor = ? WHERE isbn = ?', (autor, isbn))
    if genero:
        cursor.execute('UPDATE livros SET genero = ? WHERE isbn = ?', (genero, isbn))

    conn.commit()
    conn.close()
    print(f"{GREEN}Livro atualizado com sucesso!{RESET}")

# Função para excluir um livro
def excluir_livro():
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja excluir: {RESET}")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()

    if livro:
        print(f'''Livro:
Título: {livro[1]}
Autor: {livro[2]}
Gênero: {livro[3]}''')
        confirmar_excluir = input("Tem certeza que deseja deletar esse livro? Digite CONFIRMAR: ")
        if confirmar_excluir == "CONFIRMAR":
            cursor.execute('DELETE FROM livros WHERE isbn = ?', (isbn,))
            conn.commit()
            print(f"{GREEN}Livro excluído com sucesso!{RESET}")
        else:
            print(f"{RED}Exclusão cancelada.{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

    conn.close()

# Função principal para o menu
def menu():
    init_db()
    while True:
        print(f'''\n{MAGENTA}Menu:{RESET}
1. Adicionar Livro
2. Visualizar Livros
3. Buscar Livro por ISBN
4. Buscar Livro por Título
5. Buscar Livro por Autor
6. Buscar Livro por Gênero
7. Atualizar Livro
8. Excluir Livro
9. Sair''')
        
        opcao = input(f"{YELLOW}Escolha uma opção: {RESET}")
        
        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            adicionar_livro()
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            visualizar_livros()
        elif opcao == "3":
            os.system('cls' if os.name == 'nt' else 'clear') 
            buscar_livro_isbn()
        elif opcao == "4":
            os.system('cls' if os.name == 'nt' else 'clear') 
            buscar_livro_titulo()
        elif opcao == "5":
            os.system('cls' if os.name == 'nt' else 'clear') 
            buscar_livro_autor()
        elif opcao == "6":
            os.system('cls' if os.name == 'nt' else 'clear') 
            buscar_livro_genero()
        elif opcao == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            atualizar_livro()
        elif opcao == "8":
            os.system('cls' if os.name == 'nt' else 'clear') 
            excluir_livro()
        elif opcao == "9":
            print(f"{GREEN}Saindo do programa...{RESET}")
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")

# Exibe o título em ASCII e inicia o menu
gerar_ascii()
menu()
