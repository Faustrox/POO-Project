import board_functions # importa todo el codigo del archivo pieces.py
import pieces
def cls(): print("\n" * 35) # para hacer una "limpieza" del terminal

print("Welcome to a Chess\n")


def menu(): # Para crear un menu, muy sencillo

    while True:
        board_functions.board_function.show()
        print("\n1.- Start the game\n2.- Exit Game")

        option = int(input())

        if option == 1:
            cls()
            print("The board was created, white down, black up\n")
            board_functions.board_function.fill()
            break

        else:
            cls()
            print("I said you that its in progress")

menu()
