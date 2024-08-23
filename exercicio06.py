# Função para calcular o número de anos necessários
def calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b):
    anos = 0
    while populacao_a <= populacao_b:
        populacao_a += populacao_a * (taxa_crescimento_a / 100)
        populacao_b += populacao_b * (taxa_crescimento_b / 100)
        anos += 1
    return anos

# Função para validar a entrada do usuário
def validar_entrada(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Loop principal para repetir a operação
while True:
    # Entrada de dados do usuário
    populacao_a = validar_entrada("Digite a população inicial do país A: ")
    taxa_crescimento_a = validar_entrada("Digite a taxa de crescimento anual do país A (%): ")
    populacao_b = validar_entrada("Digite a população inicial do país B: ")
    taxa_crescimento_b = validar_entrada("Digite a taxa de crescimento anual do país B (%): ")

    # Cálculo do número de anos
    anos_necessarios = calcular_anos(populacao_a, taxa_crescimento_a, populacao_b, taxa_crescimento_b)

    # Exibição do resultado
    print(f"\nSerão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou iguale a população do país B.\n")

    # Perguntar ao usuário se deseja repetir a operação
    repetir = input("Deseja calcular novamente? (s/n): ").strip().lower()
    if repetir != 's':
        break
