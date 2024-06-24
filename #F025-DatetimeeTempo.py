from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#criar uma data

lançamento_app = datetime(2024, 5, 7)


#Desafio 

data_atual = datetime.now()
data_aniversario = datetime.strptime(input('digite a data do seu aniversario: '),'%d/%m/%Y')
total_dias = data_aniversario - data_atual
print(total_dias.days)