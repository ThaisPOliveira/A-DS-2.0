#Universidade Mogi das Cruzes
#Thais Pereira de Oliveira
#Lista(Discionario) - Exercicios

#1 Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
# numeros=[]
# for i in range(5):
#     numero=int(input(f"digite um numero{i+1}:"))
#     numeros.append(numero)
# print("os numeros digitados foram:", numeros)

#2Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
# numeros = []
# for i in range(10):
#     numero = float(input(f"Digite o número {i+1}: "))
#     numeros.append(numero)
# numeros.reverse()
# print("Números na ordem inversa:", numeros)

#3 Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
# notas =[]
# for i in range(4):
#     nota=int(input(f"digite sua {i+1} nota:"))
#     notas.append(nota)
#     soma=sum(notas)
#     quantidade=len(notas)
#     media=soma  /quantidade
     
# print("a media das suas notas é:", media)
    
#4 Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes
# consoante = []

# for i in range(10):
#     letra = input(f"Digite uma letra {i+1}: ")
#     consoante.append(letra) #o comando append é usado para adicionar um elemento ao final de uma lista. 
    #   Ele modifica a lista original, acrescentando o elemento fornecido ao final dela. 

# consoantes_filtradas = [letra for letra in consoante if letra not in ['a', 'e', 'i', 'o', 'u']]
# print("Consoantes lidas:", consoantes_filtradas)

#5Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

# Numeros=[]
# Pares=[]
# Impares=[]

# for i in range[20]:
#    numero=int(input(f"digite uma letra{i+1}:"))
#    Numeros.append(numero)
#    if numero %2 == 0:
#       Pares.append(numero)
#    else:
#     Impares.append(numero)

# print("vetor de todos os numeros:", Numeros)
# print("vetor de todos os numeros pares:", Pares )
# print("vetor de todos os numeros:", Impares)

#6 Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
# Alunos=[]
# Medias=[]

# for i in range(10):
#     n1=int(input(f"digite a nota 1 do aluno {i+1}:"))
#     n2=int(input(f"digite a nota 2 do aluno {i+1}:"))
#     n3=int(input(f"digite a nota 3 do aluno {i+1}:"))
#     n4=int(input(f"digite a nota 4 do aluno {i+1}:"))
#     Alunos.append([n1,n2,n3,n4]) #armazenando a nota dos alunos com uma sublista

# Media=(n1+n2+n3+n4)/4
# Medias.append(Media)

# Contador=0 #conta o numero de alunos com a media 7
# for media in Medias:
#     if media >= 7.0:
#         Contador+=1

# print("numero de alunos com a media maior ou igual a 7.0:", Contador)


#7 Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
# Numero=[]
# soma=[]
# multiplicação=[]
# for i in range(5):
#     n=int(input(f"digite um numero{i+1}:")) 
#     Numero.append(n)

# soma=sum(Numero)
# multiplicação = 1
# for num in Numero:
#     multiplicação *= num

# print("numeros", Numero)
# print("soma dos numeros", soma)
# print("multiplicação dos numeros", multiplicação)

#8 Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
# Idades=[]
# Alturas=[]
# for i in range(5):
#   idade=int(input(f"digite a idade da {i+1} pessoa :"))
#   Idades.append(idade)
#   altura=float(input(f"digite a altura da {i+1} pessoa"))
#   Alturas.append(altura) 
 
  
# print("a altura das cinco pessoas em ordem inversa", Alturas[::-1])
# print("a idade das cinco pessoas em ordem inversa:", Idades[::-1])
