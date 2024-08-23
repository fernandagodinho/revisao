# Função para calcular o número de anos necessários
def calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0
    while populacao_a <= populacao_b:
        populacao_a += populacao_a * (taxa_crescimento_a / 100)
        populacao_b += populacao_b * (taxa_crescimento_b / 100)
        anos += 1
    return anos

# Populações iniciais e taxas de crescimento
populacao_a = 80000
taxa_crescimento_a = 3.0
populacao_b = 200000
taxa_crescimento_b = 1.5

# Cálculo do número de anos
anos_necessarios = calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)

# Exibição do resultado
print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.")
