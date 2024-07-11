# a_lista = ['A', 'B', 'C', 'D', 'E']
# b_lista = [1, 2, 3, 4 , 6]

# for a,b in zip(a_lista, b_lista):
#     print(a)
#     print(b)


# produtos = ['Produto 1', 'Produto 2', 'Produto 3']
# precos = [250, 300, 100]

# for produto, preco in zip(produtos,precos):
#     print(f'Salvando o produto {produto} com valor de {preco}')


# titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3']
# descricoes = ['Descrição 1', 'Descrição 2']

# for titulo, descricao in zip_longest(titulos, descricoes):
#     print(f'Encontramos o titulo {titulo} com a descrição {descricao}')

#desafio 1 
from itertools import zip_longest
produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00',]

for produto, preco in zip_longest(produtos, precos):
    print(f'Produto: {produto} encontrado no valor de: {preco}')
