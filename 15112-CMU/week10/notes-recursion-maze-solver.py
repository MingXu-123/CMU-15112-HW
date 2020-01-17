# mazeSolver.py

from tkinter import *
import random
import math
import copy

############################## backtracking ####################################

NORTH = (-1,  0)
SOUTH = ( 1,  0)
EAST  = ( 0,  1)
WEST  = ( 0, -1)

def isValid(data, row, col, direction):
    if not (0 <= row < len(data.maze) and 0 <= col < len(data.maze[0])):
        return False
    return direction in data.maze[row][col].bridges

def solve(data, row, col, visited, alreadySeen):
    # base case - reach the end of the map and we're done!
    if row == len(data.maze)-1 and col == len(data.maze[0])-1:
        return visited
    # recursive case - try each possible direction from the current point
    for direction in [SOUTH, EAST, NORTH, WEST]:
        drow, dcol = direction
        # It's a valid move if there is a bridge and we haven't visited it
        if isValid(data, row, col, direction) and \
            (row + drow, col + dcol) not in alreadySeen:
            # Make the move by adding the new point to visited and updating the
            # current row/col
            visited.append((row + drow, col + dcol))
            alreadySeen.add((row + drow, col + dcol))
            tmpSolution = solve(data, row + drow, col + dcol, visited, alreadySeen)
            if tmpSolution != None:
                return tmpSolution
            # Make sure to undo the move if the solution doesn't work out!
            visited.pop()
            # We won't undo alreadySeen, because we know we can't reach the end from here.
    return None

def fullSolve(data, row, col, visited, alreadySeen, fullSolution):
    # This version keeps track of each backtracking step, so we can visualize it
    fullSolution.append(copy.deepcopy(visited))
    # base case - reach the end of the map and we're done!
    if row == len(data.maze)-1 and col == len(data.maze[0])-1:
        return visited
    # recursive case - try each possible direction from the current point
    for direction in [SOUTH, EAST, NORTH, WEST]:
        drow, dcol = direction
        # It's a valid move if there is a bridge and we haven't visited it
        if isValid(data, row, col, direction) and \
            (row + drow, col + dcol) not in alreadySeen:
            # Make the move by adding the new point to visited and updating the
            # current row/col
            visited.append((row + drow, col + dcol))
            alreadySeen.add((row + drow, col + dcol))
            tmpSolution = fullSolve(data, row + drow, col + dcol, visited, alreadySeen, fullSolution)
            if tmpSolution != None:
                return tmpSolution
            # Make sure to undo the move if the solution doesn't work out!
            visited.pop()
            # We won't undo alreadySeen, because we know we can't reach the end from here.
    return None
    

def solveMaze(data, getFull=False):
    visited = [(0, 0)]
    alreadySeen = set()
    if getFull:
        fullSolution = []
        sol = fullSolve(data, 0, 0, visited, alreadySeen, fullSolution)
        return fullSolution
    return solve(data, 0, 0, visited, alreadySeen)

############################## interactive #####################################

def keyPressed(event, data):
    row, col = data.playerSpot
    if data.inHelpScreen:
        data.inHelpScreen = False
    elif event.char == "+":
        init(data, data.rows+1, data.cols+1, False)
    elif event.char == "-":
        init(data, data.rows-1, data.cols-1, False)
    elif event.char == "h":
        data.inHelpScreen = True
    elif event.char == "r":
        resetGame(data)
    elif event.char == "p":
        data.isPolar = not data.isPolar
    elif event.char == "c":
        data.cycle = not data.cycle
        resetGame(data)
    elif event.char == "s":
        # toggle solution
        if data.solution == None:
            data.solution = solveMaze(data)
            data.inBacktrack = False
            data.fullSolution = None
            data.backtrackIndex = 0
        else:
            data.solution = None
    elif event.char == "b":
        # toggle backtracking!
        data.inBacktrack = not data.inBacktrack
        data.fullSolution = solveMaze(data, getFull=True)
        data.backtrackIndex = 0
    
    # Different key movement for backtrack mode vs. normal mode
    if data.inBacktrack:
        if event.keysym in ["Up", "Right"] and \
            data.backtrackIndex < len(data.fullSolution)-1:
            data.backtrackIndex += 1
        elif event.keysym in ["Down", "Left"] and data.backtrackIndex > 0:
            data.backtrackIndex -= 1
    else:
        if event.keysym == "Up" and isValid(data, row, col, NORTH):
            doMove(data, row, col, NORTH)
        elif event.keysym == "Down" and isValid(data, row, col, SOUTH):
            doMove(data, row, col, SOUTH)
        elif event.keysym == "Left" and isValid(data, row, col, WEST):
            doMove(data, row, col, WEST)
        elif event.keysym == "Right" and isValid(data, row, col, EAST):
            doMove(data, row, col, EAST)

