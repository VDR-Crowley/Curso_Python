"""
Escopo de variável

Escopo é uma espaço limitado

dois tipos de escopo

1 -  variaveis globais
    - variáveis globais são reconhecidas, ou seja, seu escopo compreende, toda o programa.
2 - variáveis local
    - variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado apenas onde foi declarado

forma de se declarar em python

nome_da_variavel = valor_da_variavel

python é uma linguagem de tipagem dinâmica.
Isso significa que ao declararmos uma variavel,
nós não colocamos o tipo do dado dela, como é feito em outras linguagens.
O tipo será inferido ao atribúirmos o valor á mesma.
"""

microsoft = 'bill gates'  # Global


def nome():
    nome1 = 'vando'  # Local
    print(nome1)
    print(type(nome1))


nome()
print(microsoft)
print(type(microsoft))
