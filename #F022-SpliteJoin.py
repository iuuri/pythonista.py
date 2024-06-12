# frase = 'Olá, bem-vindo a este treinamento!'
# print(frase.split())#separa em uma lista de string
# print(frase.split(','))#separa em uma lista de string sempre que encontrar o parametro colocado dentro do metodo, nesse caso virgula.
# print(frase.split('-'))#separa em uma lista de string sempre que encontrar o parametro colocado dentro do metodo, nesse caso traço.

# nomes = 'jhonatan, rafael, carol, amanda,jeferson'
# print(nomes.split())
# print(nomes.split(','))

# novos = 'music #guitar #gamer #coder #python'
# print(novos.split())
# print(novos.split('#'))
# print(novos.split('#', 3))

# hashtag_seprados_por_espaco = novos.split(' ')
# print(','.join(hashtag_seprados_por_espaco))
# print('.'.join(hashtag_seprados_por_espaco))
# print(' '.join(hashtag_seprados_por_espaco))


# #Desafios
frase1= 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camila'
#Desafio 1
palavras1 = frase1.split()
print(palavras1)

# #desafio 2
palavras2 = frase2.split(',')
print(palavras2)

#desafio 3
print(','.join(palavras1))

# desafio 4
print(' & '.join(palavras2))
