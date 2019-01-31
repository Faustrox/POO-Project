class piece():

    def __init__(self, team, pos):
        self.pos = pos
        self.team = team

    def __eat(self, pos_enemy):
        print("You have been eaten the piece of the pos2")

    def move(self, board, array, pos1, pos2):

        if pos2 in array:

            if pos2 == "Piece":
                print("EAT!")

        elif pos2 not in array:

            print("Hey, that position is imposible to do with this piece")


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
            if self.first_turn = True:
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
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "Q"


class king(piece):  # PROGRESS
    def __str__(self):  # function para que no imprima en lenguaje maquina
        return "K"


pawn = pawn([1, 2], "black")

print(pawn.possible_move())
