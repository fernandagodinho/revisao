import random

# Função para simular lançamentos de dados
def lancar_dados(n_lancamentos):
    resultados = [0] * 6  # Vetor de contadores para os valores de 1 a 6
    for _ in range(n_lancamentos):
        resultado = random.randint(1, 6)
        resultados[resultado - 1] += 1
    return resultados

# Número de lançamentos
n_lancamentos = 100

# Simulação dos lançamentos
resultados = lancar_dados(n_lancamentos)

# Exibição dos resultados
print(f"Resultados dos {n_lancamentos} lançamentos de dados:")
for i, contagem in enumerate(resultados):
    print(f"Valor {i + 1}: {contagem} vezes")
