import menu

turn = 0
team = ["white", "black"]
minus = ["a", "b", "c", "d", "e", "f", "g", "h"]


def is_it_possible(pos):

    for Fstring in menu.pieces.board.positionY:

        for Sstring in range(1, 9):

            Sstring = str(Sstring)
            string = Fstring + Sstring

            if pos == string:

                return True

    return False


while True:

    if turn == 2:
        turn = 0

    # CLEAR
    print("It's the turn for the ", team[turn], " team")
    menu.pieces.board.show()
    print("Select the position of the piece that you want to move: ")
    piece_select = input()

    if piece_select[0] in minus:
        piece_select = chr(ord(piece_select[0]) - 32) + piece_select[1]

    if is_it_possible(piece_select) is False:
        # CLEAR
        print("That position doesn't exist or you put the position wrong")
        continue

    position_name = piece_select
    piece_select = menu.pieces.board.game_board[int(
        piece_select[1])][menu.pieces.board.positionY[piece_select[0]]]

    if piece_select.team != team[turn]:
        # CLEAR
        print("This piece is of the other team, please select one that you can take")

    elif isinstance(piece_select, menu.pieces.piece) is True:

        while True:

            print("You select a ", piece_select.name, " in the positon ", position_name)
            print("Digit the position where you want to move it: (If you put 0 you can return to select another piece)")
            move_to = input()

            if is_it_possible(move_to) is False:

                if move_to == "0":
                    print("You decide to change the piece, player from team ", team[turn])
                    break

                else:
                    print(
                        "That position doesn't exist, please select a valid position, player from team ", team[turn])
                    continue

            else:

                if isinstance(piece_select.move(menu.pieces.board, move_to), str) is True:
                    # CLEAR
                    print(piece_select.move(menu.pieces.board, move_to))
                    menu.pieces.board.show()
                    continue

                else:

                    menu.pieces.piece_select.move(menu.pieces.board, move_to)
                    turn += 1
                    break

    else:

        print("That is not a piece, please select again")
