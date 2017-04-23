#game of 9
import random
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
x = []
winning_board = [[1,2,3],
                 [4,5,6],
                 [7,8," "]]
print("""Arrange the board in ( 1 2 3
                       4 5 6
                       7 8 _ ) layout to win.
        Use wasd to move the pieces into the emtpy square.
        Good luck!""")
for i in range(len(board)):
    for j in range(len(board[i])):
        random_board = random.randint(1,9)
        while random_board in x:
            random_board = random.randint(1,9)
        board[i][j] = random_board
        x.append(random_board)

def over_engineered():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 9:
                board[i][j] = " "
                indexI = i
                indexJ = j
                return indexI, indexJ
over_engineered()
def print_board():
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j]," ",end='')
        print()
print_board()
def check_under():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                return i, j
def play(indexI, indexJ):
    character = board[indexI][indexJ]
    direction = input("wasd: ")
    if direction == "a":
        if not check_illegal(indexI, indexJ+1):
            tmp = board[indexI][indexJ + 1]
            board[indexI][indexJ + 1] = " "
            board[indexI][indexJ] = tmp
    if direction == "d":
        if not check_illegal(indexI, indexJ-1):   
            tmp = board[indexI][indexJ - 1]
            board[indexI][indexJ - 1] = " "
            board[indexI][indexJ] = tmp
    if direction == "s":
        if not check_illegal(indexI-1, indexJ): 
            tmp = board[indexI-1][indexJ]
            board[indexI-1][indexJ] = " "
            board[indexI][indexJ] = tmp
    if direction == "w":
        if not check_illegal(indexI+1, indexJ): 
            tmp = board[indexI+1][indexJ]
            board[indexI+1][indexJ] = " "
            board[indexI][indexJ] = tmp
    print_board()
def won():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != winning_board[i][j]:
                return False
    return True
def check_illegal(indexI, indexJ):
    return indexI < 0 or indexI > 2 or indexJ < 0 or indexJ > 2
while not won():
    i,j = check_under()
    play(i, j)
    
print("\n\n\nCongratulations You have won the game!!!")
