# Victor Lindolfo Silva
# # Bruno Teodoro Oliveira da Lomba
# # João Martins Bernades
# # Luis Felipe Rodrigues da Silva


# Códigos ANSI para cores
import os


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
    os.system('cls')
    ascii_art = f"""
{GREEN} 
  ___ ___    _   ___ _  _ 
 | _ ) _ \  /_\ |_ _| \| |
 | _ \   / / _ \ | || .` |
 |___/_|_\/_/ \_\___|_|\_|
                          
   {RESET}
    """
    print(ascii_art)



# Função para adicionar um livro
def adicionar_livro(biblioteca):
    try: 
        isbn = int(input(f"{CYAN}Digite o ISBN-13, somente números (formato XXX-X-XXXXX-XXXXX-X): {RESET}"))
    except ValueError:
        print(f"{RED}Digite somente números.{RESET}")
        return
    else:
        isbn = str(isbn)
        if not len(isbn)==13:
            print(f"{RED}ISBN inválido! Tente novamente.{RESET}")
            return
        titulo = input(f"{CYAN}Digite o título: {RESET}") 
        autor = input(f"{CYAN}Digite o autor: {RESET}")
        genero = input(f"{CYAN}Digite o gênero: {RESET}")

        for isbn_veficar, info in biblioteca.items():
            if isbn == isbn_veficar:
                print(f"{RED}ISBN já cadastrado.{RESET}")
                return
            elif info["Título"]==titulo:
                print(f"{RED}Título já cadastrado.{RESET}")
                return
                

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
        print(f"{RED}ISBN não encontrado.{RESET}")

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
        print(f"{RED}Autor não encontrado.{RESET}")

# Função para buscar um livro por gênero
def buscar_livro_genero(biblioteca):
    genero = input(f"{CYAN}Digite o gênero: {RESET}")
    encontrados = [info for info in biblioteca.values() if info['Gênero'].lower() == genero.lower()]
    if encontrados:
        for livro in encontrados:
            print(f"{WHITE}Título: {livro['Título']}, Autor: {livro['Autor']}, Gênero: {livro['Gênero']}{RESET}")
    else:
        print(f"{RED}Nenhum livro corresponde a esse gênero.{RESET}")

# Função para atualizar um livro
def atualizar_livro(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja atualizar: {RESET}")
    if isbn not in biblioteca:
        print(f"{RED}Livro não encontrado.{RESET}")
        return

    titulo = input(f"{CYAN}Digite o novo título (ou pressione Enter para manter o atual: {biblioteca[isbn]['Título']}): {RESET}")
    autor = input(f"{CYAN}Digite o novo autor (ou pressione Enter para manter o atual: {biblioteca[isbn]['Autor']}): {RESET}")
    genero = input(f"{CYAN}Digite o novo gênero (ou pressione Enter para manter o atual: {biblioteca[isbn]['Gênero']}): {RESET}")

    if titulo:
        biblioteca[isbn]['Título'] = titulo
    if autor:
        biblioteca[isbn]['Autor'] = autor
    if genero:
        biblioteca[isbn]['Gênero'] = genero

    print(f"{GREEN}Livro atualizado com sucesso!{RESET}")

# Função para excluir um livro
def excluir_livro(biblioteca):
    isbn = input(f"{CYAN}Digite o ISBN do livro que deseja excluir: {RESET}")
    if isbn in biblioteca:
        print(f'''Livro:
Título: {biblioteca[isbn]['Título']}
Autor: {biblioteca[isbn]['Autor']}
Gênero: {biblioteca[isbn]['Gênero']}''')
        confirmar_excluir = input("Tem certeza que deseja deletar esse livro? digite CONFIRMAR.")
        if confirmar_excluir == "CONFIRMAR":
            del biblioteca[isbn] 
            print(f"{GREEN}Livro excluído com sucesso!{RESET}")
        else:
            print(f"{RED}Exclusão cancelada.{RESET}")
    else:
        print(f"{RED}Livro não encontrado.{RESET}")

# Função principal para o menu
def menu():
    biblioteca = {}
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
            os.system('cls')
            adicionar_livro(biblioteca)
        elif opcao == "2":
            os.system('cls')
            visualizar_livros(biblioteca)
        elif opcao == "3":
            os.system('cls') 
            buscar_livro_isbn(biblioteca)
        elif opcao == "4":
            os.system('cls') 
            buscar_livro_titulo(biblioteca)
        elif opcao == "5":
            os.system('cls') 
            buscar_livro_autor(biblioteca)
        elif opcao == "6":
            os.system('cls') 
            buscar_livro_genero(biblioteca)
        elif opcao == "7":
            os.system('cls')
            atualizar_livro(biblioteca)
        elif opcao == "8":
            os.system('cls') 
            excluir_livro(biblioteca)
        elif opcao == "9":
            print(f"{GREEN}Saindo do programa...{RESET}")
            break
        else:
            os.system('cls')
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")


# Exibe o título em ASCII e inicia o menu
gerar_ascii()
menu()
