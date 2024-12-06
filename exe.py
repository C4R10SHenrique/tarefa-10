# Passo 1: Criar a função de conversão
def converter_para_fahrenheit(celsius):
    # Fórmula de conversão de Celsius para Fahrenheit
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

# Passo 2: Pedir ao usuário uma temperatura em Celsius
celsius_input = input("Digite a temperatura em Celsius: ")

# Converter a entrada do usuário para um número (float)
celsius = float(celsius_input)

# Passo 3: Chamar a função e obter o resultado
fahrenheit = converter_para_fahrenheit(celsius)

# Passo 4: Exibir o resultado para o usuário
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
