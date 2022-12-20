# importando a biblioteca math
import math

# utilizando a biblioteca math
numero = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, math.trunc(numero)))

# utilizando a conversão do python
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numero, int(numero)))
