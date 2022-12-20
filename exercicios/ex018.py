# calculando cosseno, seno e tangente
import math

# lendo o angulo
angulo = float(input('Digite um Angulo: '))

# convertendo para radianos
radiano = math.radians(angulo)

# calculando os valores
cos = math.cos(radiano)
sen = math.sin(radiano)
tan = math.tan(radiano)

# printanto
print('O COS do ângulo de {:.2f} é: {:.2f}'.format(angulo, cos))
print('O SEN do ângulo de {:.2f} é: {:.2f}'.format(angulo, sen))
print('A TAN do ângulo de {:.2f} é: {:.2f}'.format(angulo, tan))
