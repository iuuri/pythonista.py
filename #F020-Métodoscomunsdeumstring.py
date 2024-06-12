nome_curso = 'Edição de video'
print(nome_curso.upper())#Deixa toda a string maiuscula
print(nome_curso.lower())#Deixa toda a string minuscula
print(nome_curso.strip())#remove todos os espaços em branco
print(nome_curso.lstrip())#remove todos os espaços em branco da esquerda
print(nome_curso.rstrip())#remove todos os espaços em branco da direita
print(nome_curso.find('ção'))#encontrar o indice de alguma informação
print(nome_curso.replace('video', 'Musica'))#Substitui alguma informação por outra
print('https://olx.com.br/relogio'.replace('relogio', 'carro'))

#Desafio
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print(f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')