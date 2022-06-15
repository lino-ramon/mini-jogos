from io import UnsupportedOperation


class JogoDaVelha:

    def __init__(self):
        self.branco = " "
        self.xis = "X"
        self.bolinha = "O"
        self.tabuleiro = self.criar_tabuleiro()
    
    def criar_tabuleiro(self):
        tab = []
        for i in range(3):
            tab.append([self.branco, self.branco, self.branco])

        return tab

    def realizarJogada(self, linha, coluna, jogador):       
        try:
            linha  = int(linha) - 1
            coluna = int(coluna) - 1
        except:
            print("Caracteres Inválidos!! Informe apenas números")

        try:
            self.tabuleiro[linha][coluna] = jogador
        except UnsupportedOperation:
            print("Posição Inválida!!")