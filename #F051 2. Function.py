"""
def nome_da_funcao(parametros)
"""

# def dar_boas_vindas():
#     print('Bem-vindo!')
# dar_boas_vindas()

def gerar_nome_completo(nome, sobrenome):
    print(f'Olá, bem vindo {nome} {sobrenome}.')

gerar_nome_completo("Iuri", "Souza")

def calcular_valores(preco, quantidade = 1):
    print(f'O valor do produto é {preco*quantidade}')

calcular_valores(10.50, 3)