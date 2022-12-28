numero1 = int(input('Número: '))
numero2 = int(input('Número: '))
numero3 = int(input('Número: '))

if numero3 < numero2 < numero1:
    maior = numero1
    menor = numero3
elif numero3 < numero1 < numero2:
    maior = numero2
    menor = numero3
elif numero2 < numero3 < numero1:
    maior = numero1
    menor = numero2
elif numero2 < numero1 < numero3:
    maior = numero3
    menor = numero2
elif numero1 < numero2 < numero3:
    maior = numero3
    menor = numero1
elif numero1 < numero3 < numero2:
    maior = numero2
    menor = numero1

print('\nMaior: {}\nMenor: {}'.format(maior, menor))
