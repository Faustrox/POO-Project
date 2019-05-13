import pieces
import board
import rook
import bishoop

class queen(pieces.piece):
    # Reina
    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♕"

        else:
            simbol = "♛"

        return simbol

    def possible_move(self): # Funcion que imprime los movimientos posibles, mezcla los movimientos de la torre y del alfil y los junta en un diccionario
        arraym = {}
        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
        torre = rook.rook(self.team, [pos[0], pos[1]], "rook")
        alfil = bishoop.bishoop(self.team, [pos[0], pos[1]], "bishoop")
        for i in torre.possible_move():
            arraym[i] = torre.possible_move()[i]
        for i in alfil.possible_move():
            arraym[i] = alfil.possible_move()[i]
        return arraym
