from itertools import permutations

# Função para verificar se uma combinação é um quadrado mágico
def eh_quadrado_magico(combinacao):
    # Converte a combinação em uma matriz 3x3
    matriz = [combinacao[:3], combinacao[3:6], combinacao[6:]]
    
    # Soma das linhas
    soma_linha1 = sum(matriz[0])
    soma_linha2 = sum(matriz[1])
    soma_linha3 = sum(matriz[2])
    
    # Soma das colunas
    soma_coluna1 = matriz[0][0] + matriz[1][0] + matriz[2][0]
    soma_coluna2 = matriz[0][1] + matriz[1][1] + matriz[2][1]
    soma_coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
    
    # Soma das diagonais
    soma_diagonal1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
    soma_diagonal2 = matriz[0][2] + matriz[1][1] + matriz[2][0]
    
    # Verifica se todas as somas são iguais
    return (soma_linha1 == soma_linha2 == soma_linha3 == 
            soma_coluna1 == soma_coluna2 == soma_coluna3 == 
            soma_diagonal1 == soma_diagonal2)

# Função para encontrar todos os quadrados mágicos
def encontrar_quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    quadrados_magicos = []
    
    for combinacao in permutations(numeros):
        if eh_quadrado_magico(combinacao):
            quadrados_magicos.append(combinacao)
    
    return quadrados_magicos

# Função para exibir um quadrado mágico
def exibir_quadrado_magico(quadrado):
    for i in range(0, 9, 3):
        print(quadrado[i], quadrado[i+1], quadrado[i+2])
    print()

# Encontrar e exibir todos os quadrados mágicos
quadrados_magicos = encontrar_quadrados_magicos()
print(f"Encontrados {len(quadrados_magicos)} quadrados mágicos de lado 3:")
for quadrado in quadrados_magicos:
    exibir_quadrado_magico(quadrado)
