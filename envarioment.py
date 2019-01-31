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
        self.board = [[" \t", "A", "B", "C", "D", "E", "F", "G", "H\n"],
                      ["1\t", "■", " ", "■", " ", "■", " ", "■", " "],
                      ["2\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                      ["3\t", "■", " ", "■", " ", "■", " ", "■", " "],
                      ["4\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                      ["5\t", "■", " ", "■", " ", "■", " ", "■", " "],
                      ["6\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                      ["7\t", "■", " ", "■", " ", "■", " ", "■", " "],
                      ["8\t", " ", "■", " ", "■", " ", "■", " ", "■"]]

        self.position = {"A": {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [1, 4], 5: [1, 5], 6: [1, 6], 7: [1, 7], 8: [1, 8]},
              {"B": {1: [2, 1], 2: [2, 2], 3: [2, 3], 4: [2, 4], 5: [2, 5], 6: [2, 6], 7: [2, 7], 8: [2, 8]},
              {"C": {1: [3, 1], 2: [3, 2], 3: [3, 3], 4: [3, 4], 5: [3, 5], 6: [3, 6], 7: [3, 7], 8: [3, 8]},
              {"D": {1: [4, 1], 2: [4, 2], 3: [4, 3], 4: [4, 4], 5: [4, 5], 6: [4, 6], 7: [4, 7], 8: [4, 8]},
              {"E": {1: [5, 1], 2: [5, 2], 3: [5, 3], 4: [5, 4], 5: [5, 5], 6: [5, 6], 7: [5, 7], 8: [5, 8]},
              {"F": {1: [6, 1], 2: [6, 2], 3: [6, 3], 4: [6, 4], 5: [6, 5], 6: [6, 6], 7: [6, 7], 8: [6, 8]},
              {"G": {1: [7, 1], 2: [7, 2], 3: [7, 3], 4: [7, 4], 5: [7, 5], 6: [7, 6], 7: [7, 7], 8: [7, 8]},
              {"H": {1: [8, 1], 2: [8, 2], 3: [8, 3], 4: [8, 4],
                  5: [8, 5], 6: [8, 6], 7: [8, 7], 8: [8, 8]}}


    def show(self):
        for entry in self.board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])

    def fill(self):  # entra las piezas(objetos) al tablero.

        # entra los peones, de ambos equipos.
        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = pieces.rook(
                            "white", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = pieces.knight(
                            "white", [fila, columna])  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = pieces.bishoop(
                            "white", [fila, columna])  # alfil
                    if (columna == 4):
                        self.board[fila][columna] = pieces.queen(
                            "white", [fila, columna])  # reina
                    if (columna == 5):
                        self.board[fila][columna] = pieces.king(
                            "white", [fila, columna])  # rey
                if (fila == 2):
                    self.board[fila][columna] = pieces.pawn(
                        "white", [fila, columna])  # peones

        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = pieces.rook(
                            "black", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = pieces.knight(
                            "black", [fila, columna])  # caballo
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = pieces.bishoop(
                            "black", [fila, columna])  # alfil
                    if (columna == 5):
                        self.board[fila][columna] = pieces.queen(
                            "black", [fila, columna])  # reina
                    if (columna == 4):
                        self.board[fila][columna] = pieces.king(
                            "black", [fila, columna])  # rey

                if (fila == 7):
                    self.board[fila][columna] = pieces.pawn(
                        "black", [fila, columna])  # peones


board = board()
board.fill()
board.show()
