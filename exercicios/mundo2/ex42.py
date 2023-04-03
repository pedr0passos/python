reta1 = int(input('Reta1: '))
reta2 = int(input('Reta2: '))
reta3 = int(input('Reta3: '))

triangulo = False
equilatero = False
isosceles = False
escaleno = False

if (reta1 + reta2 > reta3) or (reta1 + reta3 > reta2) or (reta2 + reta3 > reta1):
    triangulo = True
    if reta1 == reta2 == reta3:
        equilatero = True
    if (reta1 == reta2) or (reta1 == reta3) or (reta2 == reta3):
        isosceles = True
    if reta1 != reta2 != reta3:
        escaleno = True

print('É Triangulo ? {} '.format(triangulo))
print(f'Equilatero: {equilatero}')
print(f'Isosceles: {isosceles}')
print(f'Escaleno: {escaleno}')
