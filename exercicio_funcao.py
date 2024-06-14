#Universidade Mogi das Cruzes
#Nome: Thais Pereira de Oliveira
#Exercicio de fixacao Python - Funç~sp#n1=0 #inicializador
#n2=0
#def Somando(n1,n2): #parametro
  #n1=int(input("digite um numero"))
  #n2=int(input("digite um numero"))
  #soma=n1+n2
  #print("a soma dos dois numeros é igual a", soma)
#Somando(n1,n2)
 
#2
#n=0 #inicializador
#def Tabuada(numero): #parametro
    #n=int(input("digite um numero"))
#for i in range(1,11):
      #resultado=i*n
      #print("a tabuada é",resultado)
#Tabuada(n)
 
#3
lista=(1,2,3,4,5,6,7,8,9,10)
def Soma(lista):
    soma=sum(lista)
    media = soma / len(lista)
    return (media, soma)
print("a soma da lista é", Soma (lista[1]))
print("a media da lista é", Soma (lista[0]))
Soma(lista)

