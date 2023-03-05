reta1 = int(input('Reta1: '))
reta2 = int(input('Reta2: '))
reta3 = int(input('Reta3: '))

if (reta1 + reta2 > reta3) or (reta1 + reta3 > reta2) or (reta2 + reta3 > reta1):
    triangulo = True
else:
    triangulo = False

print('É Triangulo ? {} '.format(triangulo))