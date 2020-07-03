"""
1 - Faça um programa que receba dois números e mostre qual deles é o maior.
    Algoritmo
    inicio
        receber o numero1
        receber o numero2
        se numero1 > numero2
            mostrar numero1
        senão
            mostrar numero2
    fim
"""
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
if num1 > num2:
    print(f"O primeiro numero: {num1} é o maior")
else:
    print(f"O segundo numero: {num2} é o maior")

