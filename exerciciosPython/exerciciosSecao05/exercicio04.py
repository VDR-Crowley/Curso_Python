"""
4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:

- O número digitado ao quadrado
- A raiz quadrada do número digitado

    Algoritmo
    inicio
    receber um numero
    se numero > 0
        quadrado = numero * numero
        raiz = math.pow(numero, 1/2)
        mostrar numero elevado ao quadrado
        mostar a raiz quadrada do numero
    fim

"""
import math
numero = int(input("Infome um numero: "))
if numero > 0:
    quadrado = numero * numero
    raiz = math.pow(numero, 1/2)
    print(f"O resultado de {numero} ao quadrado é {quadrado}")
    print(f"A raiz quadrada de {numero} é {raiz:.3f} \n")
else:
    print("O numero informado é 0 ou negativo!\n"
          "Por favor digite um número positivo.")
