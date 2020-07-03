"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo string

em python, string é tudo que estiver entre:
- Aspas simles;
- Aspas duplas;
- Aspas simples triplas;
- Aspas dublas triplas;
Exemplos:
- 'hello'
- "hello"
- '''hello'''
"""
# """hello"""

# Entrada de dados
# print('Qual é o seu nome')
# nome = input()  # Input -> Entrada

nome = input('Qual é o seu nome?: ')

# Exemplo de print 'antigos' 2.x
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')

# print('Qual sua idade')
# idade = input()

idade = int(input('Qual sua idade:'))

# Processamento

# Saida

# Exemplo de print 'antigo' 2.x
# print('%s tem %s anos' % (nome, idade))

# Exemolo de print mais 'moderno' 3.x
# print('{0} tem {1} anos'.format(nome, idade))

# Exemplo de print mais 'atual' 3.7
print(f'{nome} tem {idade} anos')

'''
#int(idade) => cast
cast é a conversão de um tipo de dado para outro
'''
print(f'{nome} nasceu em {2020 - idade}')
