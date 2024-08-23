import random

# Função para lançar os dados
def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1 + dado2

# Função para jogar Craps
def jogar_craps():
    print("Bem-vindo ao jogo de Craps!")
    
    # Primeira jogada
    resultado = lancar_dados()
    print(f"Você tirou {resultado} na primeira jogada.")
    
    if resultado in [7, 11]:
        print("Você tirou um 'natural' e ganhou!")
    elif resultado in [2, 3, 12]:
        print("Você tirou 'craps' e perdeu!")
    else:
        ponto = resultado
        print(f"Seu 'Ponto' é {ponto}. Continue jogando até tirar {ponto} novamente, mas cuidado com o 7!")
        
        while True:
            resultado = lancar_dados()
            print(f"Você tirou {resultado}.")
            
            if resultado == ponto:
                print("Você tirou seu 'Ponto' novamente e ganhou!")
                break
            elif resultado == 7:
                print("Você tirou 7 e perdeu!")
                break

# Iniciar o jogo
jogar_craps()
