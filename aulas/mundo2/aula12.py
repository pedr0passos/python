nome = str(input('Nome: '))
feminino = ['Ana', 'Claudia', 'Jessica', 'Juliana']
masculino = ['Pedro', 'Gustavo', 'Matheus', 'Henrique']
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome in feminino:
    print('Feminino')
elif nome in masculino:
    print('Masculino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}')
