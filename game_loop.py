import menu

turn = 0
team = ["white", "black"]

while True:

    # CLEAR
    print("It's the turn for the ", team[turn], " team")
    menu.pieces.board.show()
    print("Select the position of the piece that you want to move: ")
    piece_select = input()
    piece_select = menu.pieces.board.game_board[int(piece_select[0])][menu.pieces.piece.positionY[piece_select[1]]

    if isinstance(piece_select, menu.pieces.piece) is True:

        while True:

            print("You select: ", piece_select.name, " in the positon ", piece_select)
            print("Digit the position where you want to move it: (If you put 0 you can return to select another piece)")
            move_to = input()

            if int(move_to) == 0:
                break

            else:

                if isinstance(menu.pieces.piece_select.move(menu.pieces.board, move_to), str) is True:
                    # CLEAR
                    print(menu.pieces.piece_select.move(menu.pieces.board, move_to))
                    menu.pieces.board.show()
                    continue

                else:

                    menu.pieces.piece_select.move(menu.pieces.board, move_to)

        if int(move_to) == 0:
            continue

    else:

        print("That is not a piece, please select again")

    turn += 1
