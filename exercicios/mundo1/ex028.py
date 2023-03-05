import random

condicao = True
while condicao:
    numero_pensado = random.randint(0, 5)
    adivinha = int(input('Advinhe o Número: '))

    if adivinha == numero_pensado:
        print('Adivinhou, Parabéns você Venceu!')
        condicao = False
    else:
        print('Sinto Muito, você perdeu!')

