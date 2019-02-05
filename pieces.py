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

        self.position = {"A": {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [1, 4], 5: [1, 5], 6: [1, 6], 7: [1, 7], 8: [1, 8]},
                         "B": {1: [2, 1], 2: [2, 2], 3: [2, 3], 4: [2, 4], 5: [2, 5], 6: [2, 6], 7: [2, 7], 8: [2, 8]},
                         "C": {1: [3, 1], 2: [3, 2], 3: [3, 3], 4: [3, 4], 5: [3, 5], 6: [3, 6], 7: [3, 7], 8: [3, 8]},
                         "D": {1: [4, 1], 2: [4, 2], 3: [4, 3], 4: [4, 4], 5: [4, 5], 6: [4, 6], 7: [4, 7], 8: [4, 8]},
                         "E": {1: [5, 1], 2: [5, 2], 3: [5, 3], 4: [5, 4], 5: [5, 5], 6: [5, 6], 7: [5, 7], 8: [5, 8]},
                         "F": {1: [6, 1], 2: [6, 2], 3: [6, 3], 4: [6, 4], 5: [6, 5], 6: [6, 6], 7: [6, 7], 8: [6, 8]},
                         "G": {1: [7, 1], 2: [7, 2], 3: [7, 3], 4: [7, 4], 5: [7, 5], 6: [7, 6], 7: [7, 7], 8: [7, 8]},
                         "H": {1: [8, 1], 2: [8, 2], 3: [8, 3], 4: [8, 4], 5: [8, 5], 6: [8, 6], 7: [8, 7], 8: [8, 8]}}

    def show(self):
        for entry in self.board:
            print(entry[0], entry[1], entry[2], entry[3],
                  entry[4], entry[5], entry[6], entry[7], entry[8])

    def fill(self):  # entra las piezas(objetos) al tablero.

        # entra los peones, de ambos equipos.
        for fila in range(1, 3):
            for columna in range(1, 9):
                if (fila == 1):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = rook(
                            "white", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = knight(
                            "white", [fila, columna])  # caballo de trolla
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = bishoop(
                            "white", [fila, columna])  # alfil
                    if (columna == 4):
                        self.board[fila][columna] = queen(
                            "white", [fila, columna])  # reina
                    if (columna == 5):
                        self.board[fila][columna] = king(
                            "white", [fila, columna])  # rey
                if (fila == 2):
                    self.board[fila][columna] = pawn(
                        "white", [fila, columna])  # peones

        for fila in range(7, 9):
            for columna in range(1, 9):
                if (fila == 8):
                    if (columna == 1 or columna == 8):
                        self.board[fila][columna] = rook(
                            "black", [fila, columna])  # torres
                    if (columna == 2 or columna == 7):
                        self.board[fila][columna] = knight(
                            "black", [fila, columna])  # caballo
                    if (columna == 3 or columna == 6):
                        self.board[fila][columna] = bishoop(
                            "black", [fila, columna])  # alfil
                    if (columna == 5):
                        self.board[fila][columna] = queen(
                            "black", [fila, columna])  # reina
                    if (columna == 4):
                        self.board[fila][columna] = king(
                            "black", [fila, columna])  # rey

                if (fila == 7):
                    self.board[fila][columna] = pawn(
                        "black", [fila, columna])  # peones


board = board()
# END OF THE BOARD

# Pieces

class piece():

    def __init__(self, team, pos):
        self.pos = pos
        self.team = team
        self.positionX = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8"}
        self.positionY = {1 : "A", 2 : "B", 3 : "C", 4 : "D", 5 : "E", 6 : "F", 7 : "G", 8 : "H"}
        
        
    def __eat(self, pos_enemy):
        print("You have been eaten the piece of the pos2")

    def move(self, board, array, pos1, pos2):

        if pos2 in array:

            if pos2 == "Piece":
                print("EAT!")

        elif pos2 not in array:

            print("Hey, that position is imposible to do with this piece")

    def move_posible(self):
        pieces_name = [pawn, knight, bishoop, rook, queen, king]
        array = []
        #return movimientos imposibles ya que no puedes-
        #ocupar el espacio de una ficha de tu mismo team    
        for i in board.board:
            for j in i:
                k = 0
                while k <= 5:
                    if (isinstance(j,pieces_name[k])) == True:
                        if j.team == "white":
                            array.append(self.positionY[j.pos[1]] + self.positionX[j.pos[0]])
                    k += 1        
        return array      
    
                    
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

piece = piece("white", [1,1])
board.fill()
print(piece.move_posible())
