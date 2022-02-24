# CONFERE OS JOGOS

def confere(feito, sorteado):
    acertados = []
    for num in feito:
        for num1 in sorteado:
            if num1 == num:
                acertados.append(num)
            else:
                continue
    return acertados