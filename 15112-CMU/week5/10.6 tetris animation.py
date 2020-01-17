#################################################
# Hw6
# Your andrewID: yilunw
# Your section: F
#################################################
from tkinter import *
#################################################
# Hw6-tetris
#################################################
def gameDimentions(data):
    data.rows = 15
    data.cols = 10
    data.cellSize = 20
    data.margin = 25
    return (data.rows,data.cols,data.cellSize,data.margin)
    
def init(data):
    (data.rows,data.cols,data.cellSize,data.margin) = gameDimentions(data)
    data.emptyColor = "#CFD8DC"
    data.board = []
    #fill the board, which is a 2D list, with the empty color
    data.board += [[data.emptyColor for col in range(data.cols)]\
                                    for row in range(data.rows)]
    data.board2 = []
    data.board2 += [[data.emptyColor for col in range(4)]\
                                    for row in range(4)]
    # Seven "standard" pieces (tetrominoes)
    data.iPiece = [
        [  True,  True,  True,  True ]
    ]

    data.jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    data.lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    data.oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    data.sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    data.tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    data.zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]
    data.tetrisPieces = [data.iPiece, data.jPiece, data.lPiece, data.oPiece, \
                                        data.sPiece, data.tPiece, data.zPiece]
    data.tetrisPieceColors = ["red", "#FFEB3B", "violet", "#EC407A", \
                                        "#00ACC1", "green", "blue"]
    data.paused = False
    firstFallingPiece = newFallingPiece(data)
    data.score = 0
    data.isGameOver = False

def drawCell(canvas,data,row,col):
    #draw every cell
    boardWidth  = data.width - 2*data.margin
    boardHeight = data.height - 2*data.margin
    cellBoundsWidth = 3
    canvas.create_rectangle(data.margin + data.cellSize*col, data.margin + \
    data.cellSize*row, data.margin + data.cellSize*(col+1), data.margin + \
    data.cellSize*(row+1), fill = data.board[row][col], width = cellBoundsWidth)

def drawBoard(canvas, data):
    #draw the board by filling every cells(using draw cells)
    for row in range(data.rows):
        for col in range(data.cols):
            drawCell(canvas,data,row,col) 

def newFallingPiece(data):
    import random
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = data.tetrisPieces[randomIndex]
    data.fallingPieceRow = 0
    data.fallingPieceCol = data.cols//2 - len(data.fallingPiece[0])//2
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex]
    data.numFallingPieceRow = len(data.fallingPiece)
    data.numFallingPieceCol = len(data.fallingPiece[0])
    
def drawFallingPiece(canvas, data):
    #find out the boolean value(True/False) to draw falling pieces
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col] == True:
                color = data.fallingPieceColor
                pieceRow = data.fallingPieceRow + row
                pieceCol = data.fallingPieceCol + col
                cellBoundsWidth = 3
                canvas.create_rectangle(data.margin + data.cellSize*pieceCol, \
                data.margin + data.cellSize*pieceRow, \
                data.margin + data.cellSize*(pieceCol+1), \
                data.margin + data.cellSize*(pieceRow+1), \
                fill = data.fallingPieceColor, width = cellBoundsWidth)

def moveFallingPiece(data, drow, dcol):
    if data.paused == False:
        data.fallingPieceRow += drow
        data.fallingPieceCol += dcol
        if fallingPieceIsLegal(data) == False:
            data.fallingPieceRow -= drow
            data.fallingPieceCol -= dcol
            return False
        return True

def hardDropFallingPiece(data):
    if data.paused == False:
        while fallingPieceIsLegal(data):
            data.fallingPieceRow += 1
        data.fallingPieceRow -= 1

