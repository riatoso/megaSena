# JOGO SORTEADO

def sorteado():
    from random import randint
    jogo = []
    while True and len(jogo) <= 6:
        numero = randint(1,60)
        if numero in jogo:
            continue
        else:
            jogo.append(numero)
    jogo = sorted(jogo)
    return jogo

