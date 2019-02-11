class board():

    def __init__(self):
        # Diseno del tablero donde iran las piezas
        self.game_board = [[" \t", "A", "B", "C", "D", "E", "F", "G", "H\n"],
                           ["1\t", "■", " ", "■", " ", "■", " ", "■", " "],
                           ["2\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                           ["3\t", "■", " ", "■", " ", "■", " ", "■", " "],
                           ["4\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                           ["5\t", "■", " ", "■", " ", "■", " ", "■", " "],
                           ["6\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                           ["7\t", "■", " ", "■", " ", "■", " ", "■", " "],
                           ["8\t", " ", "■", " ", "■", " ", "■", " ", "■"]]
        # Dise
        self.empty_board = [[" \t", "A", "B", "C", "D", "E", "F", "G", "H\n"],
                            ["1\t", "■", " ", "■", " ", "■", " ", "■", " "],
                            ["2\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                            ["3\t", "■", " ", "■", " ", "■", " ", "■", " "],
                            ["4\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                            ["5\t", "■", " ", "■", " ", "■", " ", "■", " "],
                            ["6\t", " ", "■", " ", "■", " ", "■", " ", "■"],
                            ["7\t", "■", " ", "■", " ", "■", " ", "■", " "],
                            ["8\t", " ", "■", " ", "■", " ", "■", " ", "■"]]
        # Se le da valor a las posiciones para leer las columnas
        self.positionY = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

    def show(self):
        # Muestra los objetos en el tablero
        for entry in self.game_board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])

    def fill(self):  # entra las piezas(objetos) al tablero.

        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = rook(
                            "black", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = knight(
                            "black", [fila, columna])  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = bishoop(
                            "black", [fila, columna])  # alfil
                    if (columna == 4):
                        self.game_board[fila][columna] = queen(
                            "black", [fila, columna])  # reina
                    if (columna == 5):
                        self.game_board[fila][columna] = king(
                            "black", [fila, columna])  # rey
                if (fila == 2):
                    self.game_board[fila][columna] = pawn(
                        "black", [fila, columna])  # peones

        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.game_board[fila][columna] = rook(
                            "white", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.game_board[fila][columna] = knight(
                            "white", [fila, columna])  # caballo
                    if (columna == 3 or columna == 6):
                        self.game_board[fila][columna] = bishoop(
                            "white", [fila, columna])  # alfil
                    if (columna == 5):
                        self.game_board[fila][columna] = queen(
                            "white", [fila, columna])  # reina
                    if (columna == 4):
                        self.game_board[fila][columna] = king(
                            "white", [fila, columna])  # rey

                if (fila == 7):
                    self.game_board[fila][columna] = pawn(
                        "white", [fila, columna])  # peones


board = board()
# END OF THE BOARD

# Pieces


class piece():

    def __init__(self, team, pos):
        self.positionX = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}
        self.positionY = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}
        self.pos = self.positionY[pos[1]] + str(pos[0])
        self.team = team

    # def eat(self, pos2):

    def move(self, board, array, pos2):

        pos1 = [int(self.pos[1]), board.positionY[self.pos[0]]]
        pos2_name = pos2
        pos2 = [int(pos2[1]), board.positionY[pos2[0]]]
        piece = board.game_board[pos1[0]][pos1[1]]

        if pos2_name in array:

            board.game_board[pos1[0]][pos1[1]] = board.empty_board[pos1[0]][pos1[1]]
            self.pos = pos2
            board.game_board[self.pos[0]][self.pos[1]] = piece

        elif pos2_name not in array:

            print("Hey, that position is imposible to do with this piece")

    def move_posible(self):
        pieces_name = [pawn, knight, bishoop, rook, queen, king]
        array = []

        # return movimientos imposibles ya que no puedes-
        # ocupar el espacio de una ficha de tu mismo team

        for i in board.board:
            for j in i:
                k = 0
                while k <= 5:
                    if (isinstance(j, pieces_name[k])) is True:
                        if j.team == "white":
                            print("hola")
                            array.append(self.positionY[j.pos[1]] + self.positionX[j.pos[0]])
                    k += 1
<<<<<<< HEAD
            
        return array      
    
                    
=======
        return array


>>>>>>> cd75f90d7d9f7aeb05598de5e32effaea5047f64
class pawn(piece):
    # Hereda los atributos de equipo y posiciones
    def __init__(self, pos, team):
        super().__init__(pos, team)
        self.first_turn = True

    # Movimientos posibles
    def possible_move(self, board):
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
        if pos[0] >= 1 and pos[0] >= 8:
            move_RD = [move_forward[0], move_forward[1] + 1]

        if pos[0] <= 8 and pos[0] >= 1:
            move_LD = [move_forward[0], move_forward[1] - 1]

        if isinstance(board.game_board[move_forward[0]][move_forward[1]], piece) is False:

            array.append(self.positionY[move_forward[1]] + str(move_forward[0]))

            # Verifica el primer movimiento de cada peon
            if self.first_turn is True:
                self.first_turn = False
                array.append(self.positionY[move_forward[1]] + str(move_forward[0] + 1))

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
        return "P"
    #     # A pawn move one step by one but in the exit it can do two step in one move.


class knight(piece):
    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "H"


class bishoop(piece):
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "B"


class rook(piece):
    # A rook (in spanish called tower), it can move straight but in diference of
    # a pawn is that the rook can move more than one step

    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "R"


class queen(piece):

    def __init__(self, pos, team):
        super().__init__(pos, team)

    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "Q"

    def posible_move(self):
        piece.move_posible()


class king(piece):  # PROGRESS
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "K"
