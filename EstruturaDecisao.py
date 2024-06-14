#Universidade Mogi das Cruzes
#Thais Pereira de Oliveira
#Estrutura de Decisão - Exercicios

#1 Faça um Programa que peça dois números e imprima o maior dele
# n1=float(input("digite um numero"))
# n2=float(input("digite outro numero"))
# if n1>n2:
#   print(n1)
# else:
#   print(n2)
   
#2Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# numero=float(input("digite um numero"))
# if numero<0:
#     print("esse numero é negativo")
# elif numero>0:
#   print("esse numero é positivo")

#3Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
# letra = input("Digite uma letra: ")
# if letra == "F": 
#     print("Sexo feminino")
# elif letra == "M":
#     print("Sexo masculino")
# else:
#     print("Sexo Inválido")

#4Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# letra = input("Digite uma letra: ")
# if letra in ['a','e','i','o','u']: 
#     print("Essa letra é vogal")
# else:
#     print("Essa letra é consoante")

#5Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# m1=int(input("digite a primeira nota"))
# m2=int(input("digite a segunda nota"))
# soma = m1+m2
# media = soma/2
# if media >= 7 and media > 10:
#     print("aprovado")
# elif media < 7:
#     print("reprovado")
# elif media == 10:
#     print("aprovado com distinção")

#6 Faça um Programa que leia três números e mostre o maior deles.
# n1=int(input("digite o primeiro numero"))
# n2=int(input("digite o segundo numero"))
# n3=int(input("digite o terceiro numero"))
# if n1>=n2 and n1>=n3:
#     maior=n1
# if n2>=n1 and n2>=n3:
#     maior=n2
# else:
#     maior=n3
# print("o maior numero é:", maior)
    
#7Faça um Programa que leia três números e mostre o maior e o menor deles.
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# if n1 <= n2 and n1 <= n3:
#     menor = n1
# elif n2 <= n1 and n2 <= n3:
#     menor = n2
# else:
#     menor = n3

# if n1>=n2 and n1>=n3:
#     maior=n1
# if n2>=n1 and n2>=n3:
#     maior=n2
# else:
#     maior=n3

# print("o maior numero é:", maior)
# print("O menor número é:", menor)

# 8Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = int(input("Digite o valor do primeiro produto: "))
prod2 = int(input("Digite o valor do segundo produto: "))
prod3 = int(input("Digite o valor do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    produto_mais_barato = prod1
    menor_preco = prod1
elif prod2 < prod1 and prod2 < prod3:
    produto_mais_barato = prod2
    menor_preco = prod2
else:
    produto_mais_barato = prod3
    menor_preco = prod3

print(f"Você deve comprar o produto {produto_mais_barato}, que custa R${menor_preco}")
