#################################################
# Hw5
# Your andrewID:mxu2
# Your section: 2N
#################################################


#################################################
# Hw5 tetris Problem
#################################################
from tkinter import *
import random

####################################
# customize these functions
####################################

# this is the function generating falling piece
def generateFallingPieces():
    # Seven "standard" pieces (tetrominoes)
    iPiece = [[True, True, True, True]]
    jPiece = [[True, False, False], [True, True, True]]
    lPiece = [[False, False, True], [True, True, True]]
    oPiece = [[True, True], [True, True]]
    sPiece = [[False, True, True], [True, True, False]]
    tPiece = [[False, True, False], [True, True, True]]
    zPiece = [[True, True, False], [False, True, True]]
    tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    tetrisPieceColors = ["red", "yellow", "magenta",
                         "pink", "cyan", "green", "orange"]
    return tetrisPieces, tetrisPieceColors


# this is the model of the animation
def init(data):
    data.rows = gameDimensions()[0]
    data.cols = gameDimensions()[1]
    data.cellSize = gameDimensions()[2]
    data.margin = gameDimensions()[3]
    data.emptyColor = 'blue'
    data.board = [[data.emptyColor] * data.cols for i in range(data.rows)]
    data.tetrisPieces, data.tetrisPieceColors = generateFallingPieces()
    data.FallingPiece = []
    data.FallingColor = ''
    data.fallingPieceRow = 0
    data.fallingPieceCol = 0
    data.score = 0
    data.isGameOver = False
    newFallingPiece(data)


# This is the move falling piece function
def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    if not fallingPieceIsLegal(data):
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        return False
    else:
        return True


# this is the remove full row function
def removeFullRows(data):
    fullRows = 0
    newBoard = []
    for row in range(len(data.board)):
        isFilled = True
        for col in range(len(data.board[0])):
            if data.board[row][col] == data.emptyColor:
                isFilled = False
        if isFilled:
            fullRows += 1
            continue
        else:
            newBoard += [data.board[row]]
    linesNeedToAdd = len(data.board) - len(newBoard)
    for i in range(linesNeedToAdd):
        topPosition = 0
        newBoard.insert(topPosition, [data.emptyColor] * data.cols)
    data.board = newBoard
    data.score += fullRows**2


# this is the remove full row function
def removeFullRows(data):
    fullRows = 0
    newRow = data.rows - 1
    # loop through board backwards
    for oldRow in range(data.rows - 1, -1, -1):
        isFilledRow = True
    # check whether it is an empty color position
        for i in range(len(data.board[oldRow])):
            # add unfilled row to board at newRow position
            if data.board[oldRow][i] == data.emptyColor:
                for j in range(len(data.board[oldRow])):
                    data.board[newRow][j] = data.board[oldRow][j]
                newRow -= 1
                isFilledRow = not isFilledRow
                break
        # there is no empty colors, it is a filled row
        if isFilledRow:
            fullRows += 1
    # fill rest of board with data.emptyColor
    for row in range(newRow, -1, -1):
        for col in range(len(data.board[0])):
            data.board[row][col] = data.emptyColor
    data.score += fullRows ** 2

# this is the key press handler
def keyPressed(event, data):
    if event.char == 'r':
        init(data)
    if event.keysym == 'space':
        newFallingPiece(data)
    if event.keysym == "Up":
        rotateFallingPiece(data)
    elif event.keysym == "Down":
        moveFallingPiece(data, 1, 0)
        if not fallingPieceIsLegal(data):
            moveFallingPiece(data, -1, 0)
    elif event.keysym == "Left":
        moveFallingPiece(data, 0, -1)
        if not fallingPieceIsLegal(data):
            moveFallingPiece(data, 0, 1)
    elif event.keysym == "Right":
        moveFallingPiece(data, 0, 1)
        if not fallingPieceIsLegal(data):
            moveFallingPiece(data, 0, -1)


# this is the mouse press event handler
def mousePressed(event, data):
    pass


# this is the draw Game over function
def draw(canvas, data):
    if data.isGameOver:
        text = 'Game Over!'
        x0 = data.margin
        y0 = data.margin + data.cellSize
        x1 = x0 + data.cellSize * data.cols
        y1 = y0 + data.cellSize * 2
        canvas.create_rectangle(x0, y0, x1, y1, fill = "black")
        xt = x0 + (x1 - x0) / 2
        yt = y0 + (y1 - x0) / 3
        canvas.create_text(xt, yt, text = text,
                           fill = "yellow", font = ("Helvetica", 20))


# this is the timer of the animation
def timerFired(data):
    if not moveFallingPiece(data, +1, 0):
        placeFallingPiece(data)
        if not data.isGameOver:
            newFallingPiece(data)
        if not fallingPieceIsLegal(data):
            data.isGameOver = True


# this is the function place the falling piece on the bottom of board
def placeFallingPiece(data):
    rowOfPiece = len(data.FallingPiece)
    lenOfPiece = len(data.FallingPiece[0])
    for row in range(rowOfPiece):
        for col in range(lenOfPiece):
            if data.FallingPiece[row][col]:
                color = data.FallingColor
                data.board[row + data.fallingPieceRow]\
                    [col + data.fallingPieceCol] = color
    removeFullRows(data)


