# Basic Animation Framework

from tkinter import *

####################################
# customize these functions
####################################


def init(data):
    # data comes preset with width and height, from the run function
    data.circleSize = min(data.width, data.height) / 10
    data.circleX = data.width/2
    data.circleY = data.height/2
    data.charText = ""
    data.keysymText = ""


def mousePressed(event, data):
    data.circleX = event.x
    data.circleY = event.y


def keyPressed(event, data):
    data.charText = event.char
    data.keysymText = event.keysym

def redrawAll(canvas, data):
    canvas.create_oval(data.circleX - data.circleSize,
                       data.circleY - data.circleSize,
                       data.circleX + data.circleSize,
                       data.circleY + data.circleSize)
    if data.charText != "":
        canvas.create_text(data.width/10, data.height/3,
                           text="char: " + data.charText)
    if data.keysymText != "":
        print(type(data.keysymText))
        canvas.create_text(data.width/10, data.height*2/3,
                           text="keysym: " + data.keysymText)

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