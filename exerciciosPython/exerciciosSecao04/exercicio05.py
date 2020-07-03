"""
5 - Leia um número real e imprima a quinta parte deste número.
Algoritmo
inicio
    receber número real
    escrever quinta para do número
fim
"""

numero = float(input('Digite um numero: '))
print('{:.5f}'.format(numero))
print(f'{numero:.5f}')
print(f'{numero//5}')
print(f'{round(numero, 5)}')
