def gameboard(x, y, b):
    """defining the board game base on the X and Y input and defining bomb number"""
    game = [[0 for i in range(y)] for j in range(x)]
    bobmnum = 0
    while bobmnum < b:
        xe = random.randint(0, len(game) - 1)
        ye = random.randint(0, len(game[1]) - 1)
        if game[xe][ye] != 'X':
            game[xe][ye] = 'X'
            bobmnum = bobmnum + 1
    # print(bobmnum)

    for x in range(len(game)):
        for y in range(len(game[1])):
            if game[x][y] == 'X':
                if x == 0 and y == 0:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y + 1] != 'X': game[x + 1][y + 1] = game[x + 1][y + 1] + 1

                if 0 < x < len(game) - 1 and y == 0:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y + 1] != 'X': game[x + 1][y + 1] = game[x + 1][y + 1] + 1
                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y + 1] != 'X': game[x - 1][y + 1] = game[x - 1][y + 1] + 1

                if x == len(game) - 1 and y == 0:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y + 1] != 'X': game[x - 1][y + 1] = game[x - 1][y + 1] + 1

                if x == len(game) - 1 and 0 < y < len(game[1]) - 1:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1
                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y - 1] != 'X': game[x - 1][y - 1] = game[x - 1][y - 1] + 1
                    if game[x - 1][y + 1] != 'X': game[x - 1][y + 1] = game[x - 1][y + 1] + 1

                if x == len(game) - 1 and y == len(game[1]) - 1:
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1
                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y - 1] != 'X': game[x - 1][y - 1] = game[x - 1][y - 1] + 1

                if 0 < x < len(game) - 1 and y == len(game[1]) - 1:
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1
                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y - 1] != 'X': game[x + 1][y - 1] = game[x + 1][y - 1] + 1
                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y - 1] != 'X': game[x - 1][y - 1] = game[x - 1][y - 1] + 1

                if x == 0 and y == len(game[1]) - 1:
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1
                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y - 1] != 'X': game[x + 1][y - 1] = game[x + 1][y - 1] + 1

                if x == 0 and 0 < y < len(game[1]) - 1:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1
                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y - 1] != 'X': game[x + 1][y - 1] = game[x + 1][y - 1] + 1
                    if game[x + 1][y + 1] != 'X': game[x + 1][y + 1] = game[x + 1][y + 1] + 1

                if 0 < x < len(game) - 1 and 0 < y < len(game[1]) - 1:
                    if game[x][y + 1] != 'X': game[x][y + 1] = game[x][y + 1] + 1
                    if game[x][y - 1] != 'X':  game[x][y - 1] = game[x][y - 1] + 1

                    if game[x + 1][y] != 'X': game[x + 1][y] = game[x + 1][y] + 1
                    if game[x + 1][y - 1] != 'X': game[x + 1][y - 1] = game[x + 1][y - 1] + 1
                    if game[x + 1][y + 1] != 'X': game[x + 1][y + 1] = game[x + 1][y + 1] + 1

                    if game[x - 1][y] != 'X': game[x - 1][y] = game[x - 1][y] + 1
                    if game[x - 1][y - 1] != 'X': game[x - 1][y - 1] = game[x - 1][y - 1] + 1
                    if game[x - 1][y + 1] != 'X': game[x - 1][y + 1] = game[x - 1][y + 1] + 1
    return game


