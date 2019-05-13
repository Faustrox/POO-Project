import pieces
import board

class bishoop(pieces.piece):
    # Alfil
    def possible_move(self): # Funcion para hacer los posibles movimientos del alfil

        dic = {"RightF": [], "LeftF": [], "RightB": [], "LeftB": []} # Diccionario que tendra todas las trayectorias del alfil

        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
        move_LD, move_RD = pos, pos
        can_beR, can_beL = True, True

        while True:  # Diagonal to up

            move_RD = [move_RD[0] - 1, move_RD[1] + 1]
            move_LD = [move_LD[0] - 1, move_LD[1] - 1]

            if move_RD[0] > 0 and move_RD[1] < 9 and can_beR is True:

                dic["RightF"].append(self.positionY[move_RD[1]] + str(move_RD[0]))

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], pieces.king) is True: # Condicion para saber si el movimiento al donde va es un Rey.
                    move_RD2 = [move_RD[0] - 1, move_RD[1] + 1]
                    # Si es un rey entonces en el diccionario se añadira un paso mas despues del rey
                    if move_RD2[0] > 0 and move_RD2[1] < 9:
                        self.pos_after_king = self.positionY[move_RD2[1]] + str(move_RD2[0])

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], pieces.piece) is True:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] > 0 and move_LD[1] > 0 and can_beL is True:

                dic["LeftF"].append(self.positionY[move_LD[1]] + str(move_LD[0]))

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], pieces.king) is True: # Condicion para saber si el movimiento al donde va es un Rey.
                    move_LD2 = [move_LD[0] - 1, move_LD[1] - 1]
                    # Si es un rey entonces en el diccionario se añadira un paso mas despues del rey
                    if move_LD2[0] > 0 and move_LD2[1] > 0:
                        self.pos_after_king = self.positionY[move_LD2[1]] + str(move_LD2[0])

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], pieces.piece) is True:
                    can_beL = False

            else:
                can_beL = False

            if can_beR is False and can_beL is False:

                break

        move_LD, move_RD = pos, pos
        can_beR, can_beL = True, True

        while True:  # Diagonal to down

            move_RD = [move_RD[0] + 1, move_RD[1] + 1]
            move_LD = [move_LD[0] + 1, move_LD[1] - 1]

            if move_RD[0] < 9 and move_RD[1] < 9 and can_beR is True:

                dic["RightB"].append(self.positionY[move_RD[1]] + str(move_RD[0]))

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], pieces.king) is True:
                    move_RD2 = [move_RD[0] + 1, move_RD[1] + 1]
                    if move_RD2[0] < 9 and move_RD2[1] < 9:
                        self.pos_after_king = self.positionY[move_RD2[1]] + str(move_RD2[0])

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], pieces.piece) is True:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] < 9 and move_LD[1] > 0 and can_beL is True:

                dic["LeftB"].append(self.positionY[move_LD[1]] + str(move_LD[0]))

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], pieces.king) is True:
                    move_LD2 = [move_LD[0] + 1, move_LD[1] - 1]
                    if move_LD[0] < 9 and move_LD[1] > 0:
                        self.pos_after_king = self.positionY[move_LD2[1]] + str(move_LD2[0])

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], pieces.piece) is True:
                    can_beL = False

            else:
                can_beL = False

            if can_beR is False and can_beL is False:

                break

        return dic

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♗"

        else:
            simbol = "♝"

        return simbol
