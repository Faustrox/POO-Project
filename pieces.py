class board():

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
        self.kings = {"white": [], "black": []}

    def show(self):
        # Muestra los objetos en el tablero
        for entry in self.game_board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8], entry[9])

    def fill(self):  # entra las piezas(objetos) al tablero.

        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = rook(
                            "black", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = knight(
                            "black", [fila, columna], "knight")  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = bishoop(
                            "black", [fila, columna], "bishoop")  # alfil
                    if (columna == 4):
                        self.game_board[fila][columna] = queen(
                            "black", [fila, columna], "queen")  # reina
                    if (columna == 5):
                        self.kings["black"] = [fila, columna]
                        self.game_board[fila][columna] = king(
                            "black", [fila, columna], "king")  # rey.

                if (fila == 2):
                    self.game_board[fila][columna] = pawn(
                        "black", [fila, columna], "pawn")  # peones

        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = rook(
                            "white", [fila, columna], "rook")  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = knight(
                            "white", [fila, columna], "knight")  # caballo
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = bishoop(
                            "white", [fila, columna], "bishoop")  # alfil
                    if (columna == 5):
                        self.game_board[fila][columna] = queen(
                            "white", [fila, columna], "queen")  # reina
                    if (columna == 4):
                        self.kings["white"] = [fila, columna]
                        self.game_board[fila][columna] = king(
                            "white", [fila, columna], "king")  # rey

                if (fila == 7):
                    self.game_board[fila][columna] = pawn(
                        "white", [fila, columna], "pawn")  # peones
    
    def ally_pieces(self, team):

        array = []

        for x in self.game_board:
            for y in x:

                if isinstance(self.game_board[x][y], piece) is True and self.game_board[x][y].team == team:

                    array.append(self.game_board[x][y])

        return array

    def enemy_pieces(self, team):

        array = []

        for x in self.game_board:
            for y in x:

                if isinstance(self.game_board[x][y], piece) is True and self.game_board[x][y].team != team:

                    array.append(self.game_board[x][y])

        return array

board = board()
# END OF THE BOARD

# Pieces


class piece():

    def __init__(self, team, pos, name):
        self.positionX = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}
        self.positionY = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
        self.name = name
        self.pos = self.positionY[pos[1]] + str(pos[0])
        self.team = team

    # def eat(self, pos2):

    def move(self, pos2):

        array = self.possible_move()
        pos1 = [int(self.pos[1]), board.positionY[self.pos[0]]]
        pos2_name = pos2
        pos2 = [int(pos2[1]), board.positionY[pos2[0]]]
        piece = board.game_board[pos1[0]][pos1[1]]

        if piece == "♔" or piece == "♚":

            board.kings[piece.team] = pos1

        if pos2_name in array:

            board.game_board[pos2[0]][pos2[1]] = board.empty_board[pos2[0]][pos2[1]]
            board.game_board[pos1[0]][pos1[1]] = board.empty_board[pos1[0]][pos1[1]]
            self.pos = self.positionY[pos2[1]] + str(pos2[0])
            board.game_board[pos2[0]][pos2[1]] = piece

        elif pos2_name not in array:

            return "Hey, that position is imposible to do with this piece"

        return True


class pawn(piece):
    # Hereda los atributos de equipo y posiciones
    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)
        self.first_turn = True

    # Movimientos posibles
    def possible_move(self):

        array = []
        pos = [int(self.pos[1]), board.positionY[self.pos[0]]]
        move_RD, move_LD = False, False

        # Verifica si el jugador usa fichas negras o blancas
        if self.team == "black":
            move_forward = pos
            move_forward[0] += 1

        elif self.team == "white":
            move_forward = pos
            move_forward[0] -= 1

        # desplazamiento de las posiciones de las fichas
        if pos[1] >= 1 and pos[1] < 8:
            move_RD = [move_forward[0], move_forward[1] + 1]

        if pos[1] > 1 and pos[1] <= 8:
            move_LD = [move_forward[0], move_forward[1] - 1]

        if isinstance(board.game_board[move_forward[0]][move_forward[1]], piece) is False:

            array.append(self.positionY[move_forward[1]] + str(move_forward[0]))

            # Verifica el primer movimiento de cada peon
            if self.first_turn is True:
                self.first_turn = False
                if self.team == "black":
                    array.append(self.positionY[move_forward[1]] + str(move_forward[0] + 1))
                else:
                    array.append(self.positionY[move_forward[1]] + str(move_forward[0] - 1))

        # Verifica el movimiento diagonal para poder comer o eliminar una ficha enemiga
        if move_RD is not False:
            # derecha

            if isinstance(board.game_board[move_RD[0]][move_RD[1]], piece) is True:

                if board.game_board[move_RD[0]][move_RD[1]].team != self.team:

                    array.append(self.positionY[move_RD[1]] + str(move_RD[0]))

        if move_LD is not False:
            # Izquierda

            if isinstance(board.game_board[move_LD[0]][move_LD[1]], piece) is True:

                if board.game_board[move_LD[0]][move_LD[1]].team != self.team:

                    array.append(self.positionY[move_LD[1]] + str(move_LD[0]))

        return array

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♙"

        else:
            simbol = "♟"

        return simbol
    #     # A pawn move one step by one but in the exit it can do two step in one move.


