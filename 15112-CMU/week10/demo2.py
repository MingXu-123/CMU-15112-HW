from tkinter import *

def isValid(board, queenRow, queenCol):
    # A board is legal if no two queens can attack each other
    # We only need to check the most recently placed queen
    for row in range(len(board)):
        for col in range(len(board[0])):
            if queenRow == row and queenCol == col:
                continue
            elif board[row][col] == "Q":
                if ((queenRow == row) or
                    (queenCol == col) or
                    (queenRow + queenCol == row + col) or
                    (queenRow - queenCol == row - col)):
                    return False
    return True

def solve(board, queen):
    if queen == len(board):
        return board
    else:
        row = queen
        for col in range(len(board[row])):
            if isValid(board, row, col):
                board[row][col] = "Q"
                tmp = solve(board, queen+1)
                if tmp is not None:
                    return board
                board[row][col] = " "
        return None


def nQueens(n):
    board = [[" "] * n for row in range(n)]
    return solve(board, 0)

# this is the decorator for makeExample2DList
def print2DListResult(makeExample2DList):
    def printLst(n):
        lst = makeExample2DList(n)
        rows = len(lst)
        cols = len(lst[0])
        res = ''
        for row in range(rows):
            res += ("[" + " "*n)
            for col in range(cols):
                numOfspace = n
                lenOfnum = len(str(lst[row][col]))
                if lenOfnum > 1:
                    numOfspace -= (lenOfnum - 1)
                res += str(lst[row][col])
                res += " " * numOfspace
            res += "]\n"
        return res
    return printLst


# this is the main function for make example 2D list
@print2DListResult
def makeExample2DList(n):
    myList= nQueens(6)
    return myList

print(makeExample2DList(5))

def drawVicsek(canvas, x, y, size, level):
    if level == 0:
        canvas.create_rectangle(x, y, x + size, y+size,fill= 'black')
    else:
        newSize =size/3
        for row in range(3):
            for col in range(3):
                if (row + col)%2==0:
                    drawVicsek(canvas,
                               x+col*newSize,y+col*newSize,newSize,level-1)


def init(data):
    data.level = 1

def drawVicsek(canvas, x, y, size, level):
    if level == 0:
        canvas.create_rectangle(x, y, x + size, y+size,fill= 'black')
    else:
        newSize =size/3
        for row in range(3):
            for col in range(3):
                if (row + col)%2==0:
                    drawVicsek(canvas,
                               x+col*newSize,y+col*newSize,newSize,level-1)

def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif (event.keysym in ["Down", "Left"]) and (data.level > 0):
        data.level -= 1

def redrawAll(canvas, data):
    margin = min(data.width, data.height)//10
    otherParams = None
    drawVicsek(canvas, data.level, otherParams)
    canvas.create_text(data.width/2, 0,
                       text = "Level %d Fractal" % (data.level),
                       font = "Arial " + str(int(margin/3)) + " bold",
                       anchor="n")
    canvas.create_text(data.width/2, margin,
                       text = "Use arrows to change level",
                       font = "Arial " + str(int(margin/4)),
                       anchor="s")

def mousePressed(event, data): pass

def timerFired(data): pass
