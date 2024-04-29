import re
#1)
# numeros=''
# ips=[]
# ip_invalido=[]
# with open(r'Exercicios_Diversos\A parte\ip.txt','r') as arquivo:
#     for i in arquivo:
#         ips.append(i.split())
#     padrao= r'\d+'
#     for i,ip in enumerate(ips):
#         ip=str(ip)
#         numeros=re.findall(padrao,ip)
#         for _, n in enumerate(numeros):
#                 n=int(n)
#                 print(n)
#                 if n>255:
#                     ip_invalido.append(ips.pop(i))
# with open(r'Exercicios_Diversos\A parte\ip_formatado.txt','w') as arquivo:
#     arquivo.write('IP VALIDO')
#     for i,_ in enumerate(ips):
#         arquivo.write(' '.join(ips[i])+'\n')
#     arquivo.write("\nIP INVALIDO\n")
#     for i,_ in enumerate(ips):
#         arquivo.write(' '.join(ip_invalido[i]) + '\n')

#2)

