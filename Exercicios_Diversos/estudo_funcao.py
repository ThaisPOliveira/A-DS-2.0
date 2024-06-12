#1
# n=int(input("digige um valor"))
# def impressao(numero):
#     for i in range(1,numero+1):
#         print(f"{i}"*i)

# impressao(n)

#2nn conseguimos fazer tudo burro
# n=int(input("digige um valor"))
# def impressao(numero):
#     for i in range(1,numero+1):
#         print(f"{i}"i)
# impressao(n)

#3 Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
# lista=[]
# def soma():
#     for i in range(3):
#         somando=int(input("digite um valor"))
#         lista.append(somando)
#         somando2=sum(lista)
#     print(somando2)
# soma()

#4 Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
# def caractere():
#      numero=int(input("digite um numero"))
#      if numero <0:
#         print("numero negativo")
#      else:
#          print("numero positivo")
# caractere()

#5Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto
# # A função “altera” o valor de custo para incluir o imposto sobre vendas.
# def somaImposto():
#     custo=int(input("digite o custo"))
#     imposto=int(input("digite o valor do imposto"))
#     porcentagem=imposto/100
#     novo_valor = custo+ custo*porcentagem
#     print("novo valor é ",novo_valor)
# somaImposto()

#6

def reverte(letra):
    letra = list(letra)
    letra.reverse()
    print ("".join(letra))#join deixa junto
letra = input("digite ")
reverte(letra)
        