class knight(piece):
    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)
        self.arraym = []

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♘"

        else:
            simbol = "♞"

        return simbol

    # def possible_move(self):
    #     new_pos = []
    #     pos = [board.positionY[self.pos[0]], int(self.pos[1])]
    #     posY = [[2, -1], [2, 1], [-2, 1], [-2, -1]]  # posiciones arriba y abajo del caballo
    #     posX = [[-1, 2], [1, 2], [1, -2], [-1, -2]]    # posiciones laterales
    #     for i in posY:
    #         if (isinstance(board.game_board[pos[0] + i[0]][pos[1] + i[1]], piece)) is False:
    #             if ():
    #             new_pos.append(str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))
    #         elif board.game_board[pos[0] + i[0]][pos[1] + i[1]].team != self.team:
    #             new_pos.append(str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))

    #     for i in posX:
    #         if (isinstance(board.game_board[pos[0] + i[0]][pos[1] + i[1]], piece)) is False:
    #             new_pos.append(str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))
    #         elif board.game_board[pos[0] + i[0]][pos[1] + i[1]].team != self.team:
    #             new_pos.append(str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))

    #     return new_pos


class bishoop(piece):

    def possible_move(self):

        array = []

        pos = [int(self.pos[1]), board.positionY[self.pos[0]]]
        move_LD, move_RD = pos, pos
        can_beR, can_beL = True, True

        while True:  # Diagonal to up

            move_RD = [move_RD[0] - 1, move_RD[1] + 1]
            move_LD = [move_LD[0] - 1, move_LD[1] - 1]

            if move_RD[0] > 0 and move_RD[1] < 9 and can_beR is True:

                if isinstance(board.game_board[move_RD[0]][move_RD[1]], piece) is False:

                    array.append(self.positionY[move_RD[1]] + str(move_RD[0]))

                elif board.game_board[move_RD[0]][move_RD[1]].team != self.team:

                    array.append(self.positionY[move_RD[1]] + str(move_RD[0]))
                    can_beR = False

                else:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] > 0 and move_LD[1] > 0 and can_beL is True:

                if isinstance(board.game_board[move_LD[0]][move_LD[1]], piece) is False:

                    array.append(self.positionY[move_LD[1]] + str(move_LD[0]))

                elif board.game_board[move_LD[0]][move_LD[1]].team != self.team:

                    array.append(self.positionY[move_LD[1]] + str(move_LD[0]))
                    can_beL = False

                else:
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

                if isinstance(board.game_board[move_RD[0]][move_RD[1]], piece) is False:

                    array.append(self.positionY[move_RD[1]] + str(move_RD[0]))

                elif board.game_board[move_RD[0]][move_RD[1]].team != self.team:

                    array.append(self.positionY[move_RD[1]] + str(move_RD[0]))
                    can_beR = False

                else:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] < 9 and move_LD[1] > 0 and can_beL is True:

                if isinstance(board.game_board[move_LD[0]][move_LD[1]], piece) is False:

                    array.append(self.positionY[move_LD[1]] + str(move_LD[0]))

                elif board.game_board[move_LD[0]][move_LD[1]].team != self.team:

                    array.append(self.positionY[move_LD[1]] + str(move_LD[0]))
                    can_beL = False

                else:
                    can_beL = False

            else:
                can_beL = False

            if can_beR is False and can_beL is False:

                break

        return array

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♗"

        else:
            simbol = "♝"

        return simbol


