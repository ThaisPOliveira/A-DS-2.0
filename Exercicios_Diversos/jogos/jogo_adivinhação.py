import random 

def jogo_adivinhacao():
    numero_secreto = random.randint(1,10)
    tentativas = 0
    while True:
        palpite = int(input("Digite um numero de 1 a 10: "))
        tentativas+= 1
        if palpite == numero_secreto:
            print(f"Voce acertou o numero secreto em {numero_secreto} em tantas {tentativas} tentativas.")
            break
        elif abs(palpite - numero_secreto) <=10:
            print("Quente")
        else:
            print("Frio")

jogo_adivinhacao()