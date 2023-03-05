# Preço de Produto
preco = float(input('Digite o preço: '))
desconto = preco*(5/100)
novo_preco = preco - desconto
print('O produto com o preço R${} com 5% de desconto valerá R${}.'.format(preco, novo_preco))
