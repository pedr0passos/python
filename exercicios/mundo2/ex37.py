numero = int(input('Número: '))
print('Escolha a Base de Conversão: 1-Binário 2-Octal 3-Hexadecimal')
escolha = int(input())
if escolha == 1:
    print('Binário')
if escolha == 2:
    print('Octal')
if escolha == 3:
    print('Hexadecimal')
else:
    print('Escolha Incorreta')
