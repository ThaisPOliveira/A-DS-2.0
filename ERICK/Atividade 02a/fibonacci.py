fibonnaci=int(input("digite o ultimo numero da sequência de fibonnaci desejada "))
anterior, proximo=1,1
print("1º termo = ",anterior,"\n2º termo = ",proximo)
contador=3
for i in range(fibonnaci-2):
    proximo+=anterior  
    print(f"{contador}º termo = {proximo}")
    anterior=proximo-anterior
    contador+=1