import menu

piece = menu.pieces.piece
turn = 0
team = ["white", "black"]
minus = ["a", "b", "c", "d", "e", "f", "g", "h"]


def check(team):

    first = False
    second = False
    third = False
    check = False
    
    allay_pieces = menu.pieces.board.allay_pieces(team)
    for piece in allay_pieces:

        if isinstance(piece, menu.pieces.king) is True:

            allay_king = piece
            break

    for enemy_piece in menu.pieces.board.enemy_pieces(team):
        
        if isinstance(enemy_piece, menu.pieces.king) is True:
            continue
        
        enemy_possible = enemy_piece.possible_move()
        for enemy_way in enemy_possible:
            
            if allay_king.pos in enemy_possible[enemy_way]:

                print(enemy_piece)

                check = True
 
                for allay_piece in allay_pieces:

                    if type(allay_piece) == menu.pieces.king:
                        continue

                    allay_possible = allay_piece.possible_move()
                    
                    for allay_way in allay_possible:

                        if enemy_piece.pos in allay_possible[allay_way]:

                            first = True

                        for array_move in allay_possible[allay_way]:

                            for allay_move in array_move:

                                if allay_move in enemy_possible[enemy_way] and allay_king.pos in enemy_possible[enemy_way]:

                                    third = True
                                    break

    if check is True:

        can = False

        for pos in allay_king.possible_move():

            pos = [int(pos[1]), menu.pieces.board.positionY[pos[0]]]

            if isinstance(menu.pieces.board.game_board[pos[0]][pos[1]], menu.pieces.piece) is False:
                print("HEY")
                can = True
                break

            elif type(menu.pieces.board.game_board[pos[0]][pos[1]]) == piece and menu.pieces.board.game_board[pos[0]][pos[1]].team != team:
                can = True
                break

        if can is True:

            second = True

    if check is True and first is False and second is False and third is False:

        return "checkmate"

    elif check is True and first is True or second is True or third is True:

        print(first, second, third)
        return "check"

    else:

        return


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

    if check(team[turn]) == "checkmate":

        menu.cls()
        print("The ", team[turn], " is checkmate, you lose")
        menu.pieces.board.show()
        break
    
    elif check(team[turn]) == "check":

        print("The ", team[turn], " is in check")

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

            if check(team[turn]) == "check":

                print("The ", team[turn], " is in check")

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
