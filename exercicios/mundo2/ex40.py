nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1+nota2)/2

if media < 5:
    print('Reprovado')
if 5 < media < 7:
    print('Prova Final')
if media >= 7:
    print('Aprovado')