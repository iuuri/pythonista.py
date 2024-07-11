#Dicionários
dicionario_pessoas = {
    'nome':'Carol',
    'idade':'18',
    'altura':1.60
}

dicionario_pessoas_2 = dict(
    nome='Carol',
    idade='18',
    altura=1.60
)

print(dicionario_pessoas)
print(dicionario_pessoas_2)
print(dicionario_pessoas['idade'])
print(dicionario_pessoas.keys())
print(dicionario_pessoas.values())
print(dicionario_pessoas.items())

#Iterar sobre o dicionário
for item in dicionario_pessoas.items():
    print(item[1])