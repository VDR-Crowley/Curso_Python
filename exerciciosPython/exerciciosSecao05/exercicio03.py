"""
3 - Leia um número real. Se o número for positivo imprima a raiz quadrado.
Do contrário, imprima o número ao quadrado.
    Algoritmo
    inicio
        receber um número real
        se número > 0
            raiz = math.pow(número, 1/2)
            mostrar raiz quadrada do número.
        senão
            quadrado = número*numeor
            mostrar número elevado ao quadrado
    fim
"""
import math
print("\nAtenção! leia isso antes de prosseguir.\n"
      "Digite um número, se o mesmo for positivo sera impresso o valor"
      "da raiz quadrada.\n"
      "se o número for negativo ele será elevado ao quadrado.\n\n")
num = float(input("Informe um número: "))
if num > 0:
    raiz = math.pow(num, 1/2)
    print(f"O número é positivo!")
    print(f"A raiz quadrada de {num} é {raiz:.3f}.")
elif num < 0:
    quadrado = num * num
    print(f"O número é negativo! \n")
    print(f"O {num} elevado ao quadrado {quadrado}. \n")
else:
    print(f"O número informado é {num} e não pode ser calculado.\n")
