from tkinter import *
import math
# This is the init function of animation
def init(data):
    data.torX = data.width/2
    data.torY = data.height/2
    data.commands = listOfDataCode(data)
    data.commandsToDraw = []
    data.torToDraw = []
    data.counter = 0

# Return list of data code
def listOfDataCode(data):
    lstOfDataCode = []
    for line in data.code.split("\n"):
        lstOfDataCode.append(line)
    lstOfDataCode.pop()
    lstOfDataCode = lstOfDataCode[1:]
    return lstOfDataCode


# this is a mouse event handler
def mousePressed(event, data):
    pass


# this is a keyboard event handler
def keyPressed(event, data):
        if (event.keysym == "Return"):
            if data.counter < len(data.commands):
                data.commandsToDraw.append((data.commands[data.counter], data.counter))
                data.counter += 1


# Get information of each command
def getInformationOfCommands(text, color, x, y, angle):
    color = color
    move = 0
    angle = angle
    if text.startswith('color') and "#" not in text:
        color = text[6:]
        if color == None:
            color = "white"
    elif text.startswith('color') and "#" in text:
        color = text.split(" ")[1]
        if color == None:
            color = "white"
    elif text.startswith('left'):
        angle = + int(text[5:])
    elif text.startswith('right'):
        angle = - int(text[6:])
    elif text.startswith('move'):
        move = int(text[5:])
    x = x + move * math.cos((angle/360)*2*math.pi)
    if angle < 0:
        y = y - move * math.sin((angle/360)*2*math.pi)
    else:
        y = y + move * math.sin((angle/360)*2*math.pi)
    if text == []:
        color, x, y, angle = color, x, y, angle
    return color, x, y, angle


# This is the run current line function
def runProgram(canvas, data, currentLine):
    color = ""
    angle = 0
    for i in range(currentLine):
        # print(data.commandsToDraw[i])
        canvas.create_text(data.width/50,
                           data.height/20 + data.commandsToDraw[i][1]*data.height/30,
                           text=str(data.commandsToDraw[i][0]), anchor="w", fill='gray')
        color,data.torX,data.torY,angle = \
            getInformationOfCommands(data.commandsToDraw[i][0], color, data.torX, data.torY, angle)

    # print(color, data.torX, data.torY, angle)
    drawArrow(canvas, data.torX, data.torY, angle)
        # color, data.torX, data.torY, angle = drawArrow(canvas, data.torX, data.torY, angle)
        # print(color, data.torX, data.torY, angle,"hhh")

# this function get the coordinate of the black rectangle
def getCoordinateOfRectangle(width, height):
    recx0 = 0
    recy0 = (9 / 10) * height
    recx1 = width
    recy1 = height
    return recx0, recy0, recx1, recy1

# this function get the color of the small rectangles
def getColorOfBox(i):
    if i == 0:
        color = 'red'
    elif i == 1:
        color = 'orange'
    elif i == 2:
        color = 'yellow'
    elif i == 3:
        color = 'green'
    elif i == 4:
        color = 'blue'
    elif i == 5:
        color = 'purple'
    else:
        color = 'white'
    return color


# this function get the coordinates of the small rectangles
def coordinatesInLoop(margin, i, widthOfRectangles, recy0):
    x0 = margin + i * widthOfRectangles + i * margin
    y0 = recy0 + margin
    x1 = x0 + widthOfRectangles
    y1 = y0 + widthOfRectangles - margin
    return x0, y0, x1, y1


# this is the main animation function
def redrawAll(canvas, data):
    runProgram(canvas, data, data.counter)
    margin = (1/100)*data.height
    widthOfRectangles = (data.width - 11 * margin)/10
    recx0, recy0, recx1, recy1 = getCoordinateOfRectangle(data.width, data.height)
    canvas.create_rectangle(recx0, recy0, recx1, recy1, fill='black')
    for i in range(10):
        x0, y0, x1, y1 = coordinatesInLoop(margin, i, widthOfRectangles, recy0)
        color = getColorOfBox(i)
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)


""" This function is provided as part of the starter code.
You don't need to change it, but you should call it!"""
def drawArrow(canvas, x, y, angle):
    offset = 135
    r = 10
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y - r*math.sin(math.radians(angle))
    x2 = x + r*math.cos(math.radians(angle + offset))
    y2 = y - r*math.sin(math.radians(angle + offset))
    x3 = x + r*math.cos(math.radians(angle - offset))
    y3 = y - r*math.sin(math.radians(angle - offset))
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="black")


def runTortoiseAnimation(code, width=500, height=500):
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

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.code = code
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAllWrapper(canvas, data)
    root.mainloop()  # blocks until window is closed

def testTortoiseAnimation():
    print("Running Tortoise Animation...", end="")
    runTortoiseAnimation("""
# This is a simple tortoise program
color blue
move 50

left 90

color red
move 100

color none # turns off drawing
move 50

right 45

color green # drawing is on again
move 50

right 45

color orange
move 50

right 90

color purple
move 100
""")
#     runTortoiseAnimation("""
# # Y
# color red
# right 45
# move 50
# right 45
# move 50
# right 180
# move 50
# right 45
# move 50
# color none # space
# right 45
# move 25
#
# # E
# color green
# right 90
# move 85
# left 90
# move 50
# right 180
# move 50
# right 90
# move 42
# right 90
# move 50
# right 180
# move 50
# right 90
# move 43
# right 90
# move 50  # space
# color none
# move 25
#
# # S
# color blue
# move 50
# left 180
# move 50
# left 90
# move 43
# left 90
# move 50
# right 90
# move 42
# right 90
# move 50
# """)
    print("Done.")

testTortoiseAnimation()