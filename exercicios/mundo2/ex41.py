ano_nascimento = int(input('Ano de Nascimento: '))

if ano_nascimento <= 9:
    print('MIRIM')
if 9 < ano_nascimento <= 14:
    print('INFANTIL')
if 14 < ano_nascimento <= 19:
    print('JUNIOR')
if 19 < ano_nascimento <= 20:
    print('SENIOR')
if ano_nascimento > 20:
    print('MASTER')