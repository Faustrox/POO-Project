import board
# Pieces


class piece():
    # Clase principal de las piezas
    def __init__(self, team, pos, name):
        self.positionX = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}
        self.positionY = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
        self.name = name
        self.pos = self.positionY[pos[1]] + str(pos[0])
        self.team = team
        self.pos_after_king = False

    def move(self, pos2):
        # Define los movimientos
        pos1 = [int(self.pos[1]), board.board.positionY[self.pos[0]]]

        if isinstance(self, king) is False:

            array = []
            dic = self.possible_move()

            for entry in dic:

                array += dic[entry]

        else:

        array = self.possible_move()

        pos2_name = pos2
        pos2 = [int(pos2[1]), board.board.positionY[pos2[0]]]
        self_piece = board.board.game_board[pos1[0]][pos1[1]]
        
        if self_piece == "♔" or self_piece == "♚":

            board.board.kings[self_piece.team] = pos1

        if pos2_name in array:

            if isinstance(board.board.game_board[pos2[0]][pos2[1]], piece) is True and board.board.game_board[pos2[0]][pos2[1]].team != self.team:

                enemy = board.board.game_board[pos2[0]][pos2[1]]
                board.board.real_graveyard[enemy.team].append(enemy)
                board.board.graveyard[enemy.team].append(enemy.__str__())

            elif isinstance(board.board.game_board[pos2[0]][pos2[1]], piece) is True and board.board.game_board[pos2[0]][pos2[1]].team == self.team:

                return "Hey, you can't eat your own pieces"

            if self.pos_after_king != False:

                return "Hey, that position is imposible to do with this piece"

            board.game_board[pos2[0]][pos2[1]] = board.board.empty_board[pos2[0]][pos2[1]]
            board.game_board[pos1[0]][pos1[1]] = board.board.empty_board[pos1[0]][pos1[1]]
            self.pos = self.positionY[pos2[1]] + str(pos2[0])
            board.game_board[pos2[0]][pos2[1]] = self_piece

        elif pos2_name not in array:

            return "Hey, that position is imposible to do with this piece"

        if isinstance(self, pawn) is True:

            self.switch()

        return True


class pawn(piece):
    # Hereda los atributos de equipo y posiciones
    def __init__(self, pos, team, name):
        super().__init__(pos, team, name)
        self.first_turn = True

    def possible_move(self):
        # Movimientos posibles
        dic = {"Forward": [], "Right": [], "Left": []}
        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
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

        if isinstance(board.board.game_board[move_forward[0]][move_forward[1]], piece) is False:

            dic["Forward"].append(self.positionY[move_forward[1]] + str(move_forward[0]))

            # Verifica el primer movimiento de cada peon

            if self.pos[1] == "2" and self.team == "black":
                dic["Forward"].append(self.positionY[move_forward[1]] + str(move_forward[0] + 1))
            elif self.pos[1] == "7" and self.team == "white":
                dic["Forward"].append(self.positionY[move_forward[1]] + str(move_forward[0] - 1))

        # Verifica el movimiento diagonal para poder comer o eliminar una ficha enemiga
        if move_RD is not False:
            # derecha

            if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], piece) is True:

                dic["Right"].append(self.positionY[move_RD[1]] + str(move_RD[0]))

        if move_LD is not False:
            # Izquierda

            if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], piece) is True:

                dic["Left"].append(self.positionY[move_LD[1]] + str(move_LD[0]))

        return dic

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♙"

        else:
            simbol = "♟"

        return simbol
    #     # A pawn move one step by one but in the exit it can do two step in one move.

    def switch(self): # Funcion del peon para cambiar de pieza si llega a la base enemiga

        if self.team == "white":

            destination = 1

        else:

            destination = 8

        if int(self.pos[1]) == destination:
            pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
            while True:

                print("You arrive to the enemy base!")
                print("You can switch to a piece what you want")
                print("Select one of this:", ["♞", "♝"])
                select_piece = input("Uno o Dos\n")
                select_piece = int(select_piece) - 1
                print(pos)
                knight_1 = knight(self.team, [pos[0], pos[1]], "knight")
                bishoop_1 = bishoop(self.team, [pos[0], pos[1]], "bishoop")
                if select_piece == 0:
                    board.board.game_board[pos[0]][pos[1]] = knight_1
                if select_piece == 1:
                    board.board.game_board[pos[0]][pos[1]] = bishoop_1
                break
        else:

            return False


