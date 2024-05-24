import random
with open(r"Exercicios_Diversos\jogos\forca.txt", "r") as forca:
    palavras = [linha.strip() for linha in forca]

palavra = random.choice(palavras)
qtd = len(palavra)
palavra3 = palavra[:]
palavra2 = ['_'] * len(palavra)

cont = 5
while palavra3 and cont > 0:
    tentativa = input(f"adivinhe uma letra {' '.join(palavra2)}: ")
    
    if tentativa in palavra:
        indices = [i for i, letra in enumerate(palavra) if letra == tentativa]
        for index in indices:
            palavra2[index] = tentativa
        palavra3 = palavra3.replace(tentativa, '_')
        print(''.join(palavra2))
    else:
        cont -= 1
        print(f"Você tem {cont} tentativas restantes.")

if cont > 0:
    print("Você ganhou!!")
else:
    print(f"Game over! A palavra era: {palavra}")
