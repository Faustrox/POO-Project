import pieces

# board = [[" ", "A", "B", "C", "D", "E", "F", "G", "H"],
#          ["1", "R", "K", "B", "Q", "Kg", "B", "K", "R"],
#          ["2", "p", "p", "p", "p", "p", "p", "p", "p"],
#          ["3", "O", "*", "O", "*", "O", "*", "O", "*"],
#          ["4", "*", "O", "*", "O", "*", "O", "*", "O"],
#          ["5", "O", "*", "O", "*", "O", "*", "O", "*"],
#          ["6", "*", "O", "*", "O", "*", "O", "*", "O"],
#          ["7", "p", "p", "p", "p", "p", "p", "p", "p"],
#          ["8", "R", "K", "B", "Q", "Kg", "B", "K", "R"]]
#
#
# for entry in board:
#     print(entry)

# TRASH FILL
# # entra los peones, de ambos equipos.
# for fila in range(1, 3):
#     for columna in range(1, 9):
#         if (fila == 1):
#             if (columna == 1 or columna == 8):
#                 self.board[fila][columna] = rook(
#                     "white", [fila, columna])  # torres
#             if (columna == 2 or columna == 7):
#                 self.board[fila][columna] = knight(
#                     "white", [fila, columna])  # caballo de trolla
#             if (columna == 3 or columna == 6):
#                 self.board[fila][columna] = bishoop(
#                     "white", [fila, columna])  # alfil
#             if (columna == 4):
#                 self.board[fila][columna] = queen(
#                     "white", [fila, columna])  # reina
#             if (columna == 5):
#                 self.board[fila][columna] = king(
#                     "white", [fila, columna])  # rey
#         if (fila == 2):
#             self.board[fila][columna] = pawn(
#                 "white", [fila, columna])  # peones
#
# for fila in range(7, 9):
#     for columna in range(1, 9):
#         if (fila == 8):
#             if (columna == 1 or columna == 8):
#                 self.board[fila][columna] = rook(
#                     "black", [fila, columna])  # torres
#             if (columna == 2 or columna == 7):
#                 self.board[fila][columna] = knight(
#                     "black", [fila, columna])  # caballo
#             if (columna == 3 or columna == 6):
#                 self.board[fila][columna] = bishoop(
#                     "black", [fila, columna])  # alfil
#             if (columna == 5):
#                 self.board[fila][columna] = queen(
#                     "black", [fila, columna])  # reina
#             if (columna == 4):
#                 self.board[fila][columna] = king(
#                     "black", [fila, columna])  # rey
#
#         if (fila == 7):
#             self.board[fila][columna] = pawn(
#                 "black", [fila, columna])  # peones


# When someone insert 0 to the destination it gonna comeback to select other piece


# position = {"A": {1: [1, 1], 2: [1, 2], 3: [1, 3], 4: [1, 4], 5: [1, 5], 6: [1, 6], 7: [1, 7], 8: [1, 8]},
#             "B": {1: [2, 1], 2: [2, 2], 3: [2, 3], 4: [2, 4], 5: [2, 5], 6: [2, 6], 7: [2, 7], 8: [2, 8]},
#             "C": {1: [3, 1], 2: [3, 2], 3: [3, 3], 4: [3, 4], 5: [3, 5], 6: [3, 6], 7: [3, 7], 8: [3, 8]},
#             "D": {1: [4, 1], 2: [4, 2], 3: [4, 3], 4: [4, 4], 5: [4, 5], 6: [4, 6], 7: [4, 7], 8: [4, 8]},
#             "E": {1: [5, 1], 2: [5, 2], 3: [5, 3], 4: [5, 4], 5: [5, 5], 6: [5, 6], 7: [5, 7], 8: [5, 8]},
#             "F": {1: [6, 1], 2: [6, 2], 3: [6, 3], 4: [6, 4], 5: [6, 5], 6: [6, 6], 7: [6, 7], 8: [6, 8]},
#             "G": {1: [7, 1], 2: [7, 2], 3: [7, 3], 4: [7, 4], 5: [7, 5], 6: [7, 6], 7: [7, 7], 8: [7, 8]},
#             "H": {1: [8, 1], 2: [8, 2], 3: [8, 3], 4: [8, 4], 5: [8, 5], 6: [8, 6], 7: [8, 7], 8: [8, 8]}}
#
# print(position["H"][2])
# # Tabla vacia

# board_Empty = [[" \t", "A", "B", "C", "D", "E", "F", "G", "H\n"],
#                ["1\t", "■", " ", "■", " ", "■", " ", "■", " "],
#                ["2\t", " ", "■", " ", "■", " ", "■", " ", "■"],
#                ["3\t", "■", " ", "■", " ", "■", " ", "■", " "],
#                ["4\t", " ", "■", " ", "■", " ", "■", " ", "■"],
#                ["5\t", "■", " ", "■", " ", "■", " ", "■", " "],
#                ["6\t", " ", "■", " ", "■", " ", "■", " ", "■"],
#                ["7\t", "■", " ", "■", " ", "■", " ", "■", " "],
#                ["8\t", " ", "■", " ", "■", " ", "■", " ", "■"]]
# # TABLA CON LOS OBJETOS
# board_Game = [[" \t", "A", "B", "C", "D", "E", "F", "G", "H\n"],
#               ["1\t", "R", "K", "F", "K", "Q", "F", "K", "R"],
#               ["2\t", "P", "P", "P", "P", "P", "P", "P", "P"],
#               ["3\t", "■", " ", "■", " ", "■", " ", "■", " "],
#               ["4\t", " ", "■", " ", "■", " ", "■", " ", "■"],
#               ["5\t", "■", " ", "■", " ", "■", " ", "■", " "],
#               ["6\t", " ", "■", " ", "■", " ", "■", " ", "■"],
#               ["7\t", "P", "P", "P", "P", "P", "P", "P", "P"],
#               ["8\t", "R", "K", "F", "Q", "K", "F", "K", "R"]]
# # WHITE AND BLACK
#
# if board[x][y] == "pawn":
#     # fix pawn moves. possible moves
#     possible_move.append([[x + 1], [y]])
#
#     # if the pawn is in the second possible_move
#     try:
#         if board[x + 2][y] == " " and x == 1 and board[x + 1][y] == "":
#             possible_move.append([[x + 2], [y]])
#
#         pass
#
#     try:
#         if board[pos1 + 1][pos2 + 1][0] == "":
#             possible_move.append([x + 1], [y + 1])
#
#         pass
#
#     try:
#         if board[x + 1][y - 1][0] == "":
#             possible_move.append([x + 1], [y - 1])
#             pass

# dic = {"pawn": {}}
#
# dic["pawn"][1] = "HOLA"
#
# print(dic["pawn"][1])

# positionY = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
#
# print(board_Game[7][positionY["A"]])
#
# print(positionY.len())
#
#
# print(black["pawn"][1].pos)

# black["pawn"][1].pos = [1, 4]

# pos1 = "A1"
# pos1 = [positionY[pos1[0]], int(pos1[1])]
# print(pos1)

pieces.board.fill()
pieces.board.show()

print(pieces.board.game_board[1][5].possible_move())

