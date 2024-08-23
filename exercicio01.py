# Função para calcular excesso e multa
def calcular_multa(peso):
    limite = 50  
    multa_por_quilo = 4.00
    if peso > limite:
        excesso = peso - limite
        multa = excesso * multa_por_quilo
    else:
        excesso = 0
        multa = 0
    
    return excesso, multa

# Entrada de dados
peso = float(input("Digite o peso dos peixes em quilos: "))

# Cálculo do excesso e da multa
excesso, multa = calcular_multa(peso)

# Exibição dos resultados
print(f"Peso dos peixes: {peso} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Multa a pagar: R$ {multa:.2f}")
