# strip serve para retirar os espaços antes e depois digitados errados na string
nome = input('Nome: ').strip()

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
quantidade_letras = (len(nome)-nome.count(' '))

# pegando a quantidade de letras do primeiro nome através da posição do vetor
quantidade_letras_pri_nome = nome.find(' ')

# outra maneira de separar os nomes através dos espaços 
separa = nome.split()

print('Dados do Nome:')
print('Maiusculas: {}'.format(nome_maiusculo))
print('Minusculas: {}'.format(nome_minusculo))
print('Quantidade de Letras: {}'.format(quantidade_letras))
print('Quantidade de Letras do Primeiro Nome: {}'.format(len(separa[0])))
