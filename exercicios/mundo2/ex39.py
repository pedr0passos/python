ano_nascimento = int(input('Ano de Nascimento: '))
ano_atual = 2023
idade = ano_atual - ano_nascimento

falta = False
passou = False
if idade < 18:
    print('Ainda irá se alistar')
    falta = True
if idade == 18:
    print('Está na hora de se alistar')
if idade > 18:
    print('Passou do tempo de se alistar')
    passou = True
if falta:
    print(f'Faltam {18-idade} anos para se alistar')
if passou:
    print(f'Passaram {idade-18} anos do alistamento')