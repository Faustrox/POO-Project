import menu

piece = menu.pieces.piece
turn = 0 # variable que se ira sunando para solo llegar a 1, esta decidira cual team le tocara o sea el turno, 0 para white, 1 para black
team = ["white", "black"] # Esto contendra los nombres de los equipos
minus = ["a", "b", "c", "d", "e", "f", "g", "h"] # Las posiciones en columna pero en minuscula, esta la use para alguno que ponga minusculas debes de mayusculas


def check(team):  # La funcion del Jaque y Jaquemate con un input de equipo

    check = False
    first = False
    second = False # 4 boleanos, el principal es el check, si el check no se convierte a True no podra pasar por las condiciones para volver True a los otros
    third = False  
    
    allay_pieces = menu.pieces.board.allay_pieces(team)
    for piece in allay_pieces:  # Este for ira de pieza en pieza del equipo que incertes en la funcion

        if isinstance(piece, menu.pieces.king) is True:

            allay_king = piece  # Si la pieza es un rey, me almacenara ese objeto en una variable
            break

    for enemy_piece in menu.pieces.board.enemy_pieces(team):  # Este for ira de pieza en pieza del equipo enemigo que incertaste, si incertas white, el enemigo es black
        
        if isinstance(enemy_piece, menu.pieces.king) is True: # Si esa pieza es un rey entonces cedera
            continue
        
        enemy_possible = enemy_piece.possible_move()
        for enemy_way in enemy_possible:  # Busca las trayectorias de la pieza
            
            if allay_king.pos in enemy_possible[enemy_way]:  # la condicion principal, si se cumple las otras pueden ser cumplidas, sino no

                check = True    # Si la posicion del rey aliado esta en los posibles movimientos de alguna pieza enemiga entonces es jaque
 
                for allay_piece in allay_pieces: # Un bucle que va de pieza en pieca enemiga

                    if type(allay_piece) == menu.pieces.king: # Si esa pieza es un rey, cedera
                        continue

                    allay_possible = allay_piece.possible_move()
                    
                    for allay_way in allay_possible: # La trayectoria de esa pieza

                        if enemy_piece.pos in allay_possible[allay_way]: # Si la posicion del enemigo que esta apuntando al rey esta en uno de los posibles moviemientos
                                                                        # de un aliado entonces se cumple el first
                            first = True

                        for array_move in allay_possible[allay_way]:

                            for allay_pos_mov in array_move:

                                # Si el possible movimiento de un aliado esta en la trayectoria de un enemigo y el rey aliado esta en esa misma trayectoria
                                # entonces third se cumple
                                if allay_pos_mov in enemy_possible[enemy_way] and allay_king.pos in enemy_possible[enemy_way]:

                                    third = True
                                    break

    if check is True:

        can = False

        for pos in allay_king.possible_move(): # Cada posible movimiento del rey

            pos = [int(pos[1]), menu.pieces.board.positionY[pos[0]]]

            if isinstance(menu.pieces.board.game_board[pos[0]][pos[1]], menu.pieces.piece) is False: # Si en algun posible movimiento del rey hay una pieza entonces
                # second se cumple
                can = True
                break

            elif isinstance(menu.pieces.board.game_board[pos[0]][pos[1]], piece) is True and menu.pieces.board.game_board[pos[0]][pos[1]].team != team:
                # Si en algun posible movimiento del rey hay una pieza enemiga entonces second se cumple
                can = True
                break

        if can is True:

            second = True

    if check is True and first is False and second is False and third is False: # si solo check es True entonces es jaquemate

        return "checkmate"

    elif check is True and first is True or second is True or third is True: # si check y alguna otra variable boleana es True entonces es Jaque

        return "check"

    else:

        return


def is_it_possible(pos): # Funcion que retorna True o False dependiendo de si la posicion que le pones es posible en la matriz del board

    for colum_string in menu.pieces.board.positionY:

        for row_string in range(1, 9):

            row_string = str(row_string)
            string = colum_string + row_string

            if pos == string:

                return True

    return False


while True: # BASE LOOP (GAME LOOP)

    if turn == 2: # Si la variable turno se pasa de 1 entonces vuelve a 0
        turn = 0

    if check(team[turn]) == "checkmate": # La condicion del jaquemate

        menu.cls()
        print("The ", team[turn], " is checkmate, you lose")
        menu.pieces.board.show()
        break
    
    elif check(team[turn]) == "check": # La condicion del jaque

        print("The ", team[turn], " is in check")

    print("It's the turn for the ", team[turn], " team")
    menu.pieces.board.show()
    print("Select the position of the piece that you want to move: ")
    piece_select = input()

    if piece_select[0] in minus: # Si incertas una letra en minuscula esta se convierte en mayuscula
        piece_select = chr(ord(piece_select[0]) - 32) + piece_select[1]

    if is_it_possible(piece_select) is False:
        menu.cls()
        print("That position doesn't exist or you put the position wrong")
        continue

    position_name = piece_select
    piece_select = menu.pieces.board.game_board[int(
        piece_select[1])][menu.pieces.board.positionY[piece_select[0]]] # Convierte la variable piece_select de un string al objeto que indicaste mediante posiciones

    if isinstance(piece_select, menu.pieces.piece) is False: # Si la posicion que entraste no es una pieza entonces volvera atras para volver a elegir

        menu.cls()
        print("That isn't a piece, please select a valid piece")
        continue

    if piece_select.team != team[turn]:  # Si la posicion que seleccionaste es una pieza del otro enemigo, volveras a elegir otra posicion
        menu.cls()
        print("This piece is of the other team, please select one that you can take")
        continue

    elif isinstance(piece_select, menu.pieces.piece) is True:
        menu.cls()

        while True:  # Bucle de el siguiente movimiento

            if check(team[turn]) == "check":

                print("The ", team[turn], " is in check")

            print("It's the turn for the ", team[turn], " team") 
            menu.pieces.board.show()
            print("You select a ", piece_select.name, " in the positon ", position_name)
            print("Digit the position where you want to move it: (If you put 0 you can return to select another piece)")
            print(piece_select.possible_move())
            move_to = input()
            move_to = str(move_to)

            if move_to[0] in minus: # Lo mismo que arriba, si incertas una letra en minuscula lo convierte a mayuscula
                move_to = chr(ord(move_to[0]) - 32) + move_to[1]

            if is_it_possible(move_to) is False:

                if move_to == "0": # Si alguien incerta 0 en el input move_to entonces podra cambiar de pieza
                    menu.cls()
                    print("You decide to change the piece, player from team ", team[turn])
                    break

                else:
                    menu.cls() # Si esa posicion no existe entonces le avisara y le pondra a elegir de nuevo su movimiento
                    print(
                        "That position doesn't exist, please select a valid position, player from team ", team[turn])
                    continue

            else:

                if isinstance(piece_select.move(move_to), str) is True: # Si la funcion move retorna un str... si es asi entonces significa que no se movera y retornara
                    # un error, si pasa entonces dejara al jugador elegir de nuevo de movimiento
                    menu.cls()
                    print(piece_select.move(move_to))
                    continue

                else: # si no pasa, entonces la pieza se movera y el turno cedera al otro equipo

                    piece_select.move(move_to)
                    turn += 1
                    break

    else: # si no es una pieza entonces dejara que el jugador elija de nuevo

        print("That is not a piece, please select again")
    menu.cls()
