from jogodavelha import JogoDaVelha

if __name__ == "__main__":
    game = JogoDaVelha()
    print(game.tabuleiro)
    l = input("lin: ")
    c = input("col: ")

    game.realizarJogada(l, c, game.xis)
    print(game.tabuleiro)