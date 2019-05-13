import pieces  
import board
import knight
import bishoop
import queen

class rook(pieces.piece):
    # A rook (in spanish called tower), it can move straight but in diference of
    # a pawn is that the rook can move more than one step
    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♖"

        else:
            simbol = "♜"

        return simbol

    def possible_move(self):
        arraym = {"left": [], "right": [], "up": [], "down": []}
        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
        pieces_name = [pieces.pawn, knight.knight, bishoop.bishoop, rook, queen.queen, pieces.king]
        # Movimiento Vertical
        # Movimiento Vertical Hacia arriba

        for i in range(pos[0] - 1, 0, -1):
            pos_arriba = board.board.game_board[i][pos[1]]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pos_arriba, pieces_name[j]) is True:
                    objecto = True
                    if pos_arriba.name == "king" and pos_arriba.team != self.team:
                        if pos[1] < 9 and i - 1 > 0:
                            arraym["up"].append(str(self.positionY[pos[1]]) + str(i - 1))

                    arraym["up"].append(str(self.positionY[pos[1]]) + str(i))

                j += 1
            if objecto is True:
                break
            else:
                arraym["up"].append(str(self.positionY[pos[1]]) + str(i))

        # Movimiento Vertical hacia abajo
        for i in range(pos[0] + 1, len(board.board.game_board) - 2):
            pos_abajo = board.board.game_board[i][pos[1]]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pos_abajo, pieces_name[j]) is True:
                    objecto = True
                    if pos_abajo.name == "king" and pos_abajo.team != self.team:
                        print(pos[1], i + 1, i)
                        if pos[1] < 9 and i + 1 < 9 and i > 0:
                            arraym["down"].append(str(self.positionY[pos[1]]) + str(i + 1))
                    arraym["down"].append(str(self.positionY[pos[1]]) + str(i))
                j += 1
            if objecto is True:
                break
            else:
                arraym["down"].append(str(self.positionY[pos[1]]) + str(i))

        # Movimiento Horizontal
        # movimientos horizontal a la derecha
        # for que recorre la posiciones a la derecha
        for i in range(pos[1] + 1, len(board.board.game_board[int(pos[1])]) - 1):
            # la variable son las posiciones en el board este caso a la izq.
            pieces_right = board.board.game_board[pos[0]][i]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pieces_right, pieces_name[j]) is True:
                    objecto = True
                    if pieces_right.name == "king" and pieces_right.team != self.team:
                        if i + 1 < 9 and pos[0] > 0:
                            arraym["right"].append(str(self.positionY[i + 1]) + str(pos[0]))

                    arraym["right"].append(str(self.positionY[i]) + str(pos[0]))
                j += 1
            if objecto is True:
                break
            else:
                arraym["right"].append(str(self.positionY[i]) + str(pos[0]))

        # movimientos horizontal a la izquierda
        # for que recorre la posiciones a la izquierda, el for se para cuando encuentra un objeto
        for i in range(pos[1] - 1, 0, -1):
            # la variable son las posiciones en el board este caso a la izq.
            pieces_left = board.board.game_board[pos[0]][i]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pieces_left, pieces_name[j]) is True:
                    objecto = True
                    if pieces_left.name == "king" and pieces_left.team != self.team:
                        if i - 1 < 9 and i - 1 > 0 and pos[0] > 0 and pos[0] < 9:
                            arraym["left"].append(str(self.positionY[i - 1]) + str(pos[0]))
                    arraym["left"].append(str(self.positionY[i]) + str(pos[0]))
                j += 1
            if objecto is True:
                break
            else:
                arraym["left"].append(str(self.positionY[i]) + str(pos[0]))
        return arraym