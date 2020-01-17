#################################################################
# Hw10
# Your Name: Ming Xu
# Your Andrew ID:mxu2
# Your Section:2N
#################################################################
import os
from functools import reduce

# this is the collaborators function
def findLargestFileCollaborators():
    return "yufeiche"

# this is the helper function for findLargestFile
def findLargestFileHelper(path, res, largestFilePath):
    if os.path.isfile(path):
        return path
    else:
        for filename in os.listdir(path):
            if filename == '.DS_Store':
                continue
            tmpPath = findLargestFileHelper(path + "/" + filename,
                                            res, largestFilePath)
            if not os.path.isfile(tmpPath):
                continue
            tmpValue = os.path.getsize(tmpPath)
            if tmpValue >= largestFilePath:
                largestFilePath = tmpValue
                res = tmpPath
        return res


# this is the main function for findLargestFile
def findLargestFile(path):
    largestFilePath = 0
    res = ""
    return findLargestFileHelper(path, res, largestFilePath)


# find the position of each num in board
def findPositionOfNum(num, board):
    rows = len(board)
    cols = rows
    rowOfNum = 0
    colOfNum = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == num:
                rowOfNum = row
                colOfNum = col
    return rowOfNum, colOfNum


# check whether one of the num in board has next step
def hasNextStep(num, nextNum, board):
    numRow, numCol = findPositionOfNum(num, board)
    nextNumRow, nextNumCol = findPositionOfNum(nextNum, board)
    if (nextNumRow - numRow) * (nextNumCol - numCol) == 2 or\
            (nextNumRow - numRow) * (nextNumCol - numCol) == -2:
        return True
    else:
        return False


# return True if board is a Knights Tour and return False otherwise
def isKnightsTour(board):
    if board == [[0]]:
        return False
    rows = len(board)
    cols = rows
    compareList = [i for i in range(1, cols ** 2 + 1)]
    tourList = []
    for row in range(rows):
        for col in range(cols):
            tourList.append(board[row][col])
    tourList.sort()
    # check whether tourList meet the requirement of Knights tour
    if compareList != tourList:
        return False
    finalNum = rows * cols
    knightsTour = True
    for num in range(1, finalNum):
        nextNum = num + 1
        if hasNextStep(num, nextNum, board):
            knightsTour = True
            continue
        else:
            knightsTour = False
            break
    return knightsTour


# this is the create knight's board function
def createKnightBoard(n):
    rows, cols = n, n
    board = []
    for i in range(n):
        board += [[0]*cols]
    return board


# this is the recursive function for createKnightsTour
def traverse(board, x, y, count):
    rows, cols = len(board), len(board)
    board[x][y] = count
    if count >= rows * cols:
        return board
    directionY = [2, 2, 1, -1, -2, -2, -1, 1]
    directionX = [-1, 1, 2, 2, 1, -1, -2, -2]
    numOfdirection = 8
    for i in range(numOfdirection):
        nextX = x + directionX[i]
        nextY = y + directionY[i]
        if (nextX < 0 or nextX >= cols or nextY < 0 or nextY >= rows)\
                or board[nextX][nextY] != 0:
            continue
        tmpboard = traverse(board, nextX, nextY, count + 1)
        if tmpboard != None:
            return tmpboard
        # if tmpboard is None, then undo the move
        board[nextX][nextY] = 0


