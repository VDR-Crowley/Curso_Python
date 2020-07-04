"""
5 - Faça um programa que receba um número inteiro e verifique
se estre número é par ou impar.

    Algoritmo
    receber um numero inteiro
    se numero % 2 == 0
        numero é par
    senao
        numero é impar
    fim
"""

numero = int(input("infome um numero: "))
if numero % 2 == 0:
    print(f"este numero {numero} é par")
else:
    print(f"esse numero {numero} é impar")
