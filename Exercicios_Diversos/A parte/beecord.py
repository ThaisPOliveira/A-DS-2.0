#binario

num1=input("digite um numero ")
padrao= r'\d+'
soma1=0
numeros=re.findall(padrao,num1)
for i in range(len(numeros)):
    soma1+=int(numeros[i])
lista=[]
bi={0:1,
    1:2,
    2:4,
    3:8,
    4:16,
    5:32,
    6:64,
    7:128
    }
binario=str(soma1)[::-1]
soma=0
for i in range(len(binario)):
    lista.append(int(binario[i])) 
    if lista[i]==1:
        soma+=bi[i]
    elif lista[i]>1:
        for i in range(len(numeros)):
            soma+=int(numeros[i])
        break
print(f"resultado de {num1} +  = {soma}")