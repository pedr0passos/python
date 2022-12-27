nome = str(input('Nome: ')).strip()

# separando as palavras
lista = nome.split()
tamanho_lista = len(lista)

# pegando o primeiro e ultimo nome da lista
primeiro_nome = lista[0]
ultimo_nome = lista[tamanho_lista-1]

# printando na tela
print('Primeiro Nome: {}'.format(primeiro_nome))
print('Ultimo Nome: {}'.format(ultimo_nome))