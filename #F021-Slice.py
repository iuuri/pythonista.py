teclado = 'Teclado #F021 7. Slice - extraindo partes de um string'
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])

#acessando partes de um string
link = 'facebook.com/devaprender'
print(link[0])#Acesser o primeiro item
print(link[-1])#Acesser o ultimo item
print(link[0:5])#acessar caracteres do indice 0 ate o indice 5
print(link[0:])#acessar de algum indice, no caso o primeiro, ate o final
print(link[-5:])
print(link[5:])
print(link[:-5])

#acessar a ultima ocorrencia dentro da string
frase = 'Clean Code'
print(frase.rindex('C'))

#desafio
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

#desafio 2 
frase2 = 'Desenvolvimento de Aplicações'
ultimaocorrencia = frase2.rindex('d')

print(frase2[ultimaocorrencia:])

indice_d = frase2.rindex('d')
indice_s = frase2.rindex('s')

print(frase2[indice_d:indice_s+1])