# This is the main function for createKnightsTour
def createKnightsTour(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return None
    board = createKnightBoard(n)
    startRow = 0
    startCol = 0
    count = 1
    traverse(board, startRow, startCol, count)
    if isKnightsTour(board):
        return board
    else:
        return None


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
    myList=[]
    for row in range(n):
        myList.append([col*row for col in range(n)])
    return myList


# this is the lambda function for myjoin
myJoin = lambda L, sep: str(L[0])\
    if len(L) == 1 else reduce(lambda x, y: (x + y),
                               list(map(lambda x: str(x) + sep,
                                        L[:-1]))) + str(L[-1])


#ignore_rest line
###################################################
from tkinter import *
# the maximum level for this animation code is 5,
# because I only give it five different colors for different levels
# given more colors it can run on more higher levels

# this is the init function to save data in animation
def init(data):
    data.level = 1
    data.depth = -1
    data.color = ['yellow', 'red', 'orange', '#00FF00', 'blue']
    data.lineColor = ['#F5FFFA', 'yellow', 'orange', '#E0FFFF', 'pink']
    data.smallCircleColor = ['#F5FFFA', 'red', 'orange', '#87CEFA', 'pink']


# this is the helper function for drawLinesAndCircles
def drawCircle(canvas, data, xc, yc, r, depth):
    canvas.create_oval(xc - r / 4, (yc - 2 * r) - r / 4,
                       xc + r / 4, (yc - 2 * r) + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - r / 4, (yc + 2 * r) - r / 4,
                       xc + r / 4, (yc + 2 * r) + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval((xc - 2 * r) - r / 4, yc - r / 4,
                       (xc - 2 * r) + r / 4, yc + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval((xc + 2 * r) - r / 4, yc - r / 4,
                       (xc + 2 * r) + r / 4, yc + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc + 2 ** 0.5 * r - r / 4, yc - 2 ** 0.5 * r - r / 4,
                       xc + 2 ** 0.5 * r + r / 4, yc - 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - 2 ** 0.5 * r - r / 4, yc - 2 ** 0.5 * r - r / 4,
                       xc - 2 ** 0.5 * r + r / 4, yc - 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc - 2 ** 0.5 * r - r / 4, yc + 2 ** 0.5 * r - r / 4,
                       xc - 2 ** 0.5 * r + r / 4, yc + 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])
    canvas.create_oval(xc + 2 ** 0.5 * r - r / 4, yc + 2 ** 0.5 * r - r / 4,
                       xc + 2 ** 0.5 * r + r / 4, yc + 2 ** 0.5 * r + r / 4,
                       fill=data.smallCircleColor[depth])


# this is the drawLinesAndCircles main function
def drawLinesAndCircles(canvas, data, xc, yc, r, depth):
    canvas.create_line(xc, yc, xc, yc - 2 * r, fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc, yc + 2 * r, fill=data.lineColor[depth])
    canvas.create_line(xc + 2 * r, yc, xc, yc, fill=data.lineColor[depth])
    canvas.create_line(xc - 2 * r, yc, xc, yc, fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc + 2 ** 0.5 * r, yc - 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc - 2 ** 0.5 * r, yc - 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc - 2 ** 0.5 * r, yc + 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    canvas.create_line(xc, yc, xc + 2 ** 0.5 * r, yc + 2 ** 0.5 * r,
                       fill=data.lineColor[depth])
    drawCircle(canvas, data, xc, yc, r, depth)


# this is the level0 draw text function
def drawText(data, canvas, margin):
    canvas.create_text(data.width / 2, 0,
                       text="Level %d Fractal" % (data.level),
                       font="Arial " + str(int(margin / 3)) + " bold",
                       anchor="n", fill='white')
    canvas.create_text(data.width / 2, margin,
                       text="Use arrows to change level",
                       font="Arial " + str(int(margin / 4)),
                       anchor="s", fill='white')


# this is the helper function for drawFractalSun main function
def drawForLevelO(data, canvas):
    # this following code is only for state level == 0
    margin = min(data.width, data.height) // 10
    xc = data.width // 2
    yc = data.height // 2
    r = 0.6 * data.width // 5
    canvas.create_oval(xc - r, yc - r, xc + r, yc + r, fill='#FFDAB9')
    drawText(data, canvas, margin)


# this is the main function for drawFractalSun
def drawFractalSun(data, canvas, xc, yc, r, level, depth):
    if level == 0:
        # this following code is only for state level == 0
        drawForLevelO(data, canvas)
    elif level == 1:
        drawLinesAndCircles(canvas, data, xc, yc, r, depth)
        canvas.create_oval(xc - r, yc - r, xc + r, yc + r, fill=data.color[depth])
    else:
        # the following code the recursive case for this problem
        drawFractalSun(data, canvas, xc, yc, r, level - 1, depth + 1)
        drawFractalSun(data, canvas, xc, yc - 2 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc, yc + 2 * r, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 * r, yc, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 * r, yc, r / 4, level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 ** 0.5 * r, yc - 2 ** 0.5 * r, r / 4,
                       level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 ** 0.5 * r, yc - 2 ** 0.5 * r, r / 4,
                       level - 1, depth - 1)
        drawFractalSun(data, canvas, xc - 2 ** 0.5 * r, yc + 2 ** 0.5 * r, r / 4,
                       level - 1, depth - 1)
        drawFractalSun(data, canvas, xc + 2 ** 0.5 * r, yc + 2 ** 0.5 * r, r / 4,
                       level - 1, depth - 1)


# this is the keyboard event handler
def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif (event.keysym in ["Down", "Left"]) and (data.level > 0):
        data.level -= 1


# this function only draw background of canvas
def drawCanvas(canvas, data):
    topX = 0
    topY = 0
    canvas.create_rectangle(topX, topY,
                            data.width, data.height, fill='black')


# this is the redrawAll function
def redrawAll(canvas, data):
    drawCanvas(canvas, data)
    margin = min(data.width, data.height)//10
    xc, yc = data.width // 2, data.height // 2
    r = 0.6*data.width // 5
    drawFractalSun(data, canvas, xc, yc, r, data.level, data.depth)
    canvas.create_text(data.width / 2, 0,
                       text="Level %d Fractal" % (data.level),
                       font="Arial " + str(int(margin / 3)) + " bold",
                       anchor="n", fill = 'white')
    canvas.create_text(data.width / 2, margin,
                       text="Use arrows to change level",
                       font="Arial " + str(int(margin / 4)),
                       anchor="s", fill = 'white')


# this is the mouse event handler
def mousePressed(event, data): pass


# this is the timer function
def timerFired(data): pass

####################################
# use the run function as-is frame
####################################
def run(width=500, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)
#################################################
# Hw10 Test Functions
#################################################
def testFindLargestFile():
    print("Testing findLargestFile...", end="")
    assert (findLargestFile("sampleFiles/folderA") ==
            "sampleFiles/folderA/folderC/giftwrap.txt")
    assert (findLargestFile("sampleFiles/folderB") ==
            "sampleFiles/folderB/folderH/driving.txt")
    assert (findLargestFile("sampleFiles/folderB/folderF") == "")
    print('passed!')

def testMyJoin():
    print("Testing myJoin...", end="")
    assert(myJoin(['a','b','c'], '-') == 'a-b-c')
    assert(myJoin([1, 2, 3], '@@') == '1@@2@@3')
    assert(myJoin([1, 2, 'c', 'd'], ''))
    assert(myJoin([42], '') == '42')
    print("Passed!")

def testCreateKnightsTour():
    print("Testing createKnightsTour...", end="")
    #The only n=1 board:
    board0 = [[1]]

    #A few different n=5 boards:
    board1 = [
    [ 1,  20, 9,  14, 3  ],
    [ 10, 15, 2,  19, 24 ],
    [ 21, 8,  25, 4,  13 ],
    [ 16, 11, 6,  23, 18 ],
    [ 7,  22, 17, 12, 5  ],
    ]

    board2 = [
    [ 1,  18, 23, 12, 7  ],
    [ 24, 13, 8,  17, 22 ],
    [ 19, 2,  25, 6,  11 ],
    [ 14, 9,  4,  21, 16 ],
    [ 3,  20, 15, 10, 5  ],
    ]

    board3 = createKnightsTour(5)
    board6 = createKnightsTour(1)

    #Our isKnightsTour function from HW5 should return True for each
    assert(isKnightsTour(board0)==True)
    assert(isKnightsTour(board1)==True)
    assert(isKnightsTour(board2)==True)
    assert(isKnightsTour(board3) ==True)
    assert(createKnightsTour(3) == None)
    assert(createKnightsTour(4) == None)
    assert(isKnightsTour(board6) == True)
    assert(createKnightsTour(2) == None)
    assert(createKnightsTour(1) == [[1]])
    print("Passed!")

def testAll():
    testFindLargestFile()
    testMyJoin()
    testCreateKnightsTour()
    lst = makeExample2DList(8)
    print(lst)


def main():
    testAll()

if __name__ == '__main__':
    main()
