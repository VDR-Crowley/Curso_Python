"""
2 - Leia um número fornecido pelo usuário. Se esse número for positivo,
calcule a raiz quadrada do número. Se o número for negativo,
mostre uma mensagem dizendo que o número é inválido.
    Algoritmo
    inicio
        receber um numero
        se numero > 0
            raiz = math.pow(numero, 1/2)
            mostrar raiz quadrada do número
        senão se numero < 0
            mostrar esse número é negativo
        senão
            O número é 0, digite outro número
    fim
"""
import math
numero = int(input('Informe um número: '))
if numero > 0:
    raiz = math.pow(numero, 1/2)
    print(f"Essa é a raiz quadrada do numero:{numero} é: {raiz:.3f}")
elif numero < 0:
    print(f"O número informado é negativo!")
else:
    print("número não entendido")
