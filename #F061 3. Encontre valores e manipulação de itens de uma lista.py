valores = [1,2,3,4,2,5,6,7,8,9,10]
anos = [2020, 2030, 2040, 2050]

#adcionar ao final da lista
valores.append(11)
print(valores)

#unir lista
valores.extend(anos)
print(valores)

#adicionar listas sem modificar os valores
nova_lista = valores + anos
print(nova_lista)

#inserir um novo valor no meio da lista 
anos.insert(2, 2031)
print(anos)

#extrair item com indice 
ano_2020 = anos.pop(0)
print(ano_2020)

#remover item da lista por valor
anos.remove(2050)
print(anos)

#remover item da lista por index
del anos[0] #é possivel excluir uma faixa de valores, exemplo [1:6]
print(anos)

del valores[0:5]
print(valores)

#contar ocorrencia de um valor 
print(valores.count(7))

#resetar itens da lista 
valores.clear()
print(valores)
