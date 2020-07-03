"""
Em python todo tipo de dado é considerado string
"""
nome = "vinicius \n dos reis"  # \n quebra a linha
print(nome)

nome = """vando 
dos reis"""
print(nome)

# No python não ha a necessidade de usar
# Um caracter de escape
# nome = 'viviane é \'linda\' ' <- caracter de escape \

# nome = "viviane é 'chata' "
# print(nome)

# nome1, nome2 = 'Bill Gates', 'Steve jobs'
# print(f"{nome1} Mente brilhante"
#       f" por tras da MICROSOFT")
# print(f"{nome2} Foi a mente Brilhante"
#       f" por tras da grande APPLE")

nome = 'xbox e vida'
print(nome.upper())  # upper() transforma caracteres em maiúsculo.
print(nome.lower())  # lower() transforma caracteres em minúsculo.
print(nome.split())  # split() transforma em uma lista separando as string po espaços
# [  0,     1,   2    ]
# ['xbox', 'e', 'vida']
print(nome.split()[2])  # imprime vida

# caracteres que serão impressos.
print(nome[0:4])  # slice de string

# Modo pythônico de inverte string
# Comece do primeiro elemento, vai ate o ultimo elemento e inverta.
print(nome[::-1])  # irversão de string

print(nome.replace('e', 'é'))  # substitui uma string.
print(nome.replace('xbox', 'ps4'))  # tambem pode ser com palavras inteiras.
