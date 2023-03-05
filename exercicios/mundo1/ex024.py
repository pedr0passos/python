# lendo a cidade
cidade = str(input('Cidade: ')).strip()

# separando a cidade em palavras
particao = cidade.split()

# pegando a primeira palavra e transformando ela em minuscula
pri_minuscula = particao[0].lower()

# verificando
print(pri_minuscula == 'santo')
