# idade = 21 
# possui_convite = False
# filho_do_dono = True
# print((idade >=21) and (possui_convite == True))
# print((idade >= 21) or (possui_convite == True))
# print((idade > 21 and possui_convite) or (filho_do_dono == True))

# maior_idade = True
# possui_carteira_trabalho = True
# esta_trabalhando = True
# veiculo_propio = False
# print((maior_idade == True) and (possui_carteira_trabalho == True))
# print(possui_carteira_trabalho == True and not veiculo_propio)

#desafios

possui_passaporte = False
passagem_comprada = False
menor_idade = False

print(possui_passaporte and passagem_comprada and menor_idade == False)
print((possui_passaporte == True or passagem_comprada == True) and (menor_idade == False))
print((possui_passaporte == False or passagem_comprada) and not menor_idade)
print((possui_passaporte == False or passagem_comprada == False) and not menor_idade )
print((not possui_passaporte and not passagem_comprada) and menor_idade)