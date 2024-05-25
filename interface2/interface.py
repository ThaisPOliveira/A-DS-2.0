from tkinter import *
janela=Tk()

janela.title("Sistema Bancario")
janela.geometry('620x400')

tit= Label(janela, text="SISTEMA BANCARIO")
tit= Label(janela, text="Selecione a opção desejada")
tit.place(x=215, y=30)
tit["font"] = ("blue","10","italic","bold")
tit["fg"]=("black")
tit["bg"]=("white")

# image= Image.open("reet.jpg")
# resize_image= image.resize((200,100))
# img = ImageTk.PhotoImage(resize_image)
# logo = label(image=img)
# logo.image = img
# logo.place(x=380, y=330)


# Cadastro=Button(janela, text="cadastrar"
#) #tenho que terminar
# Login=Button(janela, text="login") #tenho que terminar

Sair=Button(janela, text="sair",
command=janela.destroy, width=30)
Sair.place(x=380, y=330)


janela.mainloop()


