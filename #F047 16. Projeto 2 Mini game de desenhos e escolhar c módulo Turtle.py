from turtle import Turtle

#inicializar 
t = Turtle()

#definir velociadade 
t.speed(1)

while True:
    direcao = input('Para qual direção a tartaruga deve se mover: f = frente, t = trás: ')
    if direcao == 'f':
        distancia = int(input('Quantos pixels deve se mover para frente? '))
        rotacionar = input('Deseja rotacionar? e = esquerda, d = direita ou n = não: ')
        if rotacionar == "e":
            rotacionar = int(input('Quantos pixels devemos rotacionar para esquerda? '))
            t.left(rotacionar)
            t.forward(distancia)
        if rotacionar == 'd':
            rotacionar = int(input('Quantos pixels devemos rotacionar para direita? '))
            t.right(rotacionar)
            t.forward(distancia)
        if rotacionar == 'n':
            t.forward(distancia)
    if direcao == 't':
        distancia = int(input('Quantos pixels deve se mover para trás? '))
        rotacionar = input('Deseja rotacionar? e = esquerda, d = direita ou n = não: ')
        if rotacionar == "e":
            rotacionar = int(input('Quantos pixels devemos rotacionar para esquerda? '))
            t.left(rotacionar)
            t.backward(distancia)
        if rotacionar == 'd':
            rotacionar = int(input('Quantos pixels devemos rotacionar para direita? '))
            t.right(rotacionar)
            t.backward(distancia)
        if rotacionar == 'n':
            t.backward(distancia)
    continuar = input('Deseja continuar andando: s = sim, n = não: ')
    if continuar == 's':
        continue
    if continuar == 'n':
        break

        
    
