# Função para calcular a média anual das temperaturas
def calcular_media_anual(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Função para exibir temperaturas acima da média anual
def temperaturas_acima_da_media(temperaturas, media_anual):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    for i, temp in enumerate(temperaturas):
        if temp > media_anual:
            print(f"{i+1} - {meses[i]}: {temp:.2f}°C")

# Entrada de dados
temperaturas = []
for i in range(12):
    temp = float(input(f"Digite a temperatura média do mês {i+1}: "))
    temperaturas.append(temp)

# Cálculo da média anual
media_anual = calcular_media_anual(temperaturas)

# Exibição dos resultados
print(f"\nMédia anual das temperaturas: {media_anual:.2f}°C")
print("Temperaturas acima da média anual:")
temperaturas_acima_da_media(temperaturas, media_anual)
