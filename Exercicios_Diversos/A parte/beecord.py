import re
#binario

# num1=input("digite um numero ")
# padrao= r'\d+'
# soma1=0
# numeros=re.findall(padrao,num1)
# for i in range(len(numeros)):
#     soma1+=int(numeros[i])
# lista=[]
# bi={0:1,
#     1:2,
#     2:4,
#     3:8,
#     4:16,
#     5:32,
#     6:64,
#     7:128
#     }
# binario=str(soma1)[::-1]
# soma=0
# for i in range(len(binario)):
#     lista.append(int(binario[i])) 
#     if lista[i]==1:
#         soma+=bi[i]
#     elif lista[i]>1:
#         for i in range(len(numeros)):
#             soma+=int(numeros[i])
#         break
# print(f"resultado de {num1} = {soma}")

#melhorar o codigo
# soma=0
# soma2=0
# binario=1
# def verifica_binario(binar):
#     binar=list(binar)
#     for i,num in enumerate(list(binar)):
#         if num=='1' or num=='0':
#             pass
#         else:
#             return False
#     return True
# num1=input("")
# padrao= r'\d+'
# numeros=re.findall(padrao,num1)

# for i in range(len(numeros)):
#     soma+=int(numeros[i])

# binar=str(soma)[::-1]
# if verifica_binario(binar):
#     for i, num in enumerate(list(binar)):
#         if num=='1':
#             soma2+=binario
#             binario*=2
#         elif num=='0':
#             binario*=2
# else:
#     soma2=soma
# print(soma2)

#nao entendi bulhufas desse 
#ENTENDI
# ^ soma os valores binarios do numero, caso a casa binaria de ambos retornem True(1) reescreve como false(0)
# 5(00000101) + 3(00000011) = 8(00000110)
# while True:
#     try:
#         a, b = [int(x) for x in input().strip().split(' ')]
#         print(a ^ b)
#     except EOFError:
#         break

#xadrez

# n=int(input(""))
# xadrez=n*n
# branco,preto=0,0
# if 2<=n<=100:
#     for i in range(0,xadrez):
#         if i%2==0:
#             branco+=1
#         else:
#             preto+=1
#     print(f"{branco} casas brancas e {preto} casas pretas")

#AOT

# n, x = [int(x) for x in input().strip().split(' ')]
# t = input("")
# print(n,x)

#numero extenso

x=int(input(""))
s=(int(str(x)[:1])-2)
numeros1=["one ","two","three","four","five","six","seven","eight","nine","ten","eleven","Twelve","Thirteen","Fourteen","Fifteen","sixteen","seventeen","eighteen","nineteen"]
numeros2=["twenty ","tirty ","fourty ","fifty ","sixty ","seventy ","eighty ","ninety "]
if 1<=x<=100:
    if x<=19:
        palavra=numeros1[x-1]
    elif str(x)[1:]=='0':
        palavra=numeros2[s].strip()
    elif x==100:
        palavra="one hundred"
    else:
        palavra=numeros2[s]+numeros1[int(str(x)[1:])-1]
print(palavra,len(palavra))