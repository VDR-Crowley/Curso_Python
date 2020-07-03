"""
PEP8 - Python Enhancement proposal

São proposta de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PEP8 é que possamos escrever codigos python de forma pythónica.
[1] - Utilize Camel Case para nomes de Classes:

class Calculadora:
    pass


class CalculadoraCietifica:
    pass

[2] - Utilize nomes em minusculos, separados por underline para funções e variaveis

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação! (NÃo use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco;
- Separar funções e definições de classes com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com única linha em branco;

[5] - Imports

- Imports devem ser feitos em linhas diferentes;

# import errado

import sys, os

# import certo

import sys
import os

# Não á problemas em utilizar

from types import StringType, ListType

# Caso tenha muitos imports no mesmo pacote, recomenda-se fazer:

from type import {
    StringType,
    ListType,
    SetType,
    OutroType
}

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e
# antes de constantes ou variaveis globais

[6] - Espaços em expressões e instruções

# não faça
algo_(1)
# faça
algo(1)

[7] - Termine sempre uma nova instrução com uma nova linha
"""
import this

print('hello world')