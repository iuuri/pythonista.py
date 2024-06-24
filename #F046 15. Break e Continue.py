# #continue, ignorar /pular
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         continue

# #break, para interromper a iteração
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         break

# frutas = ['maça' , 'manga' , 'laranja' , 'morango']
# for fruta in frutas:
#     if fruta == 'manga':
#         continue
#     print(f'{fruta} adcionada a dieta')

#     frutas = ['maça' , 'manga' , 'laranja' , 'morango']
# for fruta in frutas:
#     if fruta == 'manga':
#         break
#     print(f'{fruta} adcionada a dieta')

#Desafio 1
musicas = ['hip-hop', 'rock', 'rap', 'pop']
for musica in musicas:
    if musica == 'rap':
        continue
    print(musica)

musicas2 = ['hip-hop', 'rock', 'rap', 'pop']
for musica2 in musicas2:
    if musica2 == 'rock':
        break
    print(musica2)