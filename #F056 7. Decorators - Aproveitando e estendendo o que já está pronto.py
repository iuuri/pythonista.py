#Decorators

# def meu_decorator(funcao):
#     def wrapper():
#         print('antes')
#         funcao()
#         print('depois')
#     return wrapper

# @meu_decorator
# def parabenizar():
#     print('Parabens!')

# parabenizar()

from datetime import datetime

def decorator(funcao):
    def executar():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return executar

@decorator
def executou():
    print('Executou')

executou()