import random

def jogo_pedra_papel_tesoura():
    ponto=0
    pontopc=0
    opcoes = ["pedra", "papel", "tesoura"]
    while True:
        if pontopc==2 or ponto==2:
            break
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar): ").lower()
        if jogador == "sair":
            print("Obrigado por jogar!")
            break
        elif jogador not in opcoes:
            print("Opção inválida. Escolha entre pedra, papel ou tesoura.")
            continue
        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")
        if jogador == computador:
            print("Empate!")
        elif (jogador == "pedra" and computador == "tesoura") or \
             (jogador == "papel" and computador == "pedra") or \
             (jogador == "tesoura" and computador == "papel"):
            ponto+=1
            print(f"Você ganhou um ponto! {ponto} x {pontopc}")
        
        else:
            pontopc+=1
            print(f"Computador ganhou um ponto! {ponto} x {pontopc}")
 
jogo_pedra_papel_tesoura()