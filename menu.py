import pieces # importa todo el codigo del archivo pieces.py
def cls(): print("\n" * 35) # para hacer una "limpieza" del terminal

print("Welcome to a Chess\n")


def menu(): # Para crear un menu, muy sencillo

    while True:
        pieces.board.show()
        print("\n1.- Start the game\n2.- How to play?(IN PROGRESS)\n3.- Exit Game")

        option = int(input())

        if option == 1:
            cls()
            print("The board was created, white down, black up\n")
            pieces.board.fill()
            break

        else:
            cls()
            print("I said you that its in progress")

menu()