velocidade = float(input('Velocidade: '))
limite = 80

if velocidade > limite:
    multa = 7 * (velocidade - limite)
    print('Multado em R${:.2f}!'.format(multa))
else:
    print('Dentro da Velocidade!')


