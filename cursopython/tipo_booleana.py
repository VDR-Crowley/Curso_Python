"""
Tipos de valores booleanos
ela é baseada na Algebra de George Boole

Recebe valores constantes True ou False
Os operadores dela é and, or e not
"""
chocolate = True
balas = False
print(chocolate and balas)
print(type(chocolate))
print(type(balas))

# Tambem é possivel fazer negação usando o not
"""
Fazer a negação de uma valor é invertelo como um
valor positivo vira negativo, um sim vira não
Sitaxe
"""

doces = False
print(not doces)  # valor True

print('\n\n')

print('|-OPERADOR AND-|')
print(True and True)
print(False and False)
print(True and False)
print(False and True)
print('|--------------|')

print('\n\n')

print('|-OPERADOR OR-|')
print(True or True)
print(False or False)
print(True or False)
print(False or True)
print('|-------------|')