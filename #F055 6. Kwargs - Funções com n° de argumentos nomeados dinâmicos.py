# **Kwargs(keyword arguments)
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='pythonista', d='profissionais' )