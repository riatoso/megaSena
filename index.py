# MAIN DO JOGO
# VERSAO 1.0 DA MEGASENA
from jogado.jogo_feito import jogo_afazer as feito
from sorteado.jogo_sorteado import sorteado as sorteado
from confere.confere import confere as confere

if __name__ == "__main__":
    # JOGO FEITO
    feito = feito()
    print("\n#### Numeros jogados ####")
    for f in feito:
        print(f'{f}', end=" ")
    print("\n#########################\n")
    sorteado = sorteado()
    print("#### Numeros sorteados ####")
    for s in sorteado:
        print(f'{s}', end=" ")
    print("\n##########################\n")
    conferido = confere(feito,sorteado)
    print(f'Acertos...')
    for c in conferido:
        print(f'{c}', end=" ")
else:
    print("Fora do main.")


