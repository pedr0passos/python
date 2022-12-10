# Altura da parede
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura*largura
tinta_necessaria = area/2
print('A área da parede é {} e ela precisa de {} litros de tinta para ser pintada.'.format(area, tinta_necessaria))
