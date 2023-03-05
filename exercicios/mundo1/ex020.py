# importanto a biblioteca random
import random

# lendo as pessoas
pessoa1 = input('Primeiro Aluno: ')
pessoa2 = input('Segundo Aluno: ')
pessoa3 = input('Terceiro Aluno: ')
pessoa4 = input('Quarto Aluno: ')

lista = [pessoa1, pessoa2, pessoa3, pessoa4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
