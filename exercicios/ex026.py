frase = str(input('Frase: ')).strip()
frase_minuscula = frase.lower()

quantidade_a = frase_minuscula.count('a')
primeira_posicao = frase_minuscula.find('a')
ultima_posicao = frase_minuscula.rfind('a')

print('Quantidade de vezes que o A aparece: {}'.format(quantidade_a))
print('Posição do primeiro A: {}'.format(primeira_posicao))
print('Posção do ultimo A: {}'.format(ultima_posicao))