import board
import pieces
import knight
import bishoop
import rook
import queen

class board_function():

    def __init__(self):
        pass

    def show(self):
        # Muestra los objetos en el tablero
        for entry in board.board.game_board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8], entry[9])

    def fill(self):  # entra las piezas(objetos) al tablero.
        # Para las piezas negras
        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        board.board.game_board[fila][columna] = rook.rook(
                            "black", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        board.board.game_board[fila][columna] = knight.knight(
                            "black", [fila, columna], "knight")  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        board.board.game_board[fila][columna] = bishoop.bishoop(
                            "black", [fila, columna], "bishoop")  # alfil
                    if (columna == 4):
                        board.board.game_board[fila][columna] = queen.queen(
                            "black", [fila, columna], "queen")  # reina
                    if (columna == 5):
                        board.board.game_board[fila][columna] = pieces.king(
                            "black", [fila, columna], "king")  # rey.

                if (fila == 2):
                    board.board.game_board[fila][columna] = pieces.pawn(
                        "black", [fila, columna], "pawn")  # peones
        # Para las piezas blancas
        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        board.board.game_board[fila][columna] = rook.rook(
                            "white", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        board.board.game_board[fila][columna] = knight.knight(
                            "white", [fila, columna], "knight")  # caballo
                    if (columna == 3 or columna == 6):
                        board.board.game_board[fila][columna] = bishoop.bishoop(
                            "white", [fila, columna], "bishoop")  # alfil
                    if (columna == 4):
                        board.board.game_board[fila][columna] = queen.queen(
                            "white", [fila, columna], "queen")  # reina
                    if (columna == 5):
                        board.board.game_board[fila][columna] = pieces.king(
                            "white", [fila, columna], "king")  # rey

                if (fila == 7):
                    board.board.game_board[fila][columna] = pieces.pawn(
                        "white", [fila, columna], "pawn")  # peones

    def allay_pieces(self, team):
        # Verifica si una pieza es aliada o no
        array = []

        for x in range(1, 9):
            for y in range(1, 9):

                if isinstance(board.board.game_board[x][y], pieces.piece) is True and board.board.game_board[x][y].team == team:

                    array.append(board.board.game_board[x][y])

        return array

    def enemy_pieces(self, team):
        # Verifica si una pieza es enemiga
        array = []

        for x in range(1, 9):
            for y in range(1, 9):

                if isinstance(board.board.game_board[x][y], pieces.piece) is True and board.board.game_board[x][y].team != team:

                    array.append(board.board.game_board[x][y])

        return array

board_function = board_function()
# END OF THE BOARD
