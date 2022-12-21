import random

# lendo os nomes
nome1 = input('Primeiro Aluno: ')
nome2 = input('Segundo Aluno: ')
nome3 = input('Terceiro Aluno: ')
nome4 = input('Quarto Aluno: ')

# criando lista
lista = [nome1, nome2, nome3, nome4]

# apontando para uma pessoa aleatória da lista
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
