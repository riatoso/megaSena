# JOGO PARA FAZER

def jogo_afazer():
    jogo = []
    while len(jogo) <= 5:
        num = input(f"Digite o numero {len(jogo) + 1}  para o jogo!:")
        try:
            num = int(num)
        except ValueError as err:
            print(err)
        if num in jogo:
            print(f"Voce digitou um numero jogado {num}.")
            continue
        else:
            if num > 60 or num < 1:
                print("Voce digitou um numero fora do range do jogo.")
                continue
            else:
                jogo.append(num)
    jogo = sorted(jogo)
    return jogo
