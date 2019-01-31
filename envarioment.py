#   a b c d e f g h
# 1 R K B Q K B K R
# 2 p p p p p p p p
# 3 O * O * O * O *
# 4 * O * O * O * O
# 5 O * O * O * O *
# 6 * O * O * O * O
# 7 p p p p p p p p
# 8 R K B Q K B K R

import pieces


class board():

    def __init__(self):
        self.board = [[" ", "\tA", "B", "C", "D", "E", "F", "G", "H\n"],
                      ["1", "\tR", "K", "B", "Q", "K", "B", "K", "R"],
                      ["2", "\tp", "p", "p", "p", "p", "p", "p", "p"],
                      ["3", "\t■", " ", "■", " ", "■", " ", "■", " "],
                      ["4", "\t ", "■", " ", "■", " ", "■", " ", "■"],
                      ["5", "\t■", " ", "■", " ", "■", " ", "■", " "],
                      ["6", "\t ", "■", " ", "■", " ", "■", " ", "■"],
                      ["7", "\tp", "p", "p", "p", "p", "p", "p", "p"],
                      ["8", "\tR", "K", "B", "Q", "K", "B", "K", "R"]]

    def show(self):
        for entry in self.board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])

    def fill(self):  # entra las piezas(objetos) al tablero.

        # entra los peones, de ambos equipos.
        for columna in range(1, 9):
            for fila in range(1, 3):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = pieces.rook(
                            "white", fila, columna, "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = pieces.knight(
                            "white", fila, columna, "knight")  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = pieces.bishoop(
                            "white", fila, columna, "bishoop")  # alfil
                    if (columna == 4):
                        self.board[fila][columna] = pieces.queen(
                            "white", fila, columna, "queen")  # reina
                    if (columna == 5):
                        self.board[fila][columna] = pieces.king(
                            "white", fila, columna, "king")  # rey
                if (fila == 2):
                    self.board[fila][columna] = pieces.pawn(
                        "white", fila, columna, "pawn")  # peones

        for columna in range(1, 9):
            for fila in range(7, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = pieces.rook(
                            "black", fila, columna, "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = pieces.knight(
                            "black", fila, columna, "knight")  # caballo
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = pieces.bishoop(
                            "black", fila, columna, "bishoop")  # alfil
                    if (columna == 5):
                        self.board[fila][columna] = pieces.queen(
                            "black", fila, columna, "queen")  # reina
                    if (columna == 4):
                        self.board[fila][columna] = pieces.king(
                            "black", fila, columna, "king")  # rey

                if (fila == 7):
                    self.board[fila][columna] = pieces.pawn(
                        "black", fila, columna, "pawn")  # peones


board = board()
board.fill()
board.show()
