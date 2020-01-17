from tkinter import *

def init(data):
    data.level = 1

def drawSierpinskiTriangle(canvas, x, y, size, level):
    # (x,y) is the lower-left corner of the triangle
    # size is the length of a side
    # Need a bit of trig to calculate the top point
    if level == 0:
        topY = y - (size**2 - (size/2)**2)**0.5
        canvas.create_polygon(x, y, x + size, y, x + size/2, topY,
                              fill="black")
    else:
        print(level)
        # Bottom-left triangle
        drawSierpinskiTriangle(canvas, x, y, size/2, level-1)
        # Bottom-right triangle
        drawSierpinskiTriangle(canvas, x + size/2, y, size/2, level-1)
        # Top triangle
        midY = y - ((size/2)**2 - (size/4)**2)**0.5
        drawSierpinskiTriangle(canvas, x + size/4, midY, size/2, level-1)


def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif (event.keysym in ["Down", "Left"]) and (data.level > 0):
        data.level -= 1

def redrawAll(canvas, data):
    margin = min(data.width, data.height)//10
    x, y = margin, data.height - margin
    size = min(data.width, data.height) - 2*margin
    drawSierpinskiTriangle(canvas, x, y, size, data.level)
    canvas.create_text(data.width / 2, 0,
                       text="Level %d Fractal" % (data.level),
                       font="Arial " + str(int(margin / 3)) + " bold",
                       anchor="n")
    canvas.create_text(data.width / 2, margin,
                       text="Use arrows to change level",
                       font="Arial " + str(int(margin / 4)),
                       anchor="s")

def mousePressed(event, data): pass

def timerFired(data): pass

# Updated Animation Starter Code

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

run(400, 400)