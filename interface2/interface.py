from tkinter import *

def exibir_mensagem(texto_mensagem, mensagem):
    texto_mensagem.insert(END, mensagem + '\n')
    texto_mensagem.see(END)

def tela_cadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.title("Tela de Cadastro")
    janela_cadastro.geometry('620x400')
    janela_cadastro.config(bg='gray')
    
    Label(janela_cadastro, text="CPF:", bg='gray', fg='black').grid(row=0, column=0, padx=10, pady=10)
    Entry(janela_cadastro).grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_cadastro, text="Senha:", bg='gray', fg='black').grid(row=2, column=0, padx=10, pady=10)
    Entry(janela_cadastro, show="*").grid(row=2, column=1, padx=10, pady=10)
    
    Button(janela_cadastro, text="Cadastrar", command=lambda: exibir_mensagem(caixa_mensagem, "Cadastro realizado!")).grid(row=3, columnspan=2, pady=10)
    
    caixa_mensagem = Text(janela_cadastro, width=50, height=10)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

def abrir_menu():
    janela_menu = Toplevel()
    janela_menu.title("Menu")
    janela_menu.geometry('620x400')
    janela_menu.config(bg='gray')

    caixa_mensagem = Text(janela_menu, width=50, height=10)
    caixa_mensagem.grid(row=3, columnspan=2, padx=10, pady=10)

    Button(janela_menu, width=50, text="Extrato", command=lambda: exibir_mensagem(caixa_mensagem, "Extrato da conta")).grid(row=0, columnspan=2, pady=10)
    Button(janela_menu, width=50, text="Saque", command=lambda: exibir_mensagem(caixa_mensagem, "Saque realizado no valor de:")).grid(row=1, columnspan=2, pady=10)
    Button(janela_menu, width=50, text="Deposito", command=lambda: exibir_mensagem(caixa_mensagem, "Deposito realizado")).grid(row=2, columnspan=2, pady=10)

def tela_login():
    janela_login = Toplevel()
    janela_login.title("Tela de Login")
    janela_login.geometry('620x400')
    janela_login.config(bg='gray')
    
    Label(janela_login, text="CPF:", bg='gray', fg='black').grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(janela_login)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_login, text="Senha:", bg='gray', fg='black').grid(row=1, column=0, padx=10, pady=10)
    senha_entry = Entry(janela_login, show="*")
    senha_entry.grid(row=1, column=1, padx=10, pady=10)
    
    def login_e_abrir_menu():
        exibir_mensagem(caixa_mensagem, "Login realizado!")
        janela_login.after(2000, abrir_menu)
    
    Button(janela_login, text="Login", command=login_e_abrir_menu).grid(row=2, columnspan=2, pady=10)
    
    caixa_mensagem = Text(janela_login, width=50, height=10)
    caixa_mensagem.grid(row=4, columnspan=2, padx=10, pady=10)

janela_principal = Tk()
janela_principal.title("Sistema Bancário")
janela_principal.geometry('620x400')
janela_principal.config(bg='gray')

titulo1 = Label(janela_principal, text="SISTEMA BANCÁRIO", font=("Helvetica", 16, "italic", "bold"), fg="black", bg="gray")
titulo1.place(x=215, y=10)

titulo2 = Label(janela_principal, text="Selecione a opção desejada", font=("Helvetica", 10, "bold"), fg="black", bg="gray")
titulo2.place(x=220, y=50)

botao_cadastro = Button(janela_principal, text="Cadastrar", command=tela_cadastro, width=30)
botao_cadastro.place(x=200, y=100)

botao_login = Button(janela_principal, text="Login", command=tela_login, width=30)
botao_login.place(x=200, y=150)

botao_sair = Button(janela_principal, text="Sair", command=janela_principal.destroy, width=30)
botao_sair.place(x=200, y=200)


janela_principal.mainloop()
