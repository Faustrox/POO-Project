import pieces
class board():
    # Clase principal para el tablero
    def __init__(self):
        # Diseno del tablero donde iran las piezas
        self.game_board = [["                 ", "+---------------------------+", "", "", "", "", "", "", "", ""],
                           ["1\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                           ["2\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                           ["3\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                           ["4\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                           ["5\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                           ["6\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                           ["7\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                           ["8\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                           ["                 ", "+---------------------------+",
                               "", "", "", "", "", "", "", ""],
                           [" \t", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H", ""]]
        # Dise
        self.empty_board = [["                 ", "+---------------------------+", "", "", "", "", "", "", "", ""],
                            ["1\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                            ["2\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                            ["3\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                            ["4\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                            ["5\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                            ["6\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                            ["7\t|", "▓", "░", "▓", "░", "▓", "░", "▓", "░", "|"],
                            ["8\t|", "░", "▓", "░", "▓", "░", "▓", "░", "▓", "|"],
                            ["                 ", "+---------------------------+",
                             "", "", "", "", "", "", "", ""],
                            [" \t", " A ", " B ", " C ", " D ", " E ", " F ", " G ", " H", ""]]
        # Se le da valor a las posiciones para leer las columnas
        self.positionY = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        self.real_graveyard = {"white": [], "black": []}
        self.graveyard = {"white": [], "black": []}

    def show(self):
        # Muestra los objetos en el tablero
        for entry in self.game_board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8], entry[9])

    def fill(self):  # entra las piezas(objetos) al tablero.
        # Para las piezas negras
        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = pieces.rook(
                            "black", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = pieces.knight(
                            "black", [fila, columna], "knight")  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = pieces.bishoop(
                            "black", [fila, columna], "bishoop")  # alfil
                    if (columna == 4):
                        self.game_board[fila][columna] = pieces.queen(
                            "black", [fila, columna], "queen")  # reina
                    if (columna == 5):
                        self.game_board[fila][columna] = pieces.king(
                            "black", [fila, columna], "king")  # rey.

                if (fila == 2):
                    self.game_board[fila][columna] = pieces.pawn(
                        "black", [fila, columna], "pawn")  # peones
        # Para las piezas blancas
        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = pieces.rook(
                            "white", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = pieces.knight(
                            "white", [fila, columna], "knight")  # caballo
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = pieces.bishoop(
                            "white", [fila, columna], "bishoop")  # alfil
                    if (columna == 4):
                        self.game_board[fila][columna] = pieces.queen(
                            "white", [fila, columna], "queen")  # reina
                    if (columna == 5):
                        self.game_board[fila][columna] = pieces.king(
                            "white", [fila, columna], "king")  # rey

                if (fila == 7):
                    self.game_board[fila][columna] = pieces.pawn(
                        "white", [fila, columna], "pawn")  # peones

    def allay_pieces(self, team):
        # Verifica si una pieza es aliada o no
        array = []

        for x in range(1, 9):
            for y in range(1, 9):

                if isinstance(self.game_board[x][y], pieces.piece) is True and self.game_board[x][y].team == team:

                    array.append(self.game_board[x][y])

        return array

    def enemy_pieces(self, team):
        # Verifica si una pieza es enemiga
        array = []

        for x in range(1, 9):
            for y in range(1, 9):

                if isinstance(self.game_board[x][y], pieces.piece) is True and self.game_board[x][y].team != team:

                    array.append(self.game_board[x][y])

        return array


board = board()
# END OF THE BOARD
