# Função para calcular os descontos e o salário líquido
def calcular_folha_pagamento(valor_hora, horas_trabalhadas):
    # Cálculo do salário bruto
    salario_bruto = valor_hora * horas_trabalhadas
    
    # Cálculo do desconto do IR
    if salario_bruto <= 900:
        desconto_ir = 0
    elif salario_bruto <= 1500:
        desconto_ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        desconto_ir = salario_bruto * 0.10
    else:
        desconto_ir = salario_bruto * 0.20
    
    # Cálculo do desconto do INSS (10%)
    desconto_inss = salario_bruto * 0.10
    
    # Cálculo do desconto do Sindicato (3%)
    desconto_sindicato = salario_bruto * 0.03
    
    # Cálculo do FGTS (11% do salário bruto, não descontado)
    fgts = salario_bruto * 0.11
    
    # Total de descontos
    total_descontos = desconto_ir + desconto_inss + desconto_sindicato
    
    # Cálculo do salário líquido
    salario_liquido = salario_bruto - total_descontos
    
    return salario_bruto, desconto_ir, desconto_inss, desconto_sindicato, fgts, total_descontos, salario_liquido

# Entrada de dados
valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

# Cálculo da folha de pagamento
salario_bruto, desconto_ir, desconto_inss, desconto_sindicato, fgts, total_descontos, salario_liquido = calcular_folha_pagamento(valor_hora, horas_trabalhadas)

# Exibição dos resultados
print(f"\nSalário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({desconto_ir / salario_bruto * 100:.0f}%) : R$ {desconto_ir:.2f}")
print(f"(-) INSS (10%) : R$ {desconto_inss:.2f}")
print(f"(-) Sindicato (3%) : R$ {desconto_sindicato:.2f}")
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")
