#Universidade Mogi das Cruzes
#Thais Pereira de Oliveira
#Estrutura Função - Exercicios

# #1
# def imprimir_padrao(n):
#     for i in range(1, n + 1):
#         linha = " ".join(str(i) for _ in range(i))
#         print(linha)

# n = int(input("Digite um número inteiro: "))

# imprimir_padrao(n)

#2
opcao=0
while opcao!= 5:
 def calculadora():
    opcao=int(input("digite uma oção ou 5 para finalizar"
                    "1-soma"
                    "2-subtração"
                    "3-multiplicação"
                    "4-divisão"
                    "5-sair"))
    if opcao==1:
      n1=int(input("digite o primeiro numero"))
      n2=int(input("digite o segundo numero"))
      soma=n1+n2
      print("a soma dos dois numeros é", soma)
    elif opcao==2:
      n1=int(input("digite o primeiro numero"))
      n2=int(input("digite o segundo numero"))
      subtracao=n1-n2
      print("a subtracao dos dois numeros é", subtracao)
    elif opcao==3:
      n1=int(input("digite o primeiro numero"))
      n2=int(input("digite o segundo numero"))
      multiplicação=n1*n2
      print("a multiplicação dos dois numeros é", multiplicação)
    elif opcao==4:
      n1=int(input("digite o primeiro numero"))
      n2=int(input("digite o segundo numero"))
      divisao=n1/n2
      print("a divisao dos dois numeros é", divisao)
    return opcao 
 
while opcao != 5:
    opcao = calculadora()

       