def resetGame(data):
    rows, cols = len(data.maze), len(data.maze[0])
    data.solution = None
    data.path = [(0, 0)]
    data.playerSpot = (0, 0)
    if data.inBacktrack:
        data.fullSolution = solveMaze(data, getFull=True)
    data.backtrackIndex = 0
    data.maze = makeBlankMaze(rows, cols)
    connectIslands(data, data.maze)
    if data.inBacktrack:
        data.fullSolution = solveMaze(data, getFull=True)
    else:
        data.fullSolution = None

def doMove(data, row, col, direction):
    (drow, dcol) = direction
    if not (0 <= row < len(data.maze) and 0 <= col < len(data.maze[0])): 
        return False
    if len(data.path) >= 2 and data.path[-2] == (row + drow, col + dcol):
        data.path.pop() # undo last move
    elif (row + drow, col + dcol) in data.path:
        return False # we can't move there, it's already in the path!
    else:
        data.path.append((row + drow, col + dcol))
    data.playerSpot = (row + drow, col + dcol)

def mousePressed(event, data): pass

def timerFired(data): pass

##################################### draw #####################################

def redrawAll(canvas, data):
    if data.inHelpScreen: 
        return drawHelpScreen(canvas, data)
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    drawBridges(canvas, data)
    drawIslands(canvas, data)
    if data.inBacktrack:
        highlightPath(canvas, data, data.fullSolution[data.backtrackIndex], data.solutionColor)
    elif data.solution != None: 
        highlightPath(canvas, data, data.solution, data.solutionColor)
    # Draw the current player path
    highlightPath(canvas, data, data.path, data.pathColor)
    (pRow, pCol) = data.playerSpot
    drawCircle(canvas, islandCenter(data, pRow, pCol), 
               data.islandR, data.playerColor)

def drawHelpScreen(canvas, data):
    message = """
arrows to solve manually
s to toggle solution on/off
b to toggle backtrack visualizer on/off
c to toggle cycles on/off
p to toggle circular (polar) on/off
r to reset (make new maze)
+ to increase maze size
- to decrease maze size
h to view this help screen
press any key to continue
"""
    canvas.create_text(data.width/2, 50, text="Maze Solver", 
                       font="Helvetica 32 bold")
    canvas.create_text(data.width/2, data.height/2, text=message, 
                       justify="center", font="Helvetica 24 bold")

def drawIslands(canvas, data):
    for row in range(len(data.maze)):
        for col in range(len(data.maze[0])):
            drawCircle(canvas, islandCenter(data, row, col), 
                       data.islandR, data.islandColor)

def drawCircle(canvas, position, r, color):
    (cx, cy) = position
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=color, width=0)

def islandCenter(data, row, col):
    if data.isPolar:
        cx, cy = data.width/2, data.height/2
        rows, cols = len(data.maze), len(data.maze[0])
        maxR = min(cx, cy)
        r = maxR*(row+1)/(rows+1)
        theta = 2*math.pi*col/cols
        return cx + r*math.cos(theta), cy - r*math.sin(theta)
    else:
        return (col + 0.5) * data.cW, (row + 0.5) * data.cH

def drawBridges(canvas, data):
    for r in range(len(data.maze)):
        for c in range(len(data.maze[0])):
            island = data.maze[r][c]
            # Only draw East and South to avoid duplication
            if EAST in island.bridges:
                canvas.create_line(islandCenter(data, r, c),
                                   islandCenter(data, r, c+1),
                                   fill=data.bridgeColor, width=data.bridgeSize)
            if SOUTH in island.bridges:
                canvas.create_line(islandCenter(data, r, c),
                                   islandCenter(data, r+1, c),
                                   fill=data.bridgeColor, width=data.bridgeSize)

