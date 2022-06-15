from jogodavelha import JogoDaVelha

if __name__ == "__main__":
    game = JogoDaVelha()

    while True:
        game.imprimir_tabuleiro()
        
        l = input("lin: ")
        c = input("col: ")

        if l == "777": break

        if c == "777":
            game.instanciar_novo_tabuleiro()
        else:
            game.realizar_jogada(l, c, "X")
            game.imprimir_tabuleiro()