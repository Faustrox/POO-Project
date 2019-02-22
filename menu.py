#   a b c d e f g h
# 1 R K B Q K B K R
# 2 p p p p p p p p
# 3 O * O * O * O *
# 4 * O * O * O * O
# 5 O * O * O * O *
# 6 * O * O * O * O
# 7 p p p p p p p p
# 8 R K B Q K B K R

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
