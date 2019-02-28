import menu

piece = menu.pieces.piece
turn = 0
team = ["white", "black"]
minus = ["a", "b", "c", "d", "e", "f", "g", "h"]


def check(team):

    first = False
    second = False
    third = False
    
    ally_pieces = menu.pieces.board.ally_pieces(team)
    for piece in ally_pieces:

        if isinstance(piece, menu.pieces.king) is True:

            allay_king = piece


    for enemy_piece in menu.pieces.enemy_pieces(team):

        if allay_king.pos in enemy_piece.possibe_move:

            first = True

            for ally_piece in ally_pieces:

                if enemy_piece.pos in ally_piece.possible_move:

                    third = True
        
        if len(allay_king.possible_move) > 0:

            second = True


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

    print("It's the turn for the ", team[turn], " team")
    menu.pieces.board.show()
    print("Select the position of the piece that you want to move: ")
    piece_select = input()

    if piece_select[0] in minus:
        piece_select = chr(ord(piece_select[0]) - 32) + piece_select[1]

    if is_it_possible(piece_select) is False:
        menu.cls()
        print("That position doesn't exist or you put the position wrong")
        continue

    position_name = piece_select
    piece_select = menu.pieces.board.game_board[int(
        piece_select[1])][menu.pieces.board.positionY[piece_select[0]]]

    if isinstance(piece_select, menu.pieces.piece) is False:

        menu.cls()
        print("That isn't a piece, please select a valid piece")
        continue

    if piece_select.team != team[turn]:
        menu.cls()
        print("This piece is of the other team, please select one that you can take")
        continue

    elif isinstance(piece_select, menu.pieces.piece) is True:
        menu.cls()

        while True:


            print("It's the turn for the ", team[turn], " team")
            menu.pieces.board.show()
            print("You select a ", piece_select.name, " in the positon ", position_name)
            print("Digit the position where you want to move it: (If you put 0 you can return to select another piece)")
            move_to = input()
            move_to = str(move_to)

            if move_to[0] in minus:
                move_to = chr(ord(move_to[0]) - 32) + move_to[1]

            if is_it_possible(move_to) is False:

                if move_to == "0":
                    menu.cls()
                    print("You decide to change the piece, player from team ", team[turn])
                    break

                else:
                    menu.cls()
                    print(
                        "That position doesn't exist, please select a valid position, player from team ", team[turn])
                    continue

            else:

                if isinstance(piece_select.move(move_to), str) is True:
                    menu.cls()
                    print(piece_select.move(move_to))
                    continue

                else:

                    piece_select.move(move_to)
                    turn += 1
                    break

    else:

        print("That is not a piece, please select again")
    menu.cls()
