# Victor Lindolfo Silva
# # Bruno Teodoro Oliveira da Lomba
# # João Martins Bernades
# # Luis Felipe Rodrigues da Silva

import re

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
    ascii_art = f"""
{GREEN} 
  ___ ___    _   ___ _  _ 
 | _ ) _ \  /_\ |_ _| \| |
 | _ \   / / _ \ | || .` |
 |___/_|_\/_/ \_\___|_|\_|
                          
   {RESET}
    """
    print(ascii_art)

# Função para validar ISBN
def validar_isbn(isbn):
    return re.match(r'^\d{3}-\d{1,5}-\d{1,7}-\d{1,7}-\d{1,7}$', isbn) is not None

# Função para adicionar um livro
def adicionar_livro(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN (formato XXX-X-XXXXX-XXXXX-X): {RESET}")
    if not validar_isbn(isbn):
        print(f"{RED}ISBN inválido! Tente novamente.{RESET}")
        return

    titulo = input(f"{CYAN}Digite o título: {RESET}")
    autor = input(f"{CYAN}Digite o autor: {RESET}")
    genero = input(f"{CYAN}Digite o gênero: {RESET}")

    if not all([isbn, titulo, autor, genero]):
        print(f"{RED}Todos os campos são obrigatórios!{RESET}")
        return

    biblioteca[isbn] = {
        "Título": titulo,
        "Autor": autor,
        "Gênero": genero
    }
    print(f"{GREEN}Livro adicionado com sucesso!{RESET}")

# Função para visualizar todos os livros
def visualizar_livros(biblioteca):
    if not biblioteca:
        print(f"{YELLOW}Nenhum livro cadastrado.{RESET}")
        return

    print(f"{BLUE}Lista de Livros:{RESET}")
    for isbn, info in biblioteca.items():
        print(f"{WHITE}ISBN: {isbn}, Título: {info['Título']}, Autor: {info['Autor']}, Gênero: {info['Gênero']}{RESET}")

# Função para buscar um livro por ISBN
def buscar_livro_isbn(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN: {RESET}")
    livro = biblioteca.get(isbn)
    if livro:
        print(f"{WHITE}ISBN: {isbn}, Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função para buscar um livro por título
def buscar_livro_titulo(biblioteca):
    titulo = input(f"{CYAN}Digite o título: {RESET}")
    encontrados = [info for info in biblioteca.values() if info['Título'].lower() == titulo.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{WHITE}Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função para buscar um livro por autor
def buscar_livro_autor(biblioteca):
    autor = input(f"{CYAN}Digite o autor: {RESET}")
    encontrados = [info for info in biblioteca.values() if info['Autor'].lower() == autor.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{WHITE}Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função para buscar um livro por gênero
def buscar_livro_genero(biblioteca):
    genero = input(f"{CYAN}Digite o gênero: {RESET}")
    encontrados = [info for info in biblioteca.values() if info['Gênero'].lower() == genero.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{WHITE}Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função para atualizar um livro
def atualizar_livro(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja atualizar: {RESET}")
    if isbn not in biblioteca:
        print(f"{RED}Livro não encontrado.{RESET}")
        return

    titulo = input(f"{CYAN}Digite o novo título: {RESET}")
    autor = input(f"{CYAN}Digite o novo autor: {RESET}")
    genero = input(f"{CYAN}Digite o novo gênero: {RESET}")

    if not all([titulo, autor, genero]):
        print(f"{RED}Todos os campos são obrigatórios!{RESET}")
        return

    biblioteca[isbn] = {
        "Título": titulo,
        "Autor": autor,
        "Gênero": genero
    }
    print(f"{GREEN}Livro atualizado com sucesso!{RESET}")

# Função para excluir um livro
def excluir_livro(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja excluir: {RESET}")
    if isbn in biblioteca:
        del biblioteca[isbn]
        print(f"{GREEN}Livro excluído com sucesso!{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função principal para o menu
def menu():
    biblioteca = {}
    while True:
        print(f"\n{MAGENTA}Menu:{RESET}")
        print("1. Adicionar Livro")
        print("2. Visualizar Livros")
        print("3. Buscar Livro por ISBN")
        print("4. Buscar Livro por Título")
        print("5. Buscar Livro por Autor")
        print("6. Buscar Livro por Gênero")
        print("7. Atualizar Livro")
        print("8. Excluir Livro")
        print("9. Sair")
        
        opcao = input(f"{YELLOW}Escolha uma opção: {RESET}")
        
        if opcao == "1":
            adicionar_livro(biblioteca)
        elif opcao == "2":
            visualizar_livros(biblioteca)
        elif opcao == "3":
            buscar_livro_isbn(biblioteca)
        elif opcao == "4":
            buscar_livro_titulo(biblioteca)
        elif opcao == "5":
            buscar_livro_autor(biblioteca)
        elif opcao == "6":
            buscar_livro_genero(biblioteca)
        elif opcao == "7":
            atualizar_livro(biblioteca)
        elif opcao == "8":
            excluir_livro(biblioteca)
        elif opcao == "9":
            print(f"{GREEN}Saindo do programa...{RESET}")
            break
        else:
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")

# Exibe o título em ASCII e inicia o menu
gerar_ascii()
menu()
