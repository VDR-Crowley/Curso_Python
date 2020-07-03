"""
7 - Leia uma temperatura em graus fahrenheit e apresente-a convertida em graus
Celsius. A formula de conversão é: C = 5.0* (F - 32.0) / 9.0,
sendo C a temperatura celsius e F a temperatura em fahrenheit.
algoritmo
inicio
    receber graus F
    calculo = C = 5.0 * (F - 32.0) / 9.0
    mostra o resultado
fim
"""

F = float(input('Informe a temperatura em graus F: '))
calculo = C = 5.0 * (F - 32.0) / 9.0
print(f'Essa é a conversão de graus fahrenheit em graus celsius {round(calculo, 2)}')