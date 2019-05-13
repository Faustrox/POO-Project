import board
import board_functions

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

            board.board.game_board[pos2[0]][pos2[1]] = board.board.empty_board[pos2[0]][pos2[1]]
            board.board.game_board[pos1[0]][pos1[1]] = board.board.empty_board[pos1[0]][pos1[1]]
            self.pos = self.positionY[pos2[1]] + str(pos2[0])
            board.board.game_board[pos2[0]][pos2[1]] = self_piece

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

        for enemy in board_functions.board_function.enemy_pieces(self.team):  # Estos bucles estan aqui para hacer la condicion de si el movimiento al donde puede ir el rey lo esta...
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
