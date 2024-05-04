#UNIVERSIDADE MOGI DAS CRUZES



import random
import os
os.system("cls")

numero=random.randint(1,100)
tentativa=0
while tentativa != numero:
    print("JOGO DE ADVINHAÇÃO, DE 1 a 100")
    tentativa=int(input("advinhe o numero: "))
    if tentativa < numero:
        if numero - tentativa >=7:
            print("quase la em")
        print("palpite baixo")
    elif tentativa > numero:
        if tentativa - numero <=7:
            print("quase la em")
        print("palpite alto")
print("voce ganhou!!!")

