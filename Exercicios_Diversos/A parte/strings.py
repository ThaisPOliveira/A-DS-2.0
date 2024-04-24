import datetime, locale
#1)
# string1=input("digite ")
# string2=input("digite ")
# tamanho1=len(string1)
# tamanho2=len(string2)
# print(f"tamanho de {string1} = {tamanho1} caracteres")
# print(f"tamanho de {string2} = {tamanho2} caracteres")
# if tamanho1 ==  tamanho2:
#     print("tem o mesmo tamanho")
# else:
#     print("nao tem")
# if string1==string2:
#     print("sao iguais")

#2)
# nome=input("digite nome ")
# print(f"{nome.upper()[::-1]}")

#3)
# nome=input("digite nome ")
# for i in list(nome):
#     print (i)

#4)
# nome=input("digite nome ")
# for i in range(len(nome)+1):
#     print (f"{nome[:i]}")

#5)
# nome=input("digite nome ")
# for i in range(len(nome)+1):
#     print (f"{nome[i:]}")

#6)
# locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
# dia=int(input("digite dia"))
# mes=int(input("digite mes"))
# ano=int(input("digite ano"))
# data=datetime.datetime(ano,mes,dia)
# print(data.strftime("%d/%B/%Y"))

#7)
# espacos=0
# vogais=0
# frase=input("digite uma frase ")
# lista=list(frase)
# for i in lista:
#     if i in ['a','e','i','o','u']:
#         vogais+=1
#     if i==" ":
#         espacos+=1
# print(f'tem {espacos} espacos {vogais} vogais')

#8)
# frase=input("digite uma frase ")
# frase2=""
# lista=list(frase)
# for i in lista:
#     if i==" ":
#         lista.remove(i)
# if lista == lista[::-1]:
#     print(f"{frase} é um palindromo")
# else:
#     print(f"{frase} não é um palindromo")

#9)

# cpf=input('digite cpf no exato formato "xxx.xxx.xxx-xx"')
# cpf=list(cpf)
# if len(cpf)<14:
#     print("falta caracteres")
# if len(cpf)>14:
#     print("ultrapassou os caracteres")
# else:
#     if cpf[3]!="." and cpf[7]!="." and cpf[11]!=".":
#         print("coloque os pontos")

#10)