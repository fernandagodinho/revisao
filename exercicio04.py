import math

# Função para calcular as raízes da equação do segundo grau
def calcular_raizes(a, b, c):
    if a == 0:
        print("A equação não é do segundo grau.")
        return
    
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")

# Entrada de dados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo das raízes
calcular_raizes(a, b, c)
