# FloodFill using Tkinter
# grid-based (not pixel-based), with animation
# and numeric display of depth of recursion

from tkinter import *

class Cell(object):
    def __init__(self):
        self.depth = self.ordinal = -1 # set by floodFill
        self.displayLabel = False
        self.isWall = False

def init(data):
    instructHeight = 160
    data.cellSize = 40
    data.margin = 5 # margin around grid
    data.rows = (data.height - instructHeight - 2*data.margin) // data.cellSize
    data.cols = (data.width - 2*data.margin) // data.cellSize
    data.cells = [ [ Cell() for col in range(data.cols) ] 
                            for row in range(data.rows) ]
    data.floodFillIndex = 0
    data.displayOrdinals = False

def clearLabels(data):
    for row in range(data.rows):
        for col in range(data.cols):
            cell = data.cells[row][col]
            cell.depth = cell.ordinal = -1
    data.floodFillOrder = [ ]
    data.floodFillIndex = 0
    data.displayOrdinals = False

def floodFill(data, row, col, depth=0):
    if ((row < 0) or (row >= data.rows) or
        (col < 0) or (col >= data.cols)):
        return # off-board!
    cell = data.cells[row][col]
    if (cell.isWall == True):
        return # hit a wall
    if (cell.depth >= 0):
        return # already been here

    # "fill" this cell
    cell.depth = depth
    cell.ordinal = len(data.floodFillOrder)
    data.floodFillOrder.append(cell)

    # then recursively fill its neighbors
    floodFill(data, row-1, col,   depth+1)
    floodFill(data, row+1, col,   depth+1)
    floodFill(data, row,   col-1, depth+1)
    floodFill(data, row,   col+1, depth+1)

def mousePressed(event, data):
    shift = ((event.state & 0x0001) != 0) # Fancy detection of shift-click!
    clearLabels(data)
    col = (event.x - data.margin) // data.cellSize
    row = (event.y - data.margin) // data.cellSize
    if 0 <= col < data.cols and 0 <= row < data.rows:
        if (shift == False):
            data.cells[row][col].isWall = not data.cells[row][col].isWall
        else:
            data.cells[row][col].isWall = False
            floodFill(data, row, col)

def keyPressed(event, data):
    if (event.keysym == "d"):
        data.displayOrdinals = False
    elif (event.keysym == "o"):
        data.displayOrdinals = True
    elif (event.keysym == "r"):
        init(data)

def timerFired(data):
    data.floodFillIndex += 1

def redrawAll(canvas, data):
    for row in range(data.rows):
        for col in range(data.cols):
            left = data.margin + col * data.cellSize
            top = data.margin + row * data.cellSize
            cell = data.cells[row][col]
            fill = "pink" if (cell.isWall) else "cyan"
            canvas.create_rectangle(left, top, 
                left + data.cellSize, top + data.cellSize, fill=fill)
            if ((cell.depth >= 0) and (cell.ordinal < data.floodFillIndex)):
                if (data.displayOrdinals == True):
                    label = "# " + str(cell.ordinal)
                else:
                    label = str(cell.depth)
                canvas.create_text(left + data.cellSize/2, 
                                   top + data.cellSize/2,
                                   text=label, font="Arial 12 bold", 
                                   fill="darkGreen")
    drawHelpText(canvas, data)

def drawHelpText(canvas, data):
    message = """
Click to toggle walls
Shift-click to floodFill from cell
Press 'd' to display depths
Press 'o' to display #ordinals
Press 'r' to reset
"""
    canvas.create_text(data.width/2, data.cellSize * data.rows, anchor="n",
                       text = message, font="Arial 18 bold", 
                       fill="darkBlue", justify="center")

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
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

run(610, 550)