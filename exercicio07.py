# Função para gerar a série de Fibonacci até o n-ésimo termo
def fibonacci(n):
    serie = [0, 1]
    while len(serie) < n:
        proximo_termo = serie[-1] + serie[-2]
        serie.append(proximo_termo)
    return serie[:n]

# Entrada de dados
n = int(input("Digite o valor de n para gerar a série de Fibonacci: "))

# Geração da série de Fibonacci
serie_fibonacci = fibonacci(n)

# Exibição dos resultados
print(f"Série de Fibonacci até o {n}-ésimo termo: {serie_fibonacci}")
