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

        self.positionY = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}

    def show(self):
        for entry in self.board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])

    def fill(self):  # entra las piezas(objetos) al tablero.

        white = {"pawns": {}, "knight": {}, "bishoop": {}, "rook": {}, "queen": {}, "king": {}}
        black = {"pawns": {}, "knight": {}, "bishoop": {}, "rook": {}, "queen": {}, "king": {}}
        number = 1

        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        if 1 not in black["rook"]:
                            number = 1
                        else:
                            number = 2
                        self.board[fila][columna] = "R"  # torres
                        black["rook"][number] = rook("black", [fila, columna])  # torres

                    if (columna == 2 or columna == 7):
                        if 1 not in black["knight"]:
                            number = 1
                        else:
                            number = 2

                        self.board[fila][columna] = "K"  # torres
                        black["knight"][number] = knight(
                            "black", [fila, columna])  # caballo de trolla

                    if (columna == 3 or columna == 6):
                        if 1 not in black["bishoop"]:
                            number = 1
                        else:
                            number = 2

                        self.board[fila][columna] = "B"  # torres
                        black["bishoop"][number] = bishoop("black", [fila, columna])  # alfil

                    if (columna == 4):
                        self.board[fila][columna] = "Q"  # torres
                        black["queen"][1] = queen("black", [fila, columna])   # reina

                    if (columna == 5):
                        self.board[fila][columna] = "K"  # torres
                        black["king"][1] = king("black", [fila, columna])  # rey

                if (fila == 2):
                    self.board[fila][columna] = "P"  # torres
                    black["pawns"][columna] = pawn("black", [fila, pawn])  # peones

        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        if 1 not in black["rook"]:
                            number = 1
                        else:
                            number = 2

                        self.board[fila][columna] = "R"  # torres
                        white["rook"][number] = rook("white", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        if 1 not in black["knight"]:
                            number = 1
                        else:
                            number = 2

                        self.board[fila][columna] = "K"  # torres
                        white["knight"][number] = knight(
                            "white", [fila, columna])  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        if 1 not in black["bishoop"]:
                            number = 1
                        else:
                            number = 2

                        self.board[fila][columna] = "B"  # torres
                        white["bishoop"][number] = bishoop("white", [fila, columna])  # alfil
                    if (columna == 4):
                        self.board[fila][columna] = "Q"  # torres
                        white["queen"][1] = queen("white", [fila, columna])   # reina

                    if (columna == 5):
                        self.board[fila][columna] = "K"  # torres
                        white["king"][1] = king("white", [fila, columna])  # rey

                if (fila == 7):
                    self.board[fila][columna] = "P"  # torres
                    white["pawns"][columna] = pawn("white", [fila, pawn])  # peones


board = board()
# END OF THE BOARD

# Pieces


class piece():

    def __init__(self, team, pos):
        self.pos = pos
        self.team = team

        self.positionX = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}
        self.positionY = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}

    def __eat(self, pos_enemy):
        print("You have been eaten the piece of the pos2")

    def move(self, board, array, pos1, pos2):

        if pos2 in array:

            if board[pos2] != " " or board[pos2] != "■":
                # It's a piece, can eat
                __eat(pos2)

            self.pos = pos2

            # PROGRESS

        elif pos2 not in array:

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
                    if (isinstance(j, pieces_name[k])) == True:
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

    def __init__(self, pos, team):
        super().__init__(pos, team)
        self.first_turn = True

    def possible_move(self):
        array = []

        if self.team == "black":
            possible = self.pos
            possible[1] += 1
            array.append(possible)

            if self.first_turn is True:
                possible[1] += 1
                array.append(possible)

        if self.team == "white":
            possible = self.pos
            possible[1] -= 1
            array.append(possible)

            if self.first_turn is True:
                possible[1] -= 1
                array.append(possible)
        return array

    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "P"
    #     # A pawn move one step by one but in the exit it can do two step in one move.


class knight(piece):
    # A knight (in spanish called horse), it can do a move of L in any directions
    # A knight can... like jump others pieces
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "K"


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


piece = piece("white", [1, 1])

board.fill()
print(piece.move_posible())
