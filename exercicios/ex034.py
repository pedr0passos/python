salario = float(input('Salario: '))

if salario > 1250:
    aumento = salario*(1/10)
else:
    aumento = salario*(15/100)

salario += aumento
print('Novo salario com aumento de {:.2f}: R${:.2f}'.format(aumento, salario))