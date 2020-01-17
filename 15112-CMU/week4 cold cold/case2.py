from tkinter import *
# Adds shapes on mouse clicks and deletes them on pressing 'd'
def init(data):
    data.circleCenters = [ ]

def mousePressed(event, data):
    newCircleCenter = (event.x, event.y)
    data.circleCenters.append(newCircleCenter)

def keyPressed(event, data):
    # if (event.char == "d"):
    if (event.keysym == "Return"):
        if (len(data.circleCenters) > 0):
            data.circleCenters.pop(0)
        else:
            print("No more circles to delete!")

def redrawAll(canvas, data):
    # draw the circles
    for circleCenter in data.circleCenters:
        (cx, cy) = circleCenter
        r = 20
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="cyan")
    # draw the text
    canvas.create_text(data.width/2, 20,
                       text="Example: Adding and Deleting Shapes")
    canvas.create_text(data.width/2, 40,
                       text="Mouse clicks create circles")
    canvas.create_text(data.width/2, 60,
                       text="Pressing 'd' deletes circles")

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
