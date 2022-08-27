from lib2to3.pgen2.pgen import PgenGrammar
from random import randint, random, randrange
import sys, pygame
from turtle import update

pygame.init()

size = width, height = 300, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

gameDeclared = 2
gameDraw = False
board = [None, None, None, None, None, None, None, None, None]
guiLocation = [
    (20, 20),
    (120, 20),
    (220, 20),
    (20, 120),
    (120, 120),
    (220, 120),
    (20, 220),
    (120, 220),
    (220, 220),
]
image = pygame.image.load(r"./board.png")
image = pygame.transform.scale(image, (300, 300))
x = pygame.image.load(r"./x.png")
x = pygame.transform.scale(x, (50, 50))
heading = pygame.font.SysFont("freesansbold", 32)
o = pygame.image.load(r"./o.png")
o = pygame.transform.scale(o, (50, 50))
xTurn = True

screen.fill((255, 255, 255))


screen.blit(image, (0, 0))


def findTheBox(pos):
    x = pos[0]
    y = pos[1]

    if y < 100:
        if x < 100:
            return 0
        if x > 100 and x < 200:
            return 1
        if x > 200:
            return 2
    if y > 100 and y < 200:
        if x < 100:
            return 3
        if x > 100 and x < 200:
            return 4
        if x > 200:
            return 5
    if y > 200:
        if x < 100:
            return 6
        if x > 100 and x < 200:
            return 7
        if x > 200:
            return 8
    else:
        return 5


def updateBoard():
    for box in range(len(board)):
        if board[box] == 1:
            screen.blit(x, guiLocation[box])
        elif board[box] == 0:
            screen.blit(o, guiLocation[box])


def move(box, value):
    if gameDeclared == 2:
        if board[box] == None:
            board[box] = value

        else:
            print("Occupied Mate")

    elif gameDeclared == 1:
        print("Game is over")

        # if value == 1:
        #     xTurn = True
        # elif value == 0 :
        #     xTurn = False


def endTheGame(winner):
    global gameDeclared
    if gameDeclared == 2:
        gameDeclared = 1
        if winner == 0:
            text = heading.render("O won the game", True, (0, 0, 0))
            screen.blit(text, (30, 310))
        elif winner == 1:
            text = heading.render("X won the game", True, (0, 0, 0))
            screen.blit(text, (30, 310))

        else:
            text = heading.render("Game is a draw", True, (0, 0, 0))
            screen.blit(text, (30, 310))


# def checkThreats():
#     row1 = [board[0], board[1], board[2]]
#     row2 = [board[3], board[4], board[5]]
#     row3 = [board[6], board[7], board[8]]
#     fullboard = [row1, row2, row3]
#     for row in range(len(fullboard)):
#         x = fullboard[row]

#         if x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
#             for box in range(0, 3):
#                 if x[box] == None:

#                     return box


def botPlay():
    unOccupied = []
    for box in range(len(board)):
        if board[box] == None:
            unOccupied.append(box)
    chosenBox = unOccupied[randrange(0, len(unOccupied))]
    # print(checkThreats())
    move(chosenBox, 0)


def checkforwin():
    global gameDeclared
    row1 = [board[0], board[1], board[2]]
    row2 = [board[3], board[4], board[5]]
    row3 = [board[6], board[7], board[8]]
    fullboard = [row1, row2, row3]

    # check horizontal
    for row in range(len(fullboard)):
        x = fullboard[row]
        if x[0] != None and [1] != None and x[2] != None:
            if x[0] == x[1] and x[1] == x[2]:
                endTheGame(x[0])

    # check for vertical
    for i in range(0, 3):
        if row1[i] != None and row2[i] != None and row3[i] != None:
            if row1[i] == row2[i] and row2[i] == row3[i]:
                endTheGame(row1[i])

    # chedk for diagonal
    if row2[1] != None:
        if row1[0] == row2[1] and row2[1] == row3[2]:
            endTheGame(row1[0])
        elif row1[2] == row2[1] and row2[1] == row3[0]:
            endTheGame(row1[2])
    # check for draw
    if gameDeclared == 2:
        boxFull = True
        for box in range(len(board)):
            if board[box] == None:
                boxFull = False

        if boxFull == True:
            endTheGame(3)


while True:

    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.

        if (
            event.type == pygame.MOUSEBUTTONDOWN
        ):  # If the current event is the mouse button down event
            pos = pygame.mouse.get_pos()  # Stores the mouse position
            if xTurn == True:
                if board[findTheBox(pos)] == None:
                    move(findTheBox(pos), 1)
                    updateBoard()
                    xTurn = False
                    checkforwin()
                else:
                    print("occupied")

            elif xTurn == False:
                # if board[findTheBox(pos)] == None:

                #     move(findTheBox(pos), 0)
                #     updateBoard()

                #     xTurn = True
                #     checkforwin()
                # else:
                #     print("occupied")
                botPlay()
                updateBoard()
                checkforwin()
                xTurn = True

        if event.type == pygame.QUIT:

            pygame.quit()

            # quit the program.
            quit()

        pygame.display.update()
