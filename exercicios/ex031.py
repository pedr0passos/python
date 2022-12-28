distancia = int(input('Distancia: '))
if distancia <= 200:
    preco = (distancia*0.5)
else:
    preco = (distancia*0.45)
print('Preço Total: R${:.2f}'.format(preco))