valor_casa = float(input('Valor da Casa: '))
salario_comprador = float(input('Salário do Comprador: '))
anos_pagamento = int(input('Anos de Pagamento: '))

prestacao = (valor_casa/(anos_pagamento*12))

if prestacao <= (salario_comprador*0.3):
    print('Emprestimo Concedido')
else:
    print('Emprestimo Negado')
