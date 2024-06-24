from datetime import datetime
import random

print('-------------------------------- SEJA VEM-VINDO A NOSSA EMPRESA --------------------------------')
nome_usuario = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')
data_nascimento = datetime.strptime(input('Digite sua data de nascimento no formato dd/mm/aaaa: '), '%d/%m/%Y')
data_cadastro = datetime.now()
data_cadastro_formatada = data_cadastro.strftime('%d/%m/%Y')
cartoes = ['R$50,00', 'R$ 250,00', 'R$120,00']

print(f"""Olá {nome_usuario}, seu registro foi concluido com sucesso no dia {data_cadastro_formatada}, 
Parabéns, houve um sorteio e você ganhou um cartão no valor de {random.choice(cartoes)}""")


"""
Primeiro projeto do curso mestre pythonista.
Nesse projeto foi criado um simples sistema de cadastro de usuario. Nele recebemos os dados de nome,
idade, e data de nascimento e imprimimos na tela uma mesnagem de boas vindas com um desconto aleatorio.
"""