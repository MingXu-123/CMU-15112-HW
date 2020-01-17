from tkinter import *
# moves the green square using the arrow keys
def init(data):
    data.squareX = data.width/2
    data.squareY = data.height/2

def mousePressed(event, data):
    pass

def keyPressed(event, data):
    if event.keysym == "Up":
        data.squareY -= 20
    elif event.keysym == "Down":
        data.squareY += 20
    elif event.keysym == "Left":
        data.squareX -= 20
    elif event.keysym == "Right":
        data.squareX += 20

def redrawAll(canvas, data):
    # draw the text
    canvas.create_text(data.width/2, 20,
                       text="Example: Arrow Key Movement")
    canvas.create_text(data.width/2, 40,
                       text="Pressing the arrow keys moves the square")
    # draw the square
    size = 50
    canvas.create_rectangle(data.squareX - size, data.squareY - size,
                            data.squareX + size, data.squareY + size,
                            fill="green")




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
