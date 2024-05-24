#Universidade Mogi das Cruzes
#Atividade Função 19/05
#Thais Pereira de Oliveira
#Erick Fernando Martins


# def horario():
#     opc=1
#     while opc != 0:
#         escolha=int(input("digite o horario que deseja converter "))
#         minutos=int(input("digite os minutos "))
#         if escolha==24:
#             hora=int(input("Digite o horario em 24 horas "))  
#             if hora>12:
#                 hora-=12 
#             print(f"o horario em 24, em 12 horas é {hora}:{minutos}")
#         elif escolha==12:
#             hora=int(input("Digite o horario em 12 horas "))
#             am=input("1 para AM, 2 para PM")
#             if hora<12 and am==2:
#                 hora+=12 
#             print(f"o horario em 12, em 24 horas é {hora}:{minutos}")
#         opc=int(input("Digite 0 para encerrar"))
# horario() 
prestacoespagas=[]
def pagas(valores):
    for i in range(len(valores)):
        if valores[i][4]=="s":
            prestacoespagas.append(valores[i])
    print("contas pagas ")
    for i in range(len(prestacoespagas)):
        print(f"R${prestacoespagas[i][5]:.2f}")

def conta():
    opc=1
    valores=[]
    while opc != 0:
        prestação=int(input("digite o valor da conta a ser paga ou digite 0 para encerrar o programa "))
        if prestação==0:
           break       
        paga=input("esssa conta já foi paga?S/N ").lower()
        dias=int(input("digite os dias em atraso "))   
        juros=prestação*(0.001 * dias)
        atraso=prestação*(0.03 * dias)
        total= prestação+juros+atraso
        print("o valor da prestação com juros e atrasos a ser paga é R$", total)
        extrato=[prestação,dias,juros,atraso,paga,total]
        valores.append(extrato)
        print(f"valor total R$ {total:.2f}")
        print(f"valor inicial R${prestação:.2f}")
        print(f"{dias} dias de atraso")
        print(f"juros pagos R${juros:.2f}")
        print("essa conta já foi paga? ", paga)

    return pagas(valores)

prestacoespagas=conta()





