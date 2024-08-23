import math

# Função para calcular a quantidade de tinta e o custo
def calcular_tinta(area):
    # Cobertura da tinta
    cobertura_por_litro = 6
    # Tamanhos e preços das embalagens
    litro_por_lata = 18
    preco_lata = 80.00
    litro_por_galao = 3.6
    preco_galao = 25.00
    
    # Acrescentar 10% de folga
    area_com_folga = area * 1.1
    litros_necessarios = area_com_folga / cobertura_por_litro
    
    # Apenas latas de 18 litros
    latas_necessarias = math.ceil(litros_necessarios / litro_por_lata)
    custo_latas = latas_necessarias * preco_lata
    
    # Apenas galões de 3,6 litros
    galoes_necessarios = math.ceil(litros_necessarios / litro_por_galao)
    custo_galoes = galoes_necessarios * preco_galao
    
    # Mistura de latas e galões
    latas_mistura = math.floor(litros_necessarios / litro_por_lata)
    litros_restantes = litros_necessarios - (latas_mistura * litro_por_lata)
    galoes_mistura = math.ceil(litros_restantes / litro_por_galao)
    custo_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)
    
    return latas_necessarias, custo_latas, galoes_necessarios, custo_galoes, latas_mistura, galoes_mistura, custo_mistura

# Entrada de dados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo das quantidades e custos
latas, custo_latas, galoes, custo_galoes, latas_mistura, galoes_mistura, custo_mistura = calcular_tinta(area)

# Exibição dos resultados
print(f"\nPara pintar uma área de {area:.2f} m², você precisará de:")
print(f"\n1. Comprando apenas latas de 18 litros:")
print(f"   - Quantidade de latas: {latas}")
print(f"   - Custo total: R$ {custo_latas:.2f}")

print(f"\n2. Comprando apenas galões de 3,6 litros:")
print(f"   - Quantidade de galões: {galoes}")
print(f"   - Custo total: R$ {custo_galoes:.2f}")

print(f"\n3. Misturando latas e galões:")
print(f"   - Quantidade de latas: {latas_mistura}")
print(f"   - Quantidade de galões: {galoes_mistura}")
print(f"   - Custo total: R$ {custo_mistura:.2f}")
