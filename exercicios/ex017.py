# calculandoa a hipotenusa de uma triangulo retangulo
from math import hypot

# lendo os catetos
cateto_adjacente = float(input('Cateto Adjacente: '))
cateto_oposto = float(input('Cateto Oposto: '))

# matematicamente h^2 = co^2 + ca^2
hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)
print('Hipotenusa: (Normalmente) {:.2f}'.format(hipotenusa))

# utilizando a função math
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print('Hipotenusa: (Função Math) {:.2f}'.format(hipotenusa))
