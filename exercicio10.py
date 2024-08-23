# Função para retornar o reverso de um número inteiro
def reverso_numero(numero):
    # Converte o número para string, inverte a string e converte de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Entrada de dados
numero = int(input("Digite um número inteiro: "))

# Cálculo do reverso do número
numero_reverso = reverso_numero(numero)

# Exibição do resultado
print(f"O reverso do número {numero} é {numero_reverso}.")
