# Aula Condições

nome = input('Nome: ')
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
print('Bom dia, {}!'.format(nome))

nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))
media = (nota1+nota2)/2

# condições comuns
if media < 7:
    print('Media Ruim!')
else:
    print('Media Boa!')

# condições simplificadas

print('Parabens' if media >= 7 else 'NOTA BOSTA DO KRL')

