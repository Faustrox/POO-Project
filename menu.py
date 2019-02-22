import pieces
def cls(): print("\n" * 35)

print("Welcome to a Chess\n")


def menu():

    while True:
        pieces.board.show()
        print("\n1.- Start the game\n2.- How to play?(IN PROGRESS)\n3.- Exit Game")

        option = int(input())

        if option == 1:
            cls()
            print("The board was created\n")
            pieces.board.fill()
            break

        else:
            cls()
            print("I said you that its in progress")


menu()