def fallingPieceIsLegal(data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            pieceRow = data.fallingPieceRow + row
            pieceCol = data.fallingPieceCol + col
            if data.fallingPiece[row][col] == True:
                #to check if it's on the board
                if pieceRow < 0 or pieceRow >= data.rows or \
                        pieceCol < 0 or pieceCol >= data.cols:
                    return False
                    #to check if the color of the cell's location is emptyColor
                if data.board[pieceRow][pieceCol] != data.emptyColor:
                    return False
    return True

def rotateFallingPiece(data):
    if data.paused == False:
        import copy
        #set temp local variables that restores the old datas, \
        #which may be used if the new piece is illegal
        oldRow = data.fallingPieceRow
        oldCol = data.fallingPieceCol
        oldNumRows = data.numFallingPieceRow
        oldNumCols = data.numFallingPieceCol
        #compute the new locations
        newRow = oldRow + oldNumRows//2 - oldNumCols//2
        newCol = oldCol + oldNumCols//2 - oldNumRows//2 
        newNumRows = oldNumCols
        newNumCols = oldNumRows
        oldPieceList = copy.deepcopy(data.fallingPiece)
        #create a new 2D list for storing the rotated piece
        newPieceList = []
        newPieceList += [[None for col in range(newNumCols)]\
                                for row in range(newNumRows)]
        #rotate the whole piece counterclockwise
        for row in range(len(newPieceList)):
            for col in range(len(newPieceList[0])):
                newPieceList[row][col] = data.fallingPiece\
                    [col][oldNumCols-1-row]
        #if the piece is legal, just return that piece on the board
        data.fallingPiece = newPieceList
        data.fallingPieceRow = newRow
        data.fallingPieceCol = newCol
        data.numFallingPieceRow = newNumRows
        data.numFallingPieceCol = newNumCols
        #if the rotated piece is not legal, go back to the previous step
        if fallingPieceIsLegal(data) == False:
            data.fallingPiece = oldPieceList
            data.fallingPieceRow = oldRow 
            data.fallingPieceCol = oldCol
            data.numFallingPieceRow = oldNumRows
            data.numFallingPieceCol = oldNumCols 

def rotateFallingPieceClockwise(data):
    if data.paused == False:
        import copy
        #set temp local variables that restores the old datas, \
        #which may be used if the new piece is illegal
        oldRow = data.fallingPieceRow
        oldCol = data.fallingPieceCol
        oldNumRows = data.numFallingPieceRow
        oldNumCols = data.numFallingPieceCol
        #compute the new locations
        newRow = oldRow + oldNumRows//2 - oldNumCols//2
        newCol = oldCol + oldNumCols//2 - oldNumRows//2 
        newNumRows = oldNumCols
        newNumCols = oldNumRows
        oldPieceList = copy.deepcopy(data.fallingPiece)
        #create a new 2D list for storing the rotated piece
        newPieceList = []
        newPieceList += [[None for col in range(newNumCols)]\
                                for row in range(newNumRows)]
        #rotate the whole piece clockwise
        for row in range(len(newPieceList)):
            for col in range(len(newPieceList[0])):
                newPieceList[row][col] = data.fallingPiece\
                    [oldNumRows-1-col][row]
        #if the piece is legal, just return that piece on the board
        data.fallingPiece = newPieceList
        data.fallingPieceRow = newRow
        data.fallingPieceCol = newCol
        data.numFallingPieceRow = newNumRows
        data.numFallingPieceCol = newNumCols
        #if the rotated piece is not legal, go back to the previous step
        if fallingPieceIsLegal(data) == False:
            data.fallingPiece = oldPieceList
            data.fallingPieceRow = oldRow 
            data.fallingPieceCol = oldCol
            data.numFallingPieceRow = oldNumRows
            data.numFallingPieceCol = oldNumCols 

def removeFullRows(data): 
    import copy
    index = data.rows-1
    #create an empty board for checking full rows
    board = []
    board += [[data.emptyColor for col in range(data.cols)]\
                                for row in range(data.rows)]
    count = 0
    #eliminate every full row (not containing any emptyColor) \
    #and count the score based on the number of full rows
    for row in range(data.rows-1, -1, -1):
        if data.emptyColor not in data.board[row]:
            count += 1
        else:
            board[index] = copy.deepcopy(data.board[row])
            index -= 1
    data.board = board
    data.score += count**2
    
def placeFallingPiece(data):
    for row in range(data.numFallingPieceRow):
        for col in range(data.numFallingPieceCol):
            #to "insert" that piece into the board(so it cannot move)
            if data.fallingPiece[row][col] == True:
                data.board[data.fallingPieceRow+row][data.fallingPieceCol+col]\
                        = data.fallingPieceColor
    removeFullRows(data)

'''
def drawCell2(canvas,data,row,col):
    #draw every cell
    boardWidth  = data.width - 2*data.margin
    boardHeight = data.height - 2*data.margin
    cellBoundsWidth = 3
    canvas.create_rectangle(data.margin + data.cellSize*(data.cols+3+col), \
        data.margin + data.cellSize*(data.rows//2+row), \
        data.margin + data.cellSize*(data.cols+col+4), \
        data.margin + data.cellSize*(data.rows//2+row+1), \
        fill = data.board2[row][col], width = cellBoundsWidth)
    
def drawBoard2(canvas, data):
    #draw the board by filling every cells(using draw cells)
    for row in range(4):
        for col in range(4):
            drawCell2(canvas,data,row,col) 

def drawNextFallingPiece(canvas, data):
    #find out the boolean value(True/False) to draw the next falling piece
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col] == True:
                color = data.fallingPieceColor
                pieceRow = data.fallingPieceRow + data.rows//2 + row
                pieceCol = data.fallingPieceCol + data.cols + col
                cellBoundsWidth = 3
                canvas.create_rectangle(data.margin + data.cellSize*pieceCol, \
                data.margin + data.cellSize*pieceRow, \
                data.margin + data.cellSize*(pieceCol+1), \
                data.margin + data.cellSize*(pieceRow+1), \
                fill = data.fallingPieceColor, width = cellBoundsWidth)
'''

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "a":
        rotateFallingPiece(data)
    elif event.keysym == "d":
        rotateFallingPieceClockwise(data)
    elif event.keysym == "Down":
        moveFallingPiece(data, 1, 0)
    elif event.keysym == "Left":
        moveFallingPiece(data, 0, -1)
    elif event.keysym == "Right":
        moveFallingPiece(data, 0, 1)
    elif event.keysym == "space":
        hardDropFallingPiece(data)
    elif event.keysym == "p":
        data.paused = not data.paused#pause the game (can return back)
    elif event.keysym == "r":
        data = init(data)#restart the game

def timerFired(data):
    if data.paused == False:
        if data.isGameOver == True:
            return #stop generate any new piece, thus end the game
        if moveFallingPiece(data, +1, 0) == False:
            placeFallingPiece(data)
            newFallingPiece(data) #generate a new piece
            if fallingPieceIsLegal(data) == False:
                data.isGameOver = True
    
def redrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width,data.height, fill = "#29B6F6")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    '''
    drawBoard2(canvas, data)
    drawNextFallingPiece(canvas, data) 
    canvas.create_text(data.width*(4/5), data.height/3, \
                            text = "Next\nFalling\nPiece:" ,\
                            font = "Arial 23 bold", fill = "purple" )
    #need to be revised
    '''
    canvas.create_text(data.width/2, data.margin/2, \
                            text = "Score:" + str(data.score) ,\
                            font = "Arial 23 bold", fill = "purple" )
    #if the tetris game pauses, return "Game Paused!" message                       
    if data.paused == True:
        canvas.create_rectangle(0, data.height/3, data.width, \
                                            data.height*(2/3), fill = "gold")
        canvas.create_text(data.width/2, data.height/2, text = "Game Paused!",\
                            font = "TimesNewRoman 35 bold", fill = "red")
    #if the tetris game ends, return "Game Over!" message
    if data.isGameOver == True:
        canvas.create_rectangle(0, data.height/6, data.width, data.height/3, \
                                                        fill = "gold")
        canvas.create_text(data.width/2, data.height/4, text = "Game Over!",\
                            font = "TimesNewRoman 35 bold", fill = "red")

def playTetris(width, height):
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
    data.timerDelay = 500 # milliseconds
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
    
playTetris(250,350)