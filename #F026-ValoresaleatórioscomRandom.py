#Valores aleatorios com random  
import random

print(random.random())#gera um valor de 0.0 a 1.0
print(random.uniform(4,10))#gera um valor decimal de valor minimo ao valor maximo
print(random.randint(4,10))#gera um valor inteiro de valor minimo ao valor maximo

cores = ['verde', 'vermelho','azul']
print(random.choices(cores))#escolhe uma opção aleatoria de uma lista 
print(random.choices(cores, k=2))#escolhe mais de uma opção aleatoria de uma lista 

cartas_baralho = ['carta1', 'carta2', 'carta3', 'carta4',]
print(random.shuffle(cartas_baralho))#embaralha as opções
print(cartas_baralho)

#desafio 1 
moeda = ['cara', 'coroa']
print(random.choices(moeda))

#desafio2
nomes = ['iuri', 'bruno', 'rafael', 'guilherme', 'gabriel']
print(random.choices(nomes))

#desafio3
print(random.randint(10, 100))