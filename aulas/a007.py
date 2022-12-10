# Operadores Aritméticos
# + -> adição
# - -> subtração
# * -> multiplicação
# / -> divisão
# ** -> potencia
# // -> divisão inteira
# % -> resto da divisão

#parte1
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer {:-^20}!'.format(nome))

#parte2
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor: '))

soma = n1+n2
mult = n1*n2
div = n1/n2
div_int = n1//n2
exp = n1**n2

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(soma, mult, div))
print('A divisão inteira é {} e a potencia é {}'.format(div_int, exp))
