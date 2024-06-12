import tkinter as tk
from tkinter import messagebox
import os
import sqlite3

# Definindo as cores ANSI
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

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

def adicionar_livro():
    try: 
        isbn = int(isbn_entry.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite somente números.")
        return
    else:
        isbn = str(isbn)
        if not len(isbn) == 13:
            messagebox.showerror("Erro", "ISBN inválido! Deve conter 13 dígitos.")
            return

    titulo = titulo_entry.get() 
    autor = autor_entry.get()
    genero = genero_entry.get()

    if not all([isbn, titulo, autor, genero]):
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros WHERE isbn = ? OR titulo = ?', (isbn, titulo))
    if cursor.fetchone():
        messagebox.showerror("Erro", "ISBN ou Título já cadastrado.")
    else:
        cursor.execute('INSERT INTO livros (isbn, titulo, autor, genero) VALUES (?, ?, ?, ?)', (isbn, titulo, autor, genero))
        conn.commit()
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

    conn.close()

def abrir_adicionar_livro():
    adicionar_window = tk.Toplevel(root)
    adicionar_window.title("Adicionar Livro")

    # Labels e campos de entrada
    isbn_label = tk.Label(adicionar_window, text="ISBN (13 dígitos):")
    isbn_label.grid(row=0, column=0, padx=10, pady=5)
    global isbn_entry
    isbn_entry = tk.Entry(adicionar_window)
    isbn_entry.grid(row=0, column=1, padx=10, pady=5)

    titulo_label = tk.Label(adicionar_window, text="Título:")
    titulo_label.grid(row=1, column=0, padx=10, pady=5)
    global titulo_entry
    titulo_entry = tk.Entry(adicionar_window)
    titulo_entry.grid(row=1, column=1, padx=10, pady=5)

    autor_label = tk.Label(adicionar_window, text="Autor:")
    autor_label.grid(row=2, column=0, padx=10, pady=5)
    global autor_entry
    autor_entry = tk.Entry(adicionar_window)
    autor_entry.grid(row=2, column=1, padx=10, pady=5)

    genero_label = tk.Label(adicionar_window, text="Gênero:")
    genero_label.grid(row=3, column=0, padx=10, pady=5)
    global genero_entry
    genero_entry = tk.Entry(adicionar_window)
    genero_entry.grid(row=3, column=1, padx=10, pady=5)

    # Botão para adicionar livro
    adicionar_button = tk.Button(adicionar_window, text="Adicionar Livro", command=adicionar_livro)
    adicionar_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Inicializando o banco de dados
init_db()

# Configurando a janela principal
root = tk.Tk()
root.title("Biblioteca")
root.configure(bg="black")
root.geometry("600x400")

# Botão para adicionar livro
adicionar_button = tk.Button(root, text="Adicionar Livro", command=abrir_adicionar_livro)
adicionar_button.pack(padx=10, pady=5)

# Botão para visualizar livros
visualizar_button = tk.Button(root, text="Visualizar Livros")
visualizar_button.pack(padx=10, pady=5)

# Botão para buscar livro por ISBN
buscar_isbn_button = tk.Button(root, text="Buscar Livro por ISBN")
buscar_isbn_button.pack(padx=10, pady=5)

# Botão para buscar livro por título
buscar_titulo_button = tk.Button(root, text="Buscar Livro por Título")
buscar_titulo_button.pack(padx=10, pady=5)

# Botão para buscar livro por autor
buscar_autor_button = tk.Button(root, text="Buscar Livro por Autor")
buscar_autor_button.pack(padx=10, pady=5)

# Botão para buscar livro por gênero
buscar_genero_button = tk.Button(root, text="Buscar Livro por Gênero")
buscar_genero_button.pack(padx=10, pady=5)

# Botão para atualizar livro
atualizar_button = tk.Button(root, text="Atualizar Livro")
atualizar_button.pack(padx=10, pady=5)

# Botão para excluir livro
excluir_button = tk.Button(root, text="Excluir Livro")
excluir_button.pack(padx=10, pady=5)

# Botão para sair
sair_button = tk.Button(root, text="Sair", command=root.destroy)
sair_button.pack(padx=10, pady=5)

root.mainloop()