class rook(piece):
    # A rook (in spanish called tower), it can move straight but in diference of
    # a pawn is that the rook can move more than one step
    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)
        self.arraym = []  # variable que guarda las posiciones

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♖"

        else:
            simbol = "♜"

        return simbol

    def possible_move(self):
        pos = [int(self.pos[1]), board.positionY[self.pos[0]]]
        pieces_name = [pawn, knight, bishoop, rook, queen, king]

        # Movimiento Vertical
        # Movimiento Vertical Hacia arriba
        for i in range(pos[0] - 1, 0, -1):
            pos_arriba = board.game_board[i][pos[1]]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pos_arriba, pieces_name[j]) is True:
                    objecto = True
                    if self.team == "white":  # si el objeto es de diferente team se agrega su pos
                        if pos_arriba == 'black':  # de lo contrario no se agrega y se retornan la posiciones
                            self.arraym.append(str(self.positionY[pos[1]]) + str(i))
                    if self.team == "black":
                        if pos_arriba == 'white':
                            self.arraym.append(str(self.positionY[pos[1]]) + str(i))
                j += 1
            if objecto is True:
                break
            else:
                self.arraym.append(str(self.positionY[pos[1]]) + str(i))

        # Movimiento Vertical hacia abajo
        for i in range(pos[0] + 1, len(board.game_board)):
            pos_abajo = board.game_board[i][pos[1]]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pos_abajo, pieces_name[j]) is True:
                    objecto = True
                    if self.team == "white":  # si el objeto es de diferente team se agrega su pos
                        if pos_abajo == 'black':  # de lo contrario no se agrega y se retornan la posiciones
                            self.arraym.append(str(self.positionY[pos[1]]) + str(i))
                    if self.team == "black":
                        if pos_abajo == 'white':
                            self.arraym.append(str(self.positionY[pos[1]]) + str(i))
                j += 1
            if objecto is True:
                break
            else:
                self.arraym.append(str(self.positionY[pos[1]]) + str(i))

        # Movimiento Horizontal
        # movimientos horizontal a la derecha
        # for que recorre la posiciones a la derecha
        for i in range(pos[1] + 1, len(board.game_board[int(pos[1])]) - 1):
            # la variable son las posiciones en el board este caso a la izq.
            pieces_right = board.game_board[pos[0]][i]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pieces_right, pieces_name[j]) is True:
                    objecto = True
                    if self.team == "white":  # si el objeto es de diferente team se agrega su pos
                        if pieces_right == 'black':  # de lo contrario no se agrega y se retornan la posiciones
                            self.arraym.append(str(self.positionY[i]) + str(pos[0]))
                    if self.team == "black":
                        if pieces_right == 'white':
                            self.arraym.append(str(self.positionY[i]) + str(pos[0]))
                j += 1
            if objecto is True:
                break
            else:
                self.arraym.append(str(self.positionY[i]) + str(pos[0]))

        # movimientos horizontal a la izquierda
        # for que recorre la posiciones a la izquierda, el for se para cuando encuentra un objeto
        for i in range(pos[1] - 1, 0, -1):
            # la variable son las posiciones en el board este caso a la izq.
            pieces_left = board.game_board[pos[0]][i]
            j = 0
            objecto = False
            while j < len(pieces_name):
                if isinstance(pieces_left, pieces_name[j]) is True:
                    objecto = True
                    if self.team == "white":  # si el objeto es de diferente team se agrega su pos
                        if pieces_left == 'black':  # de lo contrario no se agrega y se retornan la posiciones
                            self.arraym.append(str(self.positionY[i]) + str(pos[0]))
                    if self.team == "black":
                        if pieces_left == 'white':
                            self.arraym.append(str(self.positionY[i]) + str(pos[0]))
                j += 1
            if objecto is True:
                break
            else:
                self.arraym.append(str(self.positionY[i]) + str(pos[0]))
        return self.arraym


class queen(piece):

    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)
        self.arraym = []

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♕"

        else:
            simbol = "♛"

        return simbol

    def possible_move(self):
        pos = [int(self.pos[1]), board.positionY[self.pos[0]]]
        torre = rook(self.team, [pos[1], pos[0]], "rook")
        alfil = bishoop(self.team, [pos[0], pos[1]], "bishoop")
        self.arraym = torre.possible_move() + alfil.possible_move(board)
        return self.arraym


class king(piece):

    def possible_move(self):

        array = []
        pos = [int(self.pos[1]), board.positionY[self.pos[0]]]
        container = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        for entry in container:
            move = True
            new_pos = [pos[0] + entry[0], pos[1] + entry[1]]

            if new_pos[0] > 0 and new_pos[0] < 9 and new_pos[1] > 0 and new_pos[1] < 9:

                for x in board.game_board:

                    for y in x:

                        if isinstance(board.game_board[x][y], piece) is True and board.game_board.team != self.team:

                            if new_pos in board.game_board[x][y].possible_move:

                                move = False

                    if move is True:

                        if isinstance(board.game_board[new_pos[0]][new_pos[1]], piece) is False:
                            array.append(self.positionY[new_pos[1]] + str(new_pos[0]))

                        elif board.game_board[new_pos[0]][new_pos[1]].team != self.team:
                            array.append(self.positionY[new_pos[1]] + str(new_pos[0]))

        return array

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♔"

        else:
            simbol = "♚"

        return simbol