# this is the new falling piece function
def newFallingPiece(data):
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.FallingPiece = data.tetrisPieces[randomIndex]
    data.FallingColor = data.tetrisPieceColors[randomIndex]
    # this is the initial position of falling piece
    data.fallingPieceCol = data.cols // 2 - len(data.FallingPiece[0]) // 2
    data.fallingPieceRow = 0


# this function draws the falling piece
def drawFallingPiece(canvas, data):
    rowOfPiece = len(data.FallingPiece)
    lenOfPiece = len(data.FallingPiece[0])
    for row in range(rowOfPiece):
        for col in range(lenOfPiece):
            if data.FallingPiece[row][col]:
                color = data.FallingColor
                drawCell(canvas, data, row + data.fallingPieceRow,
                         col + data.fallingPieceCol, color)


# this function will test whether or not falling piece is legal
def fallingPieceIsLegal(data):
    # loop through row of falling piece
    for i in range(len(data.FallingPiece)):
        # loop through col of falling piece
        for j in range(len(data.FallingPiece[0])):
            if data.FallingPiece[i][j]:
                if data.fallingPieceCol < 0 or\
                        data.fallingPieceCol + len(data.FallingPiece[0])\
                        > data.cols:
                    return False
                elif data.fallingPieceRow < 0 or\
                        data.fallingPieceRow + len(data.FallingPiece)\
                        > data.rows:
                    return False
                elif data.board[data.fallingPieceRow + i]\
                        [data.fallingPieceCol + j] != data.emptyColor:
                    return False
    return True


# this function return the row, cols of the data.
def getRowNumRowsAndCenter(data):
    row = data.fallingPieceRow
    numRows = len(data.FallingPiece)
    centerRow = row + numRows / 2
    return row, numRows, centerRow


# this function return the col, cols of the data.
def getColNumColsAndCenter(data):
    col = data.fallingPieceCol
    numCols = len(data.FallingPiece[0])
    return col, numCols


# this is the rotate function
def rotateFallingPiece(data):
    oldPiece = data.FallingPiece
    lenOldRow = len(data.FallingPiece)
    lenOldCol = len(data.FallingPiece[0])
    oldColPosition = data.fallingPieceCol
    oldRowPosition = data.fallingPieceRow
    oldRow, oldNumRows, oldCenterRow = getRowNumRowsAndCenter(data)
    oldCol,oldNumCols = getColNumColsAndCenter(data)
    lenNewRow = lenOldCol
    lenNewCol = lenOldRow
    newPiece = []
    for i in range(lenNewRow):
        newPiece += [[None]*lenNewCol]
    for x in range(lenOldRow):
        for y in range(lenOldCol):
            if oldPiece[x][y]:
                newPiece[lenOldCol - 1 - y][x] = oldPiece[x][y]
    data.FallingPiece = newPiece
    newRow, newNumRows, newCenterRow = getRowNumRowsAndCenter(data)
    newCol, newNumCols = getColNumColsAndCenter(data)
    newCol = oldCol + oldNumCols / 2 - newNumCols / 2
    newRow = oldRow + oldNumRows / 2 - newNumRows / 2
    data.fallingPieceCol = round(newCol)
    data.fallingPieceRow = round(newRow)
    if not fallingPieceIsLegal(data):
        data.FallingPiece = oldPiece
        data.fallingPieceCol = oldColPosition
        data.fallingPieceRow = oldRowPosition


# this is function is used to draw score
def drawScore(canvas,data):
    canvas.create_text(data.width / 2, data.height / 25,
                       text = "Score: " + str(data.score))


# This is the function that draws the cell
def drawCell(canvas, data, row, col, color):
    x0 = col * data.cellSize + data.margin
    y0 = row * data.cellSize + data.margin
    x1 = x0 + data.cellSize
    y1 = y0 + data.cellSize
    color = color
    canvas.create_rectangle(x0, y0, x1, y1, fill = color,
                            outline = 'black', width = 4)


# This is the function that draws the board
def drawBoard(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            color = data.board[row][col]
            drawCell(canvas, data, row, col, color)


# This function return the default features of Tetris
def gameDimensions():
    rows = 15
    cols = 10
    cellSize = 20
    margin = 25
    return(rows, cols, cellSize, margin)


# This function set up the window for this game
def playTetris():
    (rows, cols, cellSize, margin) = gameDimensions()
    width = cols * cellSize + 2 * margin
    height = rows * cellSize + 2 * margin
    run(width, height)


# this is the main draw function of the animation
def redrawAll(canvas, data):
    # draw orange background
    canvas.create_rectangle(0, 0, data.width, data.height, fill = 'orange')
    drawBoard(canvas, data)
    drawScore(canvas, data)
    drawFallingPiece(canvas, data)
    if data.isGameOver:
        draw(canvas, data)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill = 'white', width=0)
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
    data.timerDelay = 1000 # milliseconds
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

run(250, 350)
