from tkinter import *

def init(data):
    data.level = 1

def drawFractal(canvas, level, otherParams):
    if level == 0:
        pass # base case
    else:
        pass # recursive case; call drawFractal as needed with level-1

def keyPressed(event, data):
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif (event.keysym in ["Down", "Left"]) and (data.level > 0):
        data.level -= 1

def redrawAll(canvas, data):
    margin = min(data.width, data.height)//10
    otherParams = None
    drawFractal(canvas, data.level, otherParams)
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

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
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
    redrawAllWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 200)