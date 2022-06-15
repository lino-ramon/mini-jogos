from io import UnsupportedOperation


class JogoDaVelha:

    def __init__(self):
        self.branco = " "
        self.xis = "X"
        self.bolinha = "O"
        self.tabuleiro = []
        self.instanciar_novo_tabuleiro()
    
    def instanciar_novo_tabuleiro(self):
        self.tabuleiro = []
        for i in range(3):
            self.tabuleiro.append([self.branco, self.branco, self.branco])

    def imprimir_tabuleiro(self):
        for lin in range(3):
            for col in range(3):
                
                if self.tabuleiro[lin][col] == self.branco and lin < 2:
                    if col < 2:
                        print("___|", end="")
                    else:
                        print("___")
                
                elif self.tabuleiro[lin][col] != self.branco and lin < 2:
                    if col < 2:
                        print("_" + self.tabuleiro[lin][col] + "_|", end="")
                    else:
                        print("_" + self.tabuleiro[lin][col] + "_")
                
                elif self.tabuleiro[lin][col] == self.branco and lin == 2:
                    if col < 2:
                        print("   |", end="")
                    else:
                        print("   ")

                elif self.tabuleiro[lin][col] != self.branco and lin == 2:
                    if col < 2:
                        print(" " + self.tabuleiro[lin][col] + " |", end="")
                    else:
                        print(" " + self.tabuleiro[lin][col] + " \n")

    def verificar_posicao_branco(self, linha, coluna):
        return (self.tabuleiro[linha][coluna] == self.branco)
    
    def realizar_jogada(self, linha, coluna, jogador):       
        try:
            linha  = int(linha) - 1
            coluna = int(coluna) - 1
        except:
            print("Caracteres Inválidos!! Informe apenas números")
            
            return False

        if (linha >= 0 and linha <= 2) and (coluna >= 0 and coluna <= 2): 
            
            if self.verificar_posicao_branco(linha, coluna):
                self.tabuleiro[linha][coluna] = jogador
                
                return True
            
            print("Posição já preenchida!! Tenta outra jogada")

        else:
            print("Posição Inválida!!")

        return False