class knight(piece):
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
            if (isinstance(board.board.game_board[pos[0] + i[0]][pos[1] + i[1]], piece)) is False:
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
            if (isinstance(board.board.game_board[pos[0] + i[0]][pos[1] + i[1]], piece)) is False:
                new_pos["left and right"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))
            # Movement enemy possible
            elif board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team != self.team or board.board.game_board[pos[0] + i[0]][pos[1] + i[1]].team == self.team:
                new_pos["left and right"].append(
                    str(self.positionY[pos[1] + i[1]]) + str(pos[0] + i[0]))

        return new_pos


class bishoop(piece):
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

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], king) is True: # Condicion para saber si el movimiento al donde va es un Rey.
                    move_RD2 = [move_RD[0] - 1, move_RD[1] + 1]
                    # Si es un rey entonces en el diccionario se añadira un paso mas despues del rey
                    if move_RD2[0] > 0 and move_RD2[1] < 9:
                        self.pos_after_king = self.positionY[move_RD2[1]] + str(move_RD2[0])

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], piece) is True:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] > 0 and move_LD[1] > 0 and can_beL is True:

                dic["LeftF"].append(self.positionY[move_LD[1]] + str(move_LD[0]))

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], king) is True: # Condicion para saber si el movimiento al donde va es un Rey.
                    move_LD2 = [move_LD[0] - 1, move_LD[1] - 1]
                    # Si es un rey entonces en el diccionario se añadira un paso mas despues del rey
                    if move_LD2[0] > 0 and move_LD2[1] > 0:
                        self.pos_after_king = self.positionY[move_LD2[1]] + str(move_LD2[0])

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], piece) is True:
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

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], king) is True:
                    move_RD2 = [move_RD[0] + 1, move_RD[1] + 1]
                    if move_RD2[0] < 9 and move_RD2[1] < 9:
                        self.pos_after_king = self.positionY[move_RD2[1]] + str(move_RD2[0])

                if isinstance(board.board.game_board[move_RD[0]][move_RD[1]], piece) is True:
                    can_beR = False

            else:
                can_beR = False

            if move_LD[0] < 9 and move_LD[1] > 0 and can_beL is True:

                dic["LeftB"].append(self.positionY[move_LD[1]] + str(move_LD[0]))

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], king) is True:
                    move_LD2 = [move_LD[0] + 1, move_LD[1] - 1]
                    if move_LD[0] < 9 and move_LD[1] > 0:
                        self.pos_after_king = self.positionY[move_LD2[1]] + str(move_LD2[0])

                if isinstance(board.board.game_board[move_LD[0]][move_LD[1]], piece) is True:
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


class rook(piece):
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
        pieces_name = [pawn, knight, bishoop, rook, queen, king]
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


class queen(piece):
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
        torre = rook(self.team, [pos[0], pos[1]], "rook")
        alfil = bishoop(self.team, [pos[0], pos[1]], "bishoop")
        for i in torre.possible_move():
            arraym[i] = torre.possible_move()[i]
        for i in alfil.possible_move():
            arraym[i] = alfil.possible_move()[i]
        return arraym


class king(piece):
    # Rey
    def possible_move(self): # Funcion que imprime los movimientos posibles

        array = []
        pos = [int(self.pos[1]), board.board.positionY[self.pos[0]]]
        container = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]] # Los pasos que puede hacer el rey en una matriz

        for entry in container:
            move = True
            new_pos = [pos[0] + entry[0], pos[1] + entry[1]]

            if new_pos[0] > 0 and new_pos[0] < 9 and new_pos[1] > 0 and new_pos[1] < 9:

                if isinstance(board.board.game_board[new_pos[0]][new_pos[1]], piece) is False:
                    array.append(self.positionY[new_pos[1]] + str(new_pos[0]))

                else:
                    array.append(self.positionY[new_pos[1]] + str(new_pos[0]))

        for enemy in board.board.enemy_pieces(self.team):  # Estos bucles estan aqui para hacer la condicion de si el movimiento al donde puede ir el rey lo esta...
            # ...apuntando, entonces que se borre ya que seria un movimiento invalido

            if enemy.pos_after_king != False:

                if enemy.pos_after_king in array:

                    array.remove(enemy.pos_after_king)

            if type(enemy) == king:

                continue

            for way in enemy.possible_move():

                for move in enemy.possible_move()[way]:

                    if move in array:

                        array.remove(move)

        return array

    def __str__(self):  # function para que no imprima en lenguaje maquina

        if self.team == "white":
            simbol = "♔"

        else:
            simbol = "♚"

        return simbol
