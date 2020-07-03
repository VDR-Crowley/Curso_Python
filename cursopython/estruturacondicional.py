"""
Estruturas concionais if, elif e else
e
Estruturas logicas and (e), or (ou), not (não) e is (é)

Operadores únarios: not
Operadores binarios: and, or, is

Regras de funcionamentos:

para o "and" ambos dos valores tem que ser verdadeiros.
para o "or" um dos valores deve ser verdadeiro.
para o "not" o valor booleano é invertido, verdadeiro vira falso e falso vira verdadeiro.
para o "is" o valor é comparado com outro valor.
"""

idade = int(input('Infome sua idade: '))

if idade <= 18:
    print('Você ainda é menor de idade!')
elif idade >= 18:
    print('Você é maior de idade!')
else:
    print('comando não reconhecido.')


ligado = True
desligado = False
if ligado:
    print(not ligado)
if ligado or desligado:
    print(True)

login = True
ativo = True
if login and ativo:
    print('Bem vindo"')
else:
    print('Negado!')

bolo = True
brigadeiro = True
if bolo is brigadeiro:
    print(True)