def highlightPath(canvas, data, path, color):
    for i in range(len(path)):
        (row, col) = path[i]
        # Highlight the islands and bridges in the path
        drawCircle(canvas, islandCenter(data, row, col), data.islandR, color)
        if i != len(path)-1:
            (nRow, nCol) = path[i+1]
            canvas.create_line(islandCenter(data, row, col),
                               islandCenter(data, nRow, nCol),
                               fill=color, width=data.bridgeSize)

##################################### init #####################################

def init(data, rows=10, cols=10, inHelpScreen=True):
    if (rows < 1): rows = 1
    if (cols < 1): cols = 1
    data.inHelpScreen = inHelpScreen
    data.rows = rows
    data.cols = cols
    data.islandColor = "dark green"
    data.bridgeColor = "white"
    data.pathColor = "blue"
    data.playerColor = "green"
    data.solutionColor = "red"
    data.inBacktrack = False
    data.fullSolution = None
    data.backtrackIndex = 0
    data.isPolar = False
    data.cycle = False
    data.path = [(0, 0)]
    data.solution = None
    data.playerSpot = (0, 0)
    margin = 5
    data.cW = (data.width - margin) / cols
    data.cH = (data.height - margin) / rows
    data.islandR = min(data.cW, data.cH) / 6
    data.bridgeSize = min(data.cW, data.cH) / 15
    data.margin = margin
    #make the islands
    data.maze = makeBlankMaze(rows,cols)
    #connect the islands
    connectIslands(data, data.maze)

class Island(object):
    def __init__(self, number):
        self.number = number
        self.bridges = { } # start with no bridges


def makeBlankMaze(rows, cols):
    return [ [ Island(row*cols + col) for col in range(cols) ] 
                                      for row in range(rows) ]

def connectIslands(data, islands):
    if data.cycle == True:
        connectCycleIslands(data, islands)
    else:
        connectRegularIslands(data, islands)

def connectCycleIslands(data, islands):
    rows, cols = len(islands), len(islands[0])
    dirs = [ NORTH, EAST, SOUTH, WEST ]
    changeCount = 0
    while solveMaze(data) == None:
        changeMade = False
        while not changeMade:
            row, col = random.randint(0, rows-1), random.randint(0, cols-1)
            start = islands[row][col]
            random.shuffle(dirs)
            (drow, dcol) = dirs[0]
            if (0 <= row + drow < rows and 0 <= col + dcol < cols) and \
               (drow, dcol) not in start.bridges:
                target = islands[row + drow][col + dcol]
                start.bridges[(drow, dcol)] = target
                target.bridges[(-drow,-dcol)] = start
                changeMade = True
                changeCount += 1
        
def connectRegularIslands(data, islands):
    rows, cols = len(islands), len(islands[0])
    for i in range(rows*cols-1):
        makeBridge(islands)

def makeBridge(islands):
    rows, cols = len(islands), len(islands[0])
    dirs = [ NORTH, EAST, SOUTH, WEST ]
    while True:
        row, col = random.randint(0, rows-1), random.randint(0, cols-1)
        random.shuffle(dirs)
        (drow, dcol) = dirs[0]
        start = islands[row][col]
        if not (0 <= row + drow < rows and 0 <= col + dcol < cols):
            continue # out of bounds
        elif (drow, dcol) in start.bridges:
            continue # we already have that bridge!
        target = islands[row + drow][col + dcol]
        if start.number == target.number:
            continue # they're already connected- no cycles!
        start.bridges[(drow, dcol)] = target
        target.bridges[(-drow, -dcol)] = start
        renameIslands(start, target, islands)
        #only got here if a bridge was made
        return

def renameIslands(i1, i2, islands):
    lo, hi = min(i1.number, i2.number), max(i1.number, i2.number)
    for i in range(len(islands)):
        for j in range(len(islands[i])):
            if islands[i][j].number == hi: 
                islands[i][j].number = lo

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

run(600, 600)