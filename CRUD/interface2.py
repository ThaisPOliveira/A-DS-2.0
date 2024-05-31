from tkinter import Tk, Label, Button, Entry
import CRUD as crud




def principal():
    global janela_principal
    janela_principal = Tk()
    janela_principal.title("Sistema Bancário")
    janela_principal.geometry('620x400')
    janela_principal.config(bg='black')

    titulo1 = Label(janela_principal, text="SISTEMA BANCÁRIO", font=("Helvetica", 16, "italic", "bold"), fg="blue", bg="black")
    titulo1.place(x=215, y=10)

    titulo2 = Label(janela_principal, text="Selecione a opção desejada", font=("Helvetica", 10, "bold"), fg="blue", bg="black")
    titulo2.place(x=220, y=50)

    botao_cadastro = Button(janela_principal, text="Cadastrar", command=tela_cadastro, width=30)
    botao_cadastro.place(x=200, y=100)

    botao_login = Button(janela_principal, text="Login", command=tela_login,  width=30)
    botao_login.place(x=200, y=150)

    botao_sair = Button(janela_principal, text="Sair", width=30, command=janela_principal.quit)
    botao_sair.place(x=200, y=200)

    janela_principal.mainloop()

def tela_cadastro():
    global janela
    janela = Tk()

    janela.title("Tela de Cadastro")
    janela.geometry('620x400')
    janela.config(bg='gray')
    
    Label(janela, text="CPF:", bg='gray', fg='black').grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(janela)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela, text="Nome de usuário:", bg='gray', fg='black').grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(janela)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela, text="Senha:", bg='gray', fg='black').grid(row=2, column=0, padx=10, pady=10)
    password_entry = Entry(janela, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    Button(janela, text="Voltar", command=voltar).grid(row=3, columnspan=2, pady=10)
    print(crud.Cadastro_usuario(cpf_entry,username_entry,password_entry))
    janela_principal.withdraw()  # Oculta a janela principal

def tela_login():
    global janela
    janela = Tk()

    janela.title("Tela de login")
    janela.geometry('620x400')
    janela.config(bg='gray')
    
    Label(janela, text="CPF:", bg='gray', fg='black').grid(row=0, column=0, padx=10, pady=10)
    cpf_entry = Entry(janela)
    cpf_entry.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela, text="Nome de usuário:", bg='gray', fg='black').grid(row=1, column=0, padx=10, pady=10)
    username_entry = Entry(janela)
    username_entry.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela, text="Senha:", bg='gray', fg='black').grid(row=2, column=0, padx=10, pady=10)
    password_entry = Entry(janela, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=10)
    Button(janela, text="Voltar", command=voltar).grid(row=3, columnspan=2, pady=10)

    janela_principal.withdraw()  # Oculta a janela principal
def voltar():
    janela.destroy()
    janela_principal.deiconify()  # Restaura a janela principal

principal()
