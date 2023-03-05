# Salário
salario = float(input('Digite o salário: '))
aumento = salario*(15/100)
novo_salario = salario + aumento
print('O salario que era R${:.2f} tera 15% de aumento, portanto agora vale: R${:.2f}'.format(salario, novo_salario))