def open(x, y):
    """determining how to open a '#' in the board game that already define based on the input"""
    if x == 0 and y == 0:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y + 1] == a:
            board[x + 1][y + 1] = game[x + 1][y + 1]
            if board[x + 1][y + 1] == 0: open(x + 1, y + 1)

    if 0 < x < len(game) - 1 and y == 0:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y + 1] == a:
            board[x + 1][y + 1] = game[x + 1][y + 1]
            if board[x + 1][y + 1] == 0: open(x + 1, y + 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y + 1] == a:
            board[x - 1][y + 1] = game[x - 1][y + 1]
            if board[x - 1][y + 1] == 0: open(x - 1, y + 1)

    if x == len(game) - 1 and y == 0:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y + 1] == a:
            board[x - 1][y + 1] = game[x - 1][y + 1]
            if board[x - 1][y + 1] == 0: open(x - 1, y + 1)

    if x == len(game) - 1 and 0 < y < len(game[1]) - 1:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y - 1] == a:
            board[x - 1][y - 1] = game[x - 1][y - 1]
            if board[x - 1][y - 1] == 0: open(x - 1, y - 1)

        if board[x - 1][y + 1] == a:
            board[x - 1][y + 1] = game[x - 1][y + 1]
            if board[x - 1][y + 1] == 0: open(x - 1, y + 1)

    if x == len(game) - 1 and y == len(game[1]) - 1:
        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y - 1] == a:
            board[x - 1][y - 1] = game[x - 1][y - 1]
            if board[x - 1][y - 1] == 0: open(x - 1, y - 1)

    if 0 < x < len(game) - 1 and y == len(game[1]) - 1:
        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y - 1] == a:
            board[x + 1][y - 1] = game[x + 1][y - 1]
            if board[x + 1][y - 1] == 0: open(x + 1, y - 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y - 1] == a:
            board[x - 1][y - 1] = game[x - 1][y - 1]
            if board[x - 1][y - 1] == 0: open(x - 1, y - 1)

    if x == 0 and y == len(game[1]) - 1:
        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y - 1] == a:
            board[x + 1][y - 1] = game[x + 1][y - 1]
            if board[x + 1][y - 1] == 0: open(x + 1, y - 1)

    if x == 0 and 0 < y < len(game[1]) - 1:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y - 1] == a:
            board[x + 1][y - 1] = game[x + 1][y - 1]
            if board[x + 1][y - 1] == 0: open(x + 1, y - 1)

        if board[x + 1][y + 1] == a:
            board[x + 1][y + 1] = game[x + 1][y + 1]
            if board[x + 1][y + 1] == 0: open(x + 1, y + 1)

    if 0 < x < len(game) - 1 and 0 < y < len(game[1]) - 1:
        if board[x][y + 1] == a:
            board[x][y + 1] = game[x][y + 1]
            if board[x][y + 1] == 0: open(x, y + 1)

        if board[x][y - 1] == a:
            board[x][y - 1] = game[x][y - 1]
            if board[x][y - 1] == 0: open(x, y - 1)

        if board[x + 1][y] == a:
            board[x + 1][y] = game[x + 1][y]
            if board[x + 1][y] == 0: open(x + 1, y)

        if board[x + 1][y - 1] == a:
            board[x + 1][y - 1] = game[x + 1][y - 1]
            if board[x + 1][y - 1] == 0: open(x + 1, y - 1)

        if board[x + 1][y + 1] == a:
            board[x + 1][y + 1] = game[x + 1][y + 1]
            if board[x + 1][y + 1] == 0: open(x + 1, y + 1)

        if board[x - 1][y] == a:
            board[x - 1][y] = game[x - 1][y]
            if board[x - 1][y] == 0: open(x - 1, y)

        if board[x - 1][y - 1] == a:
            board[x - 1][y - 1] = game[x - 1][y - 1]
            if board[x - 1][y - 1] == 0: open(x - 1, y - 1)

        if board[x - 1][y + 1] == a:
            board[x - 1][y + 1] = game[x - 1][y + 1]
            if board[x - 1][y + 1] == 0: open(x - 1, y + 1)


###############################################
import random

gameDone = False
winposs = False
flagged = 0

print("Let's play minesweeper!")
xx = int(input("Insert number of columns: "))
print("Nice!")
yy = int(input("And number of rows: "))
print("Cool!")
numbomb = int(input("Lastly how many bombs? "))

a = '#'
game = gameboard(xx, yy, numbomb)
board = [[a for i in range(len(game[1]))] for j in range(len(game))]

print("Tip: You have to flag all the bombs to win!")
print("let's Begin: ")
print('')

for i in range(len(game)):
    print(*board[i])
print('')
while gameDone == False:
    print('########################################################')
    checkin = input(
        "Choose column (Y) to open between " + str(1) + ' and ' + str(len(game)) + ' (or press F to flag BOMB!) : ')

    if checkin == 'f' or checkin == 'F':
        x = int(input("Choose column (Y) to flag between " + str(1) + ' and ' + str(len(game)) + ' : ')) - 1
        y = int(input("Choose column (X) to flag between " + str(1) + ' and ' + str(len(game[1])) + ' : ')) - 1
        board[x][y] = 'B'
        if game[x][y] == 'X':
            flagged = flagged + 1



    else:
        x = int((checkin)) - 1
        y = int(input("Choose column (X) to open between " + str(1) + ' and ' + str(len(game[1])) + ' : ')) - 1

        board[x][y] = game[x][y]

        if game[x][y] == 0:
            open(x, y)

        if game[x][y] == 'X':
            gameDone = True
            print("############################### WHOOPS!!")
            print('')
            for i in range(len(game)):
                print(*game[i])
            print("")
            for i in range(len(game)):
                print(*board[i])
            print('')
            print("BOOM! You opened a bomb!...YOU LOST :( ")

    winposs = True
    for xo in range(0, len(game)):
        for yo in range(0, len(game[1])):
            if game[xo][yo] == 'X' and board[xo][yo] != 'B':
                # print(game[xo][yo] + ' , ' +board[xo][yo])
                winposs = False
                break
            if game[xo][yo] != 'X' and board[xo][yo] == 'B':
                winposs = False
                break
        if winposs == False:
            break
    if winposs == True:
        gameDone = True
        print("############################### CONGRATS! ")
        print('')
        for i in range(len(game)):
            print(*game[i])
        print("")
        for i in range(len(game)):
            print(*board[i])
        print('')
        print("GGs YOU WON!!! :) ")

    if gameDone == False:
        print("")
        for i in range(len(game)):
            print(*board[i])
        print('')

print("Thanks for playing ;) ")