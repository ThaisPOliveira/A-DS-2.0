import os
import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
 
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
    isbn = simpledialog.askstring("Adicionar Livro", "Digite o ISBN-13, somente números (13 dígitos):")
    if not isbn or len(isbn) != 13 or not isbn.isdigit():
        messagebox.showerror("Erro", "ISBN inválido! Deve ter 13 dígitos.")
        return
 
    titulo = simpledialog.askstring("Adicionar Livro", "Digite o título:")
    autor = simpledialog.askstring("Adicionar Livro", "Digite o autor:")
    genero = simpledialog.askstring("Adicionar Livro", "Digite o gênero:")
 
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
 
# Função para visualizar todos os livros
def visualizar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    conn.close()
 
    if not livros:
        messagebox.showinfo("Visualizar Livros", "Nenhum livro cadastrado.")
        return
 
    livros_str = "\n".join([f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}" for livro in livros])
    messagebox.showinfo("Lista de Livros", livros_str)
 
# Função para buscar um livro por ISBN
def buscar_livro_isbn():
    isbn = simpledialog.askstring("Buscar Livro por ISBN", "Digite o ISBN:")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()
    conn.close()
 
    if livro:
        messagebox.showinfo("Buscar Livro por ISBN", f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}")
    else:
        messagebox.showerror("Erro", "ISBN não encontrado.")
 
# Função para buscar um livro por título
def buscar_livro_titulo():
    titulo = simpledialog.askstring("Buscar Livro por Título", "Digite o título:") + "%"
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE titulo LIKE ?', (titulo,))
    livros = cursor.fetchall()
    conn.close()
 
    if livros:
        livros_str = "\n".join([f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}" for livro in livros])
        messagebox.showinfo("Buscar Livro por Título", livros_str)
    else:
        messagebox.showerror("Erro", "Livro não encontrado.")
 
# Função para buscar um livro por autor
def buscar_livro_autor():
    autor = simpledialog.askstring("Buscar Livro por Autor", "Digite o autor:") + "%"
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor LIKE ?', (autor,))
    livros = cursor.fetchall()
    conn.close()
 
    if livros:
        livros_str = "\n".join([f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}" for livro in livros])
        messagebox.showinfo("Buscar Livro por Autor", livros_str)
    else:
        messagebox.showerror("Erro", "Autor não encontrado.")
 
# Função para buscar um livro por gênero
def buscar_livro_genero():
    genero = simpledialog.askstring("Buscar Livro por Gênero", "Digite o gênero:") + "%"
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE genero LIKE ?', (genero,))
    livros = cursor.fetchall()
    conn.close()
 
    if livros:
        livros_str = "\n".join([f"ISBN: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}" for livro in livros])
        messagebox.showinfo("Buscar Livro por Gênero", livros_str)
    else:
        messagebox.showerror("Erro", "Nenhum livro corresponde a esse gênero.")
 
# Função para atualizar um livro
def atualizar_livro():
    isbn = simpledialog.askstring("Atualizar Livro", "Digite o ISBN do livro que deseja atualizar:")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()
 
    if not livro:
        messagebox.showerror("Erro", "Livro não encontrado.")
        conn.close()
        return
 
    titulo = simpledialog.askstring("Atualizar Livro", f"Digite o novo título (atual: {livro[1]}):")
    autor = simpledialog.askstring("Atualizar Livro", f"Digite o novo autor (atual: {livro[2]}):")
    genero = simpledialog.askstring("Atualizar Livro", f"Digite o novo gênero (atual: {livro[3]}):")
 
    if titulo:
        cursor.execute('UPDATE livros SET titulo = ? WHERE isbn = ?', (titulo, isbn))
    if autor:
        cursor.execute('UPDATE livros SET autor = ? WHERE isbn = ?', (autor, isbn))
    if genero:
        cursor.execute('UPDATE livros SET genero = ? WHERE isbn = ?', (genero, isbn))
 
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Livro atualizado com sucesso!")
 
# Função para excluir um livro
def excluir_livro():
    isbn = simpledialog.askstring("Excluir Livro", "Digite o ISBN do livro que deseja excluir:")
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE isbn = ?', (isbn,))
    livro = cursor.fetchone()
 
    if livro:
        if messagebox.askyesno("Confirmação", f"Tem certeza que deseja deletar o livro?\n\nTítulo: {livro[1]}\nAutor: {livro[2]}\nGênero: {livro[3]}"):
            cursor.execute('DELETE FROM livros WHERE isbn = ?', (isbn,))
            conn.commit()
            messagebox.showinfo("Sucesso", "Livro excluído com sucesso!")
        else:
            messagebox.showinfo("Cancelado", "Exclusão cancelada.")
    else:
        messagebox.showerror("Erro", "Livro não encontrado.")
 
    conn.close()
 
# Função para excluir todos os livros
def excluir_todos_os_livros():
    if messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar todos os livros?"):
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM livros')
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Todos os livros foram excluídos com sucesso!")
 
# Função principal para o menu
def menu():
    init_db()
 
    def adicionar():
        adicionar_livro()
 
    def visualizar():
        visualizar_livros()
 
    def buscar_isbn():
        buscar_livro_isbn()
 
    def buscar_titulo():
        buscar_livro_titulo()
 
    def buscar_autor():
        buscar_livro_autor()
 
    def buscar_genero():
        buscar_livro_genero()
 
    def atualizar():
        atualizar_livro()
 
    def excluir():
        excluir_livro()
 
    def excluir_todos():
        excluir_todos_os_livros()
 
    def sair():
        root.destroy()
 
    root = tk.Tk()
    root.title("Biblioteca")
    root.geometry("400x600")
 
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(expand=True, fill='both')
 
    title_label = tk.Label(main_frame, text="Sistema de Biblioteca", font=("Helvetica", 16))
    title_label.pack(pady=10)
 
    button_frame = tk.Frame(main_frame)
    button_frame.pack(pady=10)
 
    buttons = [
        ("Adicionar Livro", adicionar),
        ("Visualizar Livros", visualizar),
        ("Buscar Livro por ISBN", buscar_isbn),
        ("Buscar Livro por Título", buscar_titulo),
        ("Buscar Livro por Autor", buscar_autor),
        ("Buscar Livro por Gênero", buscar_genero),
        ("Atualizar Livro", atualizar),
        ("Excluir Livro", excluir),
        ("Excluir Todos os Livros", excluir_todos),
        ("Sair", sair)
    ]
 
    for i, (text, command) in enumerate(buttons):
        button = tk.Button(button_frame, text=text, command=command, font=("Helvetica", 12), pady=5)
        button.grid(row=i, column=0, sticky="ew", pady=5)
 
    root.mainloop()
 
# Exibe o título em ASCII e inicia o menu
menu()
