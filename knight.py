import pieces
import board

class knight(pieces.piece):
    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♘"

        else:
            simbol = "♞"

        return simbol

    def possible_move(self):
        new_pos = {"left and right": [], "up and down": []}
        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
        posY = [[2, -1], [2, 1], [-2, 1], [-2, -1]]  # posiciones arriba y abajo del caballo
        posX = [[-1, 2], [1, 2], [1, -2], [-1, -2]]    # posiciones laterales
        for i in posY:
            if pos[1] + i[1] < 1 or pos[1] + i[1] > 8:
                continue
            if pos[0] + i[0] < 1 or pos[0] + i[0] > 8:
                continue
            if (isinstance(board.board.game_board[pos[0] + i[0]][pos[1] + i[1]], pieces.piece)) is False:
                new_pos["up and down"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))
            # Movement enemy possible
            elif board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team != self.team or board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team == self.team:
                new_pos["up and down"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))

        for i in posX:
            if pos[1] + i[1] < 1 or pos[1] + i[1] > 8:
                continue
            if pos[0] + i[0] < 1 or pos[0] + i[0] > 8:
                continue
            if (isinstance(board.board.game_board[pos[0] + i[0]][pos[1] + i[1]], pieces.piece)) is False:
                new_pos["left and right"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))
            # Movement enemy possible
            elif board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team != self.team or board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team == self.team:
                new_pos["left and right"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))

        return new_